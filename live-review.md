---
layout: post
title: "Live Review: Sprint 1"
permalink: /live-review/
search_exclude: true
hide: true
---

<p style="max-width: 700px;">
My checklist for the Sprint 1 Live Review (<a href="https://github.com/Open-Coding-Society/portfolio/issues/47">Open-Coding-Society/portfolio#47</a>),
all in one page. <strong>Individual</strong> items I present myself; <strong>Team</strong> items I cover live with my CSA crew.
</p>

<div style="display:flex; gap:8px; flex-wrap:wrap; margin: 16px 0;">
  <a href="#setup" style="text-decoration:none; padding:6px 12px; border-radius:5px; background-color: var(--green); color:black; font-weight:bold; font-size:0.9em;">1. Portfolio Setup</a>
  <a href="#sdlc" style="text-decoration:none; padding:6px 12px; border-radius:5px; background-color: var(--blue); color:white; font-weight:bold; font-size:0.9em;">2. SDLC Steps</a>
  <a href="#progress" style="text-decoration:none; padding:6px 12px; border-radius:5px; background-color: var(--warn); color:black; font-weight:bold; font-size:0.9em;">3. Unit 1-4 Progress</a>
  <a href="#unicorn" style="text-decoration:none; padding:6px 12px; border-radius:5px; background-color: var(--orange); color:white; font-weight:bold; font-size:0.9em;">4. My Unicorn</a>
  <a href="#team" style="text-decoration:none; padding:6px 12px; border-radius:5px; background-color: var(--red); color:white; font-weight:bold; font-size:0.9em;">Team</a>
</div>

<hr>

<h2 id="setup">
  <span style="font-size:0.55em; vertical-align:middle; background-color: var(--green); color:black; padding:2px 8px; border-radius:4px; margin-right:8px;">INDIVIDUAL</span>
  1. Portfolio Setup
</h2>

<p>Forked from the <a href="https://github.com/Open-Coding-Society/portfolio">Open-Coding-Society/portfolio</a> template, personalized, and deployed on my own GitHub Pages.</p>

- ✅ Created [Wick2009/portfolio](https://github.com/Wick2009/portfolio) from the template, cloned locally
- ✅ Personalized `_config.yml` (name, title, GitHub info)
- ✅ Enabled GitHub Pages with the Actions build source
- ✅ Confirmed a push triggers a real rebuild and the live site updates

**Live site**: [wick2009.github.io/portfolio](https://wick2009.github.io/portfolio/) — deployed under my own account, not a template screenshot.
**Repo**: [github.com/Wick2009/portfolio](https://github.com/Wick2009/portfolio)

<h4>Tools check, straight from my own terminal</h4>

```
$ python3 --version
Python 3.10.1

$ ruby -v
ruby 3.3.10 (2025-10-23 revision 343ea05002) [arm64-darwin25]

$ bundle exec jekyll -v
jekyll 3.9.5

$ git config --global user.name
Wick2009

$ git remote -v
origin  https://github.com/Wick2009/portfolio.git (fetch)
origin  https://github.com/Wick2009/portfolio.git (push)
```

Python + Ruby/Jekyll is what actually builds and serves this site locally (`make serve`) — that's the toolchain I use day to day. I don't have a local JDK installed; AP CSA Java work for this portfolio lives in the unit notebooks rather than a local `java` install.

<h2 id="sdlc">
  <span style="font-size:0.55em; vertical-align:middle; background-color: var(--blue); color:white; padding:2px 8px; border-radius:4px; margin-right:8px;">INDIVIDUAL</span>
  2. SDLC Steps for Updating My Portfolio
</h2>

<p>Every portfolio change follows Plan → Design → Develop → Test → Deploy → Maintain. Rather than describe this in the abstract, I walked one real change through all six — including a revision after feedback, since that's most of what real dev work actually looks like.</p>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0;">
    <a href="{{site.baseurl}}/sdlc" style="text-decoration: none;">
        <div style="background-color: var(--blue); color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
           See the full SDLC walkthrough →
        </div>
    </a>
</div>

Quick summary of that page: 🧭 Plan → 🎨 Design → 🛠️ Develop → 🧪 Test → 🚀 Deploy → 🔧 Maintain, each phase backed by a real commit link and a real GitHub Actions run link — not a hypothetical.

<h2 id="progress">
  <span style="font-size:0.55em; vertical-align:middle; background-color: var(--warn); color:black; padding:2px 8px; border-radius:4px; margin-right:8px;">INDIVIDUAL</span>
  3. Unit 1-4 Progress
</h2>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0;">
{% for u in site.data.csa_units %}
  {% assign colors = "green,blue,warn,orange" | split: "," %}
  {% assign color = colors[forloop.index0] %}
  {% assign lesson_total = u.lessons.size %}
  {% if u.quiz %}{% assign lesson_total = lesson_total | plus: 1 %}{% endif %}
  <a href="{{site.baseurl}}{{ u.first_real_permalink }}" style="text-decoration:none;">
  <div style="background-color: var(--{{ color }}); color: {% if color == 'green' or color == 'warn' %}black{% else %}white{% endif %}; padding: 10px 16px; border-radius: 5px; font-weight: bold; min-width: 120px;">
    Unit {{ u.unit }}<br>
    <span style="font-weight: normal; font-size: 0.9em;">{{ lesson_total }} lessons</span>
  </div>
  </a>
{% endfor %}
</div>

52 lessons, homeworks, and quizzes copied in across Units 1-4 from the class's AP CSA MCQ notebooks (`Open-Coding-Society/pages`). Rather than screenshot each unit folder, the actual evidence is a working, searchable page:

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0;">
    <a href="{{site.baseurl}}/csa/dashboard" style="text-decoration: none;">
        <div style="background-color: var(--teal); color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
           Open the full Lesson Index →
        </div>
    </a>
</div>

<h2 id="unicorn">
  <span style="font-size:0.55em; vertical-align:middle; background-color: var(--orange); color:white; padding:2px 8px; border-radius:4px; margin-right:8px;">INDIVIDUAL</span>
  4. My Unicorn
</h2>

<p style="max-width:700px;">
Before picking a unicorn, I checked what classmates had already built for theirs, so mine wouldn't
just repeat someone else's idea. A few had converged on embedding the class's Code Runner directly
into lessons. One had hand-written a static checklist flagging which copied notebooks were still
empty placeholders — clever, but it only means anything while lessons are unfinished; once every
lesson gets written, a page whose whole point is "here's what's missing" has nothing left to say.
</p>

<p style="max-width:700px;">
My unicorn has two parts. <strong>Part 1</strong> is the <strong>CSA Lesson Index</strong>: a script that scans all 52 lesson notebooks
and generates a single searchable page — type a lesson number or keyword, jump straight to it,
check it off as you finish, and that progress is remembered next time you're back. It replaces
digging through 4 nested folders of notebooks with one page. I also went through one real
revision on it after review feedback, which is documented end-to-end on the
<a href="{{site.baseurl}}/sdlc">SDLC page</a> — the stub-auditing version got cut once I realized
it wouldn't hold up once lessons are actually finished.
</p>

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0;">
    <a href="{{site.baseurl}}/csa/dashboard" style="text-decoration: none;">
        <div style="background-color: var(--teal); color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold;">
           Try the Lesson Index →
        </div>
    </a>
    <a href="https://github.com/Wick2009/portfolio/blob/main/scripts/generate_csa_lesson_index.py" style="text-decoration: none;">
        <div style="background-color: var(--panel, #333); color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold; border: 1px solid #888;">
           View the script →
        </div>
    </a>
</div>

<h3>Part 2: an actual improvement to the Code Runner</h3>

<p style="max-width:700px;">
The class Code Runner (<code>_includes/runners/code.html</code>) runs code and prints raw output
— it has no way to tell you whether that output is <em>correct</em>, so every existing example
I've seen relies on a human eyeballing it. I added an optional <code>expected</code> parameter:
when a lesson author sets it, the runner compares the program's real output against it and shows
a ✅/❌ badge automatically. Fully backward compatible — existing runners that don't pass
<code>expected</code> behave exactly as before.
</p>

<p style="max-width:700px;">Try it — hit Run below:</p>

{% capture unicorn_demo_challenge %}
This should print 1 through 5, each on its own line. Hit Run — the badge under the output
auto-checks it against the expected result. Then try breaking the loop bound and run again.
{% endcapture %}

{% capture unicorn_demo_code %}
public class Demo {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println(i);
        }
    }
}
{% endcapture %}

{% capture unicorn_demo_expected %}1
2
3
4
5{% endcapture %}

{% include runners/code.html
   runner_id="unicorn-demo"
   language="java"
   challenge=unicorn_demo_challenge
   code=unicorn_demo_code
   expected=unicorn_demo_expected
%}

<div style="display: flex; flex-wrap: wrap; gap: 10px; margin: 16px 0;">
    <a href="https://github.com/Wick2009/portfolio/commit/7dac92f" style="text-decoration: none;">
        <div style="background-color: var(--panel, #333); color: white; padding: 10px 20px; border-radius: 5px; font-weight: bold; border: 1px solid #888;">
           View the runner change →
        </div>
    </a>
</div>

<h2 id="team">
  <span style="font-size:0.55em; vertical-align:middle; background-color: var(--red); color:white; padding:2px 8px; border-radius:4px; margin-right:8px;">TEAM</span>
  Office Hours + Sprint 1 Friends
</h2>

<p style="max-width:700px;">
Team task, covered live rather than as a write-up here: Office Hours attendance and introducing my
CSA Sprint 1 crew happen in person during the review, same as the assignment expects. No screenshot
substitutes for that.
</p>
