---
layout: post
title: SDLC Walkthrough
permalink: /sdlc
search_exclude: true
hide: true
---

<p style="max-width: 700px;">
One real portfolio feature, walked through the six SDLC phases — not a hypothetical, actual
commits: <a href="https://github.com/Wick2009/portfolio/commit/6188668081a13507fea47841a03fcab064fcf92f"><code>6188668</code></a>
(built it) and <a href="https://github.com/Wick2009/portfolio/commit/00b5c2a101a90a7b658b54e22696562105504176"><code>00b5c2a</code></a>
(revised it after review). The revision is the interesting part — most real dev work has one.
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
  public repos/issues) before picking mine. Three people had converged on embedding the class's
  Code Runner into lessons; one (Harrish) had hand-written a static Markdown checklist flagging
  which copied lesson notebooks were still empty placeholders. My first version automated that
  same idea — a script classifying real vs. stub lessons. On review, that got flagged as a
  problem: it only means anything <em>while</em> lessons are unfinished. Once every lesson is
  written, a page whose whole pitch is "here's what's incomplete" has nothing left to say. So the
  actual plan became: keep the part with lasting value (fast search across 61+ lessons,
  progress tracking) and drop the part that expires (the real/stub audit).
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🎨 Design</td>
  <td style="padding:8px;">
  Kept the existing repo pattern — a generated <code>_data/*.yml</code> file consumed by a
  Liquid page, same approach as <code>study-tracker.html</code> and
  <code>exercisegraphs.html</code> — and the same button styling as the rest of the home page.
  Removed the REAL/STUB badges, the stub counts, and the "hide stubs" toggle from the UI; kept
  every lesson checkable regardless of completion status, since progress tracking is useful no
  matter how much content exists yet.
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🛠️ Develop</td>
  <td style="padding:8px;">
  <code>scripts/generate_csa_lesson_index.py</code> still scans
  <code>_notebooks/CSA/ap_mcq_lessons/unit_0[1-4]</code> and groups homework/backup files under
  their lesson number, but the stub classification is no longer surfaced in the UI.
  <code>csa-dashboard.md</code> (<code>/csa/dashboard</code>) is now a plain searchable index of
  every lesson with a persistent progress checkbox. Along the way the audit did catch a real bug —
  the home page's Unit 2/3/4 buttons linked straight to empty lessons — fixed in the same pass.<br>
  Commits: <a href="https://github.com/Wick2009/portfolio/commit/6188668081a13507fea47841a03fcab064fcf92f">6188668</a> →
  <a href="https://github.com/Wick2009/portfolio/commit/00b5c2a101a90a7b658b54e22696562105504176">00b5c2a</a>
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🧪 Test</td>
  <td style="padding:8px;">
  Ran <code>make serve</code> locally after the revision: confirmed the search box still filters
  by number/title, confirmed a lesson checkbox persists in <code>localStorage</code> across a
  full page reload, confirmed the REAL/STUB badges and "hide stubs" control are actually gone
  from the rendered page (not just the source), and confirmed the home page's Unit 1-4 and
  Lesson Index links all still resolve.
  </td>
</tr>
<tr style="border-bottom: 1px solid #444;">
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🚀 Deploy</td>
  <td style="padding:8px;" id="sdlc-deploy-cell">
  Pushed to <code>main</code>; GitHub Actions rebuilt and redeployed the Pages site automatically.
  Runs: <a href="https://github.com/Wick2009/portfolio/actions/runs/32448239770">32448239770</a> (build) →
  <a href="https://github.com/Wick2009/portfolio/actions/runs/32508131230">32508131230</a> (revision)
  </td>
</tr>
<tr>
  <td style="padding:8px; vertical-align:top; font-weight:bold;">🔧 Maintain</td>
  <td style="padding:8px;">
  This row is basically what just happened: got feedback that the stub-audit framing wouldn't
  hold up over time, so I cut it rather than leave dead weight in the UI. The script itself is
  still meant to be re-run as lessons get added —
  <code>python3 scripts/generate_csa_lesson_index.py</code> — the index just no longer treats
  "incomplete" as the interesting fact about a lesson.
  </td>
</tr>
</tbody>
</table>
