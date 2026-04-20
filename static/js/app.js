/* ── Japanese N4 Reader ──────────────────────────────────────────────────── */

// ── State ─────────────────────────────────────────────────────────────────
let kanjiDB = {};          // loaded once at startup
let wordTooltipTimer = null;
let activeLevel = 'n4';
let tooltipPinned = false; // true while cursor is inside the tooltip

const KANJI_RE = /[\u4e00-\u9faf\u3400-\u4dbf]/;

// ── DOM refs ──────────────────────────────────────────────────────────────
const tooltip           = document.getElementById('tooltip');
const kanjiModal        = document.getElementById('kanjiModal');
const modalClose        = document.getElementById('modalClose');
const furiganaToggle    = document.getElementById('furiganaToggle');
const translationToggle = document.getElementById('translationToggle');
const levelTabs         = document.querySelectorAll('.level-tab');

// ── Furigana toggle ───────────────────────────────────────────────────────
furiganaToggle.addEventListener('change', () => {
  document.body.classList.toggle('hide-furigana', !furiganaToggle.checked);
});

// ── Translation toggle ────────────────────────────────────────────────────
translationToggle.addEventListener('change', () => {
  document.body.classList.toggle('show-translations', translationToggle.checked);
});

// ── Level tabs ────────────────────────────────────────────────────────────
levelTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    const level = tab.dataset.level;
    if (level === activeLevel) return;
    activeLevel = level;
    levelTabs.forEach(t => t.classList.toggle('active', t.dataset.level === level));
    loadPassage(level);
  });
});

// ── Tooltip positioning helper ────────────────────────────────────────────
function positionEl(el, e) {
  if (window.innerWidth <= 768) return; // CSS handles it as a bottom sheet
  const pad = 14;
  const tw  = el.offsetWidth  || 280;
  const th  = el.offsetHeight || 120;
  const vw  = window.innerWidth;
  const vh  = window.innerHeight;

  let x = e.clientX + pad;
  let y = e.clientY - th / 2;

  if (x + tw > vw - pad) x = e.clientX - tw - pad;
  if (y < pad)            y = pad;
  if (y + th > vh - pad)  y = vh - th - pad;

  el.style.left = x + 'px';
  el.style.top  = y + 'px';
}

// ── Word/grammar/particle tooltip ────────────────────────────────────────
function showWordTooltip(e, tok) {
  clearTimeout(wordTooltipTimer);

  tooltip.className = 'tooltip type-' + tok.type;

  tooltip.querySelector('.tooltip-word').textContent    = tok.text;
  tooltip.querySelector('.tooltip-reading').textContent =
    tok.reading && tok.reading !== tok.text ? '【' + tok.reading + '】' : '';

  const badgeLabels = { word: 'VOCAB', grammar: 'GRAMMAR', particle: 'PARTICLE', name: 'NAME' };
  const levelStr = tok.level ? ' · ' + tok.level : '';
  tooltip.querySelector('.tooltip-badge').textContent =
    (badgeLabels[tok.type] || tok.type.toUpperCase()) + levelStr;

  tooltip.querySelector('.tooltip-meaning').textContent =
    tok.meaning || tok.explanation || '';

  // ── Kanji breakdown (for vocabulary words) ─────────────────────────────
  const kbDiv  = tooltip.querySelector('.tooltip-kanji-breakdown');
  const kbList = tooltip.querySelector('.ttk-list');
  kbList.innerHTML = '';

  if (tok.type === 'word' || tok.type === 'name') {
    const kanjiChars = [...tok.text].filter(c => KANJI_RE.test(c));
    if (kanjiChars.length > 0) {
      kanjiChars.forEach(ch => {
        const info = kanjiDB[ch];
        if (!info) return;
        const row = document.createElement('div');
        row.className = 'ttk-row';

        const charEl = document.createElement('span');
        charEl.className = 'ttk-char';
        charEl.textContent = ch;

        const readEl = document.createElement('span');
        readEl.className = 'ttk-readings';
        const ons  = info.on  ? info.on.join('、') : '';
        const kuns = info.kun ? info.kun.join('、') : '';
        readEl.textContent = [ons, kuns].filter(Boolean).join(' / ');

        const meaningEl = document.createElement('span');
        meaningEl.className = 'ttk-meaning';
        meaningEl.textContent = (info.meanings || []).slice(0, 2).join(', ');

        const lvlEl = document.createElement('span');
        lvlEl.className = 'ttk-level';
        lvlEl.textContent = info.level || '';

        row.appendChild(charEl);
        row.appendChild(readEl);
        row.appendChild(meaningEl);
        row.appendChild(lvlEl);
        kbList.appendChild(row);
      });
      kbDiv.classList.remove('hidden');
    } else {
      kbDiv.classList.add('hidden');
    }
  } else {
    kbDiv.classList.add('hidden');
  }

  // ── Grammar extra section ──────────────────────────────────────────────
  const extra = tooltip.querySelector('.tooltip-extra');
  if (tok.type === 'grammar' && (tok.pattern || tok.explanation)) {
    extra.classList.remove('hidden');

    const patEl = tooltip.querySelector('.tooltip-pattern');
    if (tok.pattern) { patEl.textContent = tok.pattern; patEl.classList.remove('hidden'); }
    else             { patEl.classList.add('hidden'); }

    const explEl = tooltip.querySelector('.tooltip-explanation');
    if (tok.explanation) { explEl.textContent = tok.explanation; explEl.classList.remove('hidden'); }
    else                 { explEl.classList.add('hidden'); }

    const exEl = tooltip.querySelector('.tooltip-example');
    if (tok.example_jp) {
      tooltip.querySelector('.tooltip-example-jp').textContent = tok.example_jp;
      tooltip.querySelector('.tooltip-example-en').textContent = tok.example_en || '';
      exEl.classList.remove('hidden');
    } else {
      exEl.classList.add('hidden');
    }
  } else if (tok.type === 'particle' && tok.meaning) {
    extra.classList.remove('hidden');
    tooltip.querySelector('.tooltip-pattern').classList.add('hidden');
    tooltip.querySelector('.tooltip-explanation').textContent = tok.meaning;
    tooltip.querySelector('.tooltip-explanation').classList.remove('hidden');
    tooltip.querySelector('.tooltip-example').classList.add('hidden');
  } else {
    extra.classList.add('hidden');
  }

  // Notes
  const notesEl = tooltip.querySelector('.tooltip-notes');
  if (tok.notes) { notesEl.textContent = tok.notes; notesEl.classList.remove('hidden'); }
  else           { notesEl.classList.add('hidden'); }

  positionEl(tooltip, e);
  tooltip.classList.remove('hidden');
}

function hideWordTooltip() {
  wordTooltipTimer = setTimeout(() => tooltip.classList.add('hidden'), 120);
}

// ── Kanji detail modal ────────────────────────────────────────────────────
function openKanjiModal(ch) {
  const info = kanjiDB[ch];
  if (!info) return;

  document.getElementById('modalChar').textContent     = ch;
  document.getElementById('modalLevel').innerHTML      = `<span>${info.level || 'N/A'}</span>`;
  document.getElementById('modalMeanings').textContent = (info.meanings || []).join(' · ');
  document.getElementById('modalOn').textContent       = (info.on  || []).join('、') || '—';
  document.getElementById('modalKun').textContent      = (info.kun || []).join('、') || '—';
  document.getElementById('modalStrokes').textContent  =
    info.stroke_count ? `Stroke count: ${info.stroke_count}` : '';

  const exContainer = document.getElementById('modalExamples');
  exContainer.innerHTML = '';
  (info.examples || []).forEach(ex => {
    const row = document.createElement('div');
    row.className = 'modal-example-row';
    row.innerHTML = `
      <span class="mex-word">${escHtml(ex.word)}</span>
      <span class="mex-reading">${escHtml(ex.reading)}</span>
      <span class="mex-meaning">${escHtml(ex.meaning)}</span>
    `;
    exContainer.appendChild(row);
  });

  kanjiModal.classList.remove('hidden');
}

function closeKanjiModal() { kanjiModal.classList.add('hidden'); }

modalClose.addEventListener('click', closeKanjiModal);
kanjiModal.addEventListener('click', e => { if (e.target === kanjiModal) closeKanjiModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeKanjiModal(); });

// ── Sidebar toggle (mobile) ───────────────────────────────────────────────
const sidebarToggle = document.getElementById('sidebarToggle');
const sidebar       = document.getElementById('sidebar');
if (sidebarToggle) {
  sidebarToggle.addEventListener('click', () => sidebar.classList.toggle('open'));
}

// ── Tooltip close button (mobile) ─────────────────────────────────────────
const tooltipClose = document.getElementById('tooltipClose');
if (tooltipClose) {
  tooltipClose.addEventListener('click', e => {
    e.stopPropagation();
    tooltip.classList.add('hidden');
  });
}

// ── Dismiss tooltip on tap outside (mobile) ───────────────────────────────
document.addEventListener('click', e => {
  if (window.innerWidth > 768) return;
  if (!tooltip.classList.contains('hidden') &&
      !tooltip.contains(e.target) &&
      !e.target.closest('.token')) {
    tooltip.classList.add('hidden');
  }
});

// ── Render kanji characters inside token text ─────────────────────────────
// Each kanji gets a .k-char span; clicking opens the full kanji modal.
// No hover card — hovering over a token always shows the word tooltip.
function renderKanjiChars(text) {
  const frag = document.createDocumentFragment();
  for (const ch of text) {
    if (KANJI_RE.test(ch)) {
      const span = document.createElement('span');
      span.className = 'k-char';
      span.textContent = ch;
      span.dataset.kanji = ch;

      if (kanjiDB[ch]) {
        span.addEventListener('click', e => { e.stopPropagation(); openKanjiModal(ch); });
      }
      frag.appendChild(span);
    } else {
      frag.appendChild(document.createTextNode(ch));
    }
  }
  return frag;
}

// ── Build a ruby element: text with reading on top ────────────────────────
function makeRuby(text, reading) {
  const hasKanji = [...text].some(c => KANJI_RE.test(c));
  if (!hasKanji || !reading || reading === text) {
    return null;
  }
  const ruby = document.createElement('ruby');
  ruby.appendChild(renderKanjiChars(text));
  const rt = document.createElement('rt');
  rt.textContent = reading;
  ruby.appendChild(rt);
  return ruby;
}

// ── Render one token span ─────────────────────────────────────────────────
function renderToken(tok) {
  if (tok.type === 'plain') {
    return document.createTextNode(tok.text);
  }

  const span = document.createElement('span');
  span.className = 'token ' + tok.type;

  const ruby = makeRuby(tok.text, tok.reading);
  if (ruby) {
    span.appendChild(ruby);
  } else {
    span.appendChild(renderKanjiChars(tok.text));
  }

  // Word tooltip fires on any part of the token (including k-char children)
  span.addEventListener('mousemove', e => showWordTooltip(e, tok));
  span.addEventListener('mouseleave', hideWordTooltip);

  // Tap-to-show on mobile
  span.addEventListener('click', e => {
    if (window.innerWidth <= 768) {
      e.stopPropagation();
      showWordTooltip(e, tok);
    }
  });

  return span;
}

// ── Render passage ────────────────────────────────────────────────────────
function renderPassage(passage) {
  document.getElementById('passageHeader').innerHTML = `
    <div class="passage-title">${passage.title}</div>
    <div class="passage-title-reading">${passage.title_reading}</div>
    <div class="passage-title-meaning">${passage.title_meaning}</div>
    <p class="passage-description">${passage.description}</p>
  `;

  const body = document.getElementById('passageBody');
  body.innerHTML = '';

  for (const seg of passage.segments) {
    const segDiv = document.createElement('div');
    segDiv.className = 'segment';
    segDiv.id = seg.id;

    if (seg.section) {
      const h = document.createElement('div');
      h.className = 'section-heading';
      h.textContent = seg.section;
      segDiv.appendChild(h);
    }

    const line = document.createElement('div');
    line.className = 'segment-text';
    for (const tok of seg.tokens) line.appendChild(renderToken(tok));
    segDiv.appendChild(line);

    if (seg.translation) {
      const transDiv = document.createElement('div');
      transDiv.className = 'segment-translation';
      transDiv.textContent = seg.translation;
      segDiv.appendChild(transDiv);
    }

    body.appendChild(segDiv);
  }
}

// ── Render grammar sidebar ────────────────────────────────────────────────
function renderGrammarList(patterns) {
  const list = document.getElementById('grammarList');
  list.innerHTML = '';
  for (const p of patterns) {
    const item = document.createElement('div');
    item.className = 'grammar-item';
    item.innerHTML = `
      <div class="gi-pattern">${escHtml(p.pattern)}</div>
      <div class="gi-meaning">${escHtml(p.meaning)}</div>
    `;
    list.appendChild(item);
  }
}

// ── Tooltip interactivity — stay open and still when hovered ─────────────
tooltip.addEventListener('mouseenter', () => {
  tooltipPinned = true;
  clearTimeout(wordTooltipTimer);
});
tooltip.addEventListener('mouseleave', () => {
  tooltipPinned = false;
  hideWordTooltip();
});

// ── Reposition tooltip on mouse move (skip while cursor is inside it) ─────
document.addEventListener('mousemove', e => {
  if (!tooltipPinned && !tooltip.classList.contains('hidden')) positionEl(tooltip, e);
});

// ── Helpers ───────────────────────────────────────────────────────────────
function escHtml(str) {
  return (str || '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

// ── Load a passage level ──────────────────────────────────────────────────
async function loadPassage(level) {
  const body = document.getElementById('passageBody');
  body.innerHTML = '<div class="loading">Loading passage…</div>';
  try {
    const res = await fetch('japanese/api/passage/' + level);
    const passage = await res.json();
    renderPassage(passage);
    renderGrammarList(passage.grammar_index || []);
  } catch (err) {
    body.innerHTML = `<p style="color:red">Failed to load: ${err.message}</p>`;
  }
}

// ── Boot ──────────────────────────────────────────────────────────────────
async function init() {
  try {
    const kanjiRes = await fetch('japanese/api/kanji');
    kanjiDB = await kanjiRes.json();
    await loadPassage('n4');
  } catch (err) {
    document.getElementById('passageBody').innerHTML =
      `<p style="color:red">Failed to load: ${err.message}</p>`;
  }
}

init();
