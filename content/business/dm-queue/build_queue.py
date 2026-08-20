#!/usr/bin/env python3
"""Render the daily LinkedIn action queue: queue.json -> queue.html.

ponytail: stdlib only, no server, no build step. Open queue.html in a browser.
Checkbox state lives in localStorage keyed by the queue date, so a reload keeps it.

Usage: python3 build_queue.py [queue.json] [queue.html]
"""
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

TEMPLATE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>DM queue {{DATE}}</title>
<style>
:root{--bg:#faf9f7;--fg:#1a1a1a;--dim:#6b6b6b;--line:#e3e0da;--card:#fff;--accent:#1d6b47;--warn:#8a5a00}
@media(prefers-color-scheme:dark){:root{--bg:#16181a;--fg:#e9e7e3;--dim:#9a9a97;--line:#2c2f33;--card:#1e2124;--accent:#4ea87a;--warn:#c99b3a}}
*{box-sizing:border-box}
body{margin:0;padding:24px 16px 80px;background:var(--bg);color:var(--fg);
font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;max-width:820px;margin-inline:auto}
h1{font-size:19px;margin:0 0 2px}
.sub{color:var(--dim);font-size:13px;margin-bottom:20px}
.note{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--warn);
padding:10px 12px;border-radius:6px;font-size:13px;margin-bottom:20px}
.bar{position:sticky;top:0;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--line);
margin-bottom:16px;font-size:13px;color:var(--dim);z-index:5}
.bar b{color:var(--accent);font-size:15px}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--dim);
margin:26px 0 10px;font-weight:600}
ul{list-style:none;padding:0;margin:0}
li{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px 14px;
margin-bottom:10px;display:flex;gap:12px;align-items:flex-start}
li.done{opacity:.42}
input[type=checkbox]{width:19px;height:19px;margin:2px 0 0;flex:none;accent-color:var(--accent);cursor:pointer}
.body{flex:1;min-width:0}
.who{font-weight:600;margin-bottom:2px}
.who a{color:var(--fg)}
.co{font-weight:400;color:var(--dim);font-size:13px}
.ev{font-size:13px;color:var(--dim);margin:4px 0}
.checks{font-size:12px;color:var(--warn);margin:6px 0 0}
.act{font-size:11px;text-transform:uppercase;letter-spacing:.05em;padding:3px 7px;border-radius:4px;
border:1px solid var(--line);color:var(--dim);flex:none;font-weight:600}
.msg{margin-top:9px}
.msg pre{background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:9px 11px;
margin:0 0 6px;white-space:pre-wrap;word-wrap:break-word;font:13px/1.5 inherit}
button{font:600 12px inherit;padding:5px 11px;border-radius:5px;border:1px solid var(--line);
background:var(--card);color:var(--fg);cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
.simple li{display:block}
.simple label{display:flex;gap:11px;align-items:center;cursor:pointer}
#log{width:100%;height:150px;background:var(--card);color:var(--fg);border:1px solid var(--line);
border-radius:6px;padding:10px;font:12px/1.5 ui-monospace,monospace;resize:vertical}
</style></head><body>

<h1>Daily LinkedIn queue</h1>
<div class="sub">{{DATE}} &middot; about 15 minutes &middot; nothing here sends itself</div>
{{NOTE}}
<div class="bar"><b><span id="n">0</span>/{{TOTAL}}</b> done</div>

<h2>Run sheet</h2>
<ul class="simple" id="sheet">
<li><label><input type="checkbox" data-k="s0"><span>Answer 2 questions in r/n8n, r/automation or r/smallbusiness. Whole solution, no pitch, no link.</span></label></li>
<li><label><input type="checkbox" data-k="s1"><span>Leave 3 substantive comments on target posts. Not "great post".</span></label></li>
<li><label><input type="checkbox" data-k="s2"><span>Reply to every accept and every reply from yesterday.</span></label></li>
</ul>

<h2>People</h2>
<ul id="rows">{{ROWS}}</ul>

<h2>End of day</h2>
<textarea id="log" readonly></textarea>
<button id="copylog" style="margin-top:8px">Copy log</button>

<script>
var KEY = 'dmq-{{DATE}}';
var saved = JSON.parse(localStorage.getItem(KEY) || '{}');
var boxes = document.querySelectorAll('input[type=checkbox]');

function render(){
  var done = 0, total = 0, lines = [];
  boxes.forEach(function(b){
    var li = b.closest('li');
    if (b.dataset.name) {
      total++;
      if (b.checked) { done++; lines.push('- ' + b.dataset.act + ': ' + b.dataset.name + ' (' + b.dataset.co + ')'); }
      li.classList.toggle('done', b.checked);
    }
  });
  document.getElementById('n').textContent = done;
  document.getElementById('log').value =
    '## ' + '{{DATE}}' + '\\n' + done + '/' + total + ' actions done\\n' +
    (lines.length ? lines.join('\\n') : '(none)') +
    '\\n\\nAccepts since yesterday: \\nReplies: \\nBooked: ';
}

boxes.forEach(function(b){
  if (saved[b.dataset.k]) b.checked = true;
  b.addEventListener('change', function(){
    saved[b.dataset.k] = b.checked;
    localStorage.setItem(KEY, JSON.stringify(saved));
    render();
  });
});

document.querySelectorAll('.copy').forEach(function(btn){
  btn.addEventListener('click', function(){
    navigator.clipboard.writeText(btn.previousElementSibling.textContent);
    btn.textContent = 'Copied';
    setTimeout(function(){ btn.textContent = 'Copy'; }, 1200);
  });
});

document.getElementById('copylog').addEventListener('click', function(){
  navigator.clipboard.writeText(document.getElementById('log').value);
  this.textContent = 'Copied';
});

render();
</script>
</body></html>
"""

VERIFY = ("Verify on the profile before sending: posted in the last 30 days &middot; "
          "headcount on the company page &middot; no engineer or n8n/Zapier mention")


def row_html(i, r):
    e = html.escape
    name, co = r.get("name", "?"), r.get("company", "")
    head = f"{e(co)} &middot; {e(str(r['headcount']))} people" if r.get("headcount") else e(co)
    msgs = "".join(
        f'<div class="msg"><pre>{e(m)}</pre><button class="copy">Copy</button></div>'
        for m in r.get("messages", [])
    )
    return (
        f'<li><input type="checkbox" data-k="r{i}" data-name="{e(name)}" '
        f'data-co="{e(co)}" data-act="{e(r.get("action", "connect"))}">'
        f'<div class="body">'
        f'<div class="who"><a href="{e(r.get("url", "#"))}" target="_blank" rel="noopener">{e(name)}</a> '
        f'<span class="co">{head}</span></div>'
        f'<div class="ev">{e(r.get("evidence", ""))}</div>'
        f'<div class="checks">{VERIFY}</div>'
        f"{msgs}</div>"
        f'<span class="act">{e(r.get("action", "connect"))}</span></li>'
    )


def main():
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "queue.json"
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "queue.html"
    data = json.loads(src.read_text())
    rows = data.get("rows", [])
    note = f'<div class="note">{html.escape(data["note"])}</div>' if data.get("note") else ""
    out = (TEMPLATE
           .replace("{{ROWS}}", "".join(row_html(i, r) for i, r in enumerate(rows)))
           .replace("{{TOTAL}}", str(len(rows)))
           .replace("{{NOTE}}", note)
           .replace("{{DATE}}", html.escape(data.get("date", ""))))
    dst.write_text(out)
    print(f"{dst}: {len(rows)} rows")


if __name__ == "__main__":
    main()
