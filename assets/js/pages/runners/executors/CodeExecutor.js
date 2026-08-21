export class CodeExecutor {
  constructor({ editor, outputElement, execTimeElement, languageSelect, pythonURI, javaURI, fetchOptions = {}, expectedOutput = '', resultElement = null } = {}) {
    this.editor = editor;
    this.outputElement = outputElement;
    this.execTimeElement = execTimeElement;
    this.languageSelect = languageSelect;
    this.pythonURI = pythonURI;
    this.javaURI = javaURI;
    this.fetchOptions = fetchOptions;
    this.expectedOutput = expectedOutput;
    this.resultElement = resultElement;
  }

  checkExpected(actualOutput) {
    if (!this.resultElement || !this.expectedOutput) return;

    const normalize = (s) => String(s).trim().replace(/\r\n/g, '\n');
    const passed = normalize(actualOutput) === normalize(this.expectedOutput);

    this.resultElement.textContent = passed
      ? '✅ Output matches expected'
      : '❌ Output doesn\'t match yet';
    this.resultElement.style.color = passed ? 'var(--green, #2ecc71)' : 'var(--red, #e74c3c)';
  }

  async run() {
    const code = this.editor?.getValue?.() || '';
    const lang = this.languageSelect?.value || 'python';
    const outputDiv = this.outputElement;
    const execTimeSpan = this.execTimeElement;

    if (!outputDiv) {
      throw new Error('CodeExecutor requires an output element');
    }

    outputDiv.textContent = '⏳ Running...';
    if (execTimeSpan) execTimeSpan.textContent = '';
    if (this.resultElement) this.resultElement.textContent = '';

    const startTime = Date.now();
    const isLocalhost = location.hostname === 'localhost' || location.hostname === '127.0.0.1';

    let runURL;
    if (lang === 'python') runURL = `${this.pythonURI}/run/python`;
    else if (lang === 'java') runURL = `${this.javaURI}/run/java`;
    else if (lang === 'javascript') runURL = `${this.pythonURI}/run/javascript`;
    else throw new Error(`Unsupported language: ${lang}`);

    const body = JSON.stringify({ code });
    const options = { ...this.fetchOptions, method: 'POST', body };

    try {
      const res = await fetch(runURL, options);
      const result = await res.json();
      const output = result.output || '[no output]';

      if (lang === 'javascript' && isLocalhost && output.includes("No such file or directory: 'node'")) {
        throw new Error('Node.js not available on backend');
      }

      outputDiv.textContent = output;
      if (execTimeSpan) {
        execTimeSpan.textContent = `⏱Execution time: ${Date.now() - startTime}ms`;
      }
      this.checkExpected(output);
    } catch (err) {
      if (lang === 'javascript' && isLocalhost) {
        this.runJavaScriptFallback(code, startTime);
      } else {
        outputDiv.textContent = 'Error: ' + err.message;
        if (execTimeSpan) execTimeSpan.textContent = '';
      }
    }
  }

  runJavaScriptFallback(code, startTime) {
    const outputDiv = this.outputElement;
    const execTimeSpan = this.execTimeElement;

    try {
      const logs = [];
      const originalLog = console.log;
      console.log = function(...args) {
        logs.push(args.map(arg => String(arg)).join(' '));
        originalLog.apply(console, args);
      };

      eval(code);
      console.log = originalLog;

      const output = logs.length > 0 ? logs.join('\n') : '[no output]';
      outputDiv.textContent = output;
      if (execTimeSpan) {
        execTimeSpan.textContent = `⏱Execution time: ${Date.now() - startTime}ms (local fallback)`;
      }
      this.checkExpected(output);
    } catch (evalErr) {
      outputDiv.textContent = 'Error: ' + evalErr.message;
      if (execTimeSpan) execTimeSpan.textContent = '';
    }
  }

  bindCopyOutput(button) {
    if (!button || !this.outputElement) return;

    button.addEventListener('click', () => {
      const output = this.outputElement.textContent;
      const original = button.textContent;
      navigator.clipboard.writeText(output).then(() => {
        button.textContent = '✔';
        setTimeout(() => {
          button.textContent = original;
        }, 1200);
      });
    });
  }
}

export default CodeExecutor;
