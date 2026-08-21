---
layout: post
title: SDLC Walkthrough
permalink: /sdlc
search_exclude: true
hide: true
---

<p style="max-width: 700px;">
One real portfolio change, walked through the six SDLC phases — not a hypothetical, an
actual commit: <a href="https://github.com/Wick2009/portfolio/commit/6188668081a13507fea47841a03fcab064fcf92f"><code>6188668</code></a>,
"Add CSA lesson dashboard, fix stub links on home page."
</p>

<table style="width:100%; max-width: 800px; border-collapse: collapse;">
<thead>
<tr style="text-align:left; border-bottom: 2px solid #888;">
  <th style="padding:8px;">Phase</th>
  <th style="padding:8px;">What I did</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🧭 Plan</td>
  <td style="padding:8px;">
  For the Unit 1-4 "unicorn" ask, I checked what other students had already built (via their
  public repos/issues) before picking mine, so it wouldn't overlap. Three people had converged
  on embedding the class's Code Runner into lessons; one (Harrish) had hand-written a static
  Markdown checklist flagging which copied lesson notebooks were empty placeholder "stubs" vs.
  fully written. I decided to build the same kind of structural audit — but automated: a script
  that classifies real vs. stub from notebook cell counts (not lesson content), plus a live,
  searchable dashboard page instead of a file you open in VS Code.
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🎨 Design</td>
  <td style="padding:8px;">
  Before writing code, I validated the classification rule against real files: every lesson I
  checked was either exactly 1 cell (front matter only, &lt;200 chars — a stub) or several
  cells with real content. Clean signal, no fuzzy threshold needed. For output, I reused this
  repo's existing pattern — a generated <code>_data/*.yml</code> file consumed by a Liquid
  page — the same approach already used by <code>study-tracker.html</code> and
  <code>exercisegraphs.html</code>. Styling matches the home page's existing button rows
  (same <code>var(--green/blue/warn/orange/teal)</code> palette).
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🛠️ Develop</td>
  <td style="padding:8px;">
  Built <code>scripts/generate_csa_lesson_index.py</code> (scans <code>_notebooks/CSA/ap_mcq_lessons/unit_0[1-4]</code>,
  groups homework/backup files under their lesson number, writes <code>_data/csa_units.yml</code>),
  <code>csa-dashboard.md</code> (the <code>/csa/dashboard</code> page — search box, hide-stubs
  toggle, per-lesson progress checkboxes), and fixed the home page's Unit 2/3/4 buttons, which
  the audit revealed were linking straight to empty stub lessons.<br>
  Commit: <a href="https://github.com/Wick2009/portfolio/commit/6188668081a13507fea47841a03fcab064fcf92f">6188668</a>
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🧪 Test</td>
  <td style="padding:8px;">
  Ran <code>make serve</code> locally and tested in-browser: confirmed the summary counts
  (31 real / 17 stub across units 1-4) match a manual spot check, confirmed the search box
  filters rows by number/title, confirmed "hide stubs" toggles correctly, checked off a lesson
  and confirmed it persisted in <code>localStorage</code> across a full page reload, and
  clicked through a "real"-flagged link (Unit 2 → 2.3) to confirm it loads actual lesson
  content rather than a stub.
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🚀 Deploy</td>
  <td style="padding:8px;" id="sdlc-deploy-cell">
  Pushed to <code>main</code>; GitHub Actions rebuilt and redeployed the Pages site automatically.
  Run: <a href="https://github.com/Wick2009/portfolio/actions/runs/32448239770">32448239770</a>
  </td>
</tr>
<tr>
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🔧 Maintain</td>
  <td style="padding:8px;">
  The script is meant to be re-run, not one-off — any time a stub lesson gets filled in or new
  lessons are added, <code>python3 scripts/generate_csa_lesson_index.py</code> regenerates the
  data and the dashboard updates itself. Next improvement: wire that regeneration into
  <code>make serve</code>/<code>make build</code> automatically instead of running it by hand.
  </td>
</tr>
</tbody>
</table>
