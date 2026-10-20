/* ================================================================
   app.js — Ngân Hàng Câu Hỏi Toán Lớp 9 Lạng Sơn
   Vanilla JS, không framework, KaTeX cho toán học
   ================================================================ */

'use strict';

// ── Constants ──────────────────────────────────────────────────
const PAGE_SIZE = 15;

const TOPIC_LABELS = {
  can_thuc:              '√ Căn thức',
  phuong_trinh:          '= Phương trình',
  he_phuong_trinh:       '{ Hệ phương trình',
  ham_so_do_thi:         '∫ Hàm số & Đồ thị',
  bat_dang_thuc_cuc_tri: '≥ BĐT & Cực trị',
  so_hoc_nguyen:         'ℤ Số học & Nguyên',
  toan_thuc_te:          '🚗 Toán thực tế',
};

const TYPE_LABELS = {
  HSG_tinh:      '🏆 HSG Tỉnh',
  Tuyen_sinh_10: '📝 Tuyển sinh 10',
  Hoc_ky:        '📅 Học kỳ',
};

const TYPE_BADGE = {
  HSG_tinh:      'badge-hsg',
  Tuyen_sinh_10: 'badge-ts10',
  Hoc_ky:        'badge-hk',
};

// ── State ──────────────────────────────────────────────────────
const state = {
  all:      [],          // All questions from JSON
  filtered: [],          // After filters
  page:     1,
  sort:     'id_asc',
  search:   '',
  types:    new Set(['HSG_tinh', 'Tuyen_sinh_10', 'Hoc_ky']),
  topics:   new Set(Object.keys(TOPIC_LABELS)),
  diffs:    new Set([1, 2, 3, 4, 5]),
  year:     '',
  idMap:    {},          // id → question object
};

// ── LaTeX → HTML Parser ────────────────────────────────────────
const LP = {
  /**
   * Main converter: LaTeX source → rendered HTML (with KaTeX math)
   */
  convert(src) {
    if (!src) return '';

    // 1. Protect math zones so text-mode converters don't touch them
    const mathDisplay = [];
    const mathInline  = [];

    let s = src
      // \[...\] display math
      .replace(/\\\[([\s\S]*?)\\\]/g, (_, m) => {
        mathDisplay.push(m);
        return `§D${mathDisplay.length - 1}§`;
      })
      // $...$ inline math (non-greedy, no nested $)
      .replace(/\$([^$\n]+?)\$/g, (_, m) => {
        mathInline.push(m);
        return `§I${mathInline.length - 1}§`;
      });

    // 2. Convert LaTeX text-mode commands → HTML
    s = this._textToHtml(s);

    // 3. Restore math with KaTeX rendering
    s = s.replace(/§D(\d+)§/g, (_, i) =>
      this._katexRender(mathDisplay[+i], true)
    );
    s = s.replace(/§I(\d+)§/g, (_, i) =>
      this._katexRender(mathInline[+i], false)
    );

    return s;
  },

  _katexRender(math, display) {
    if (typeof katex === 'undefined') {
      // KaTeX not loaded yet — return raw
      return display ? `\\[${math}\\]` : `$${math}$`;
    }
    try {
      return katex.renderToString(math, {
        throwOnError: false,
        displayMode: display,
        output: 'html',
        trust: true,
        strict: false,
      });
    } catch (e) {
      return display
        ? `<div class="katex-display" style="overflow-x:auto;padding:4px 0">[${math}]</div>`
        : `<span>[${math}]</span>`;
    }
  },

  _textToHtml(s) {
    return s
      /* ── Nested-brace-aware textbf/textit ─────────────────── */
      .replace(/\\textbf\{((?:[^{}]|\{[^{}]*\})*)\}/g, '<strong>$1</strong>')
      .replace(/\\textit\{((?:[^{}]|\{[^{}]*\})*)\}/g, '<em>$1</em>')
      .replace(/\\emph\{((?:[^{}]|\{[^{}]*\})*)\}/g,   '<em>$1</em>')
      .replace(/\\underline\{((?:[^{}]|\{[^{}]*\})*)\}/g, '<u>$1</u>')
      .replace(/\{\\bfseries\s+((?:[^{}]|\{[^{}]*\})*)\}/g, '<strong>$1</strong>')
      .replace(/\{\\itshape\s+((?:[^{}]|\{[^{}]*\})*)\}/g, '<em>$1</em>')

      /* ── Color / font size commands (strip) ───────────────── */
      .replace(/\\color\{[^}]+\}\s*/g, '')
      .replace(/\\textcolor\{[^}]+\}\{([^}]*)\}/g, '$1')
      .replace(/\\(?:large|small|normalsize|footnotesize|tiny|huge|Large|LARGE|Huge)\b\s*/g, '')
      .replace(/\\(?:bfseries|itshape|rmfamily|ttfamily|sffamily)\b\s*/g, '')
      .replace(/\\(?:normalfont|upshape)\b\s*/g, '')

      /* ── Enumerate / itemize ──────────────────────────────── */
      .replace(/\\begin\{enumerate\}(?:\[[^\]]*\])?/g, '<ol class="tex-ol">')
      .replace(/\\end\{enumerate\}/g, '</ol>')
      .replace(/\\begin\{itemize\}/g, '<ul class="tex-ul">')
      .replace(/\\end\{itemize\}/g, '</ul>')
      .replace(/\\item\s*/g, '<li>')

      /* ── Tables (simple conversion) ───────────────────────── */
      .replace(/\\begin\{tabular\}(?:\{[^}]*\})?([\s\S]*?)\\end\{tabular\}/g,
        (_, body) => this._convertTabular(body)
      )

      /* ── center environment ───────────────────────────────── */
      .replace(/\\begin\{center\}([\s\S]*?)\\end\{center\}/g,
        (_, inner) => `<div class="tc">${inner}</div>`
      )

      /* ── Misc symbols ─────────────────────────────────────── */
      .replace(/\\checkmark\b/g, '✓')
      .replace(/\\square\b/g,    '□')
      .replace(/\\ldots\b/g,     '…')
      .replace(/\\cdots\b/g,     '⋯')
      .replace(/\\qed\b/g,       '∎')

      /* ── Spacing / line-break ─────────────────────────────── */
      .replace(/\\\\(?:\[[^\]]*\])?/g, '<br>')
      .replace(/\\newline\b/g, '<br>')
      .replace(/\\noindent\b\s*/g, '')
      .replace(/\\medskip\b/g, '<div style="margin:6px 0"></div>')
      .replace(/\\bigskip\b/g, '<div style="margin:10px 0"></div>')
      .replace(/\\vspace\{[^}]+\}/g, '<div style="margin:4px 0"></div>')
      .replace(/\\hspace\{[^}]+\}/g, '&ensp;')

      /* ── Boxed (text mode) ────────────────────────────────── */
      .replace(/\\boxed\{([^}]*)\}/g, '<span class="boxed">$1</span>')

      /* ── Strip remaining unknown commands ─────────────────── */
      .replace(/\\[a-zA-Z]+\*?\{([^}]*)\}/g, '$1')  // \cmd{arg} → arg
      .replace(/\\[a-zA-Z]+\b\s*/g, '')              // \cmd → ''
      .replace(/\{|\}/g, '')                         // stray braces

      /* ── Paragraph breaks ─────────────────────────────────── */
      .replace(/\n{2,}/g, '</p><p>')
      .replace(/\n/g, ' ')

      /* ── Wrap ─────────────────────────────────────────────── */
      .trim();
  },

  _convertTabular(body) {
    const rows = body.split(/\\\\/);
    const html = rows.map(row => {
      if (!row.trim()) return '';
      const cells = row.split('&').map(c => `<td>${c.trim()}</td>`).join('');
      return `<tr>${cells}</tr>`;
    }).filter(Boolean).join('');
    return html
      ? `<table class="tex-table" style="border-collapse:collapse;margin:6px auto;font-size:13.5px">${html}</table>`
      : '';
  },
};

// ── Utility ────────────────────────────────────────────────────
function diffStars(d) {
  return Array.from({length: 5}, (_, i) =>
    `<span class="${i < d ? 'star-filled' : 'star-empty'}">★</span>`
  ).join('');
}

function typeBadge(type) {
  return `<span class="badge ${TYPE_BADGE[type] || ''}">${TYPE_LABELS[type] || type}</span>`;
}

function topicTags(topics) {
  return topics.map(t =>
    `<span class="topic-tag tag-${t}">${TOPIC_LABELS[t] || t}</span>`
  ).join('');
}

function highlightSearch(html, term) {
  if (!term || term.length < 2) return html;
  try {
    const re = new RegExp(`(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return html.replace(re, '<mark style="background:#fef08a;border-radius:2px">$1</mark>');
  } catch { return html; }
}

// ── Filter & Sort ──────────────────────────────────────────────
function applyFilters() {
  const term = state.search.toLowerCase();

  state.filtered = state.all.filter(q => {
    // Type filter
    if (!state.types.has(q.exam_type)) return false;
    // Topic filter (question must share at least one selected topic)
    if (!q.topics.some(t => state.topics.has(t))) return false;
    // Difficulty filter
    if (!state.diffs.has(q.difficulty)) return false;
    // Year filter
    if (state.year && q.nam_hoc !== state.year) return false;
    // Search
    if (term) {
      const haystack = (
        q.statement_latex + ' ' +
        q.solution_latex + ' ' +
        q.key_techniques.join(' ') + ' ' +
        q.topics.join(' ')
      ).toLowerCase();
      if (!haystack.includes(term)) return false;
    }
    return true;
  });

  // Sort
  const [field, dir] = state.sort.split('_');
  state.filtered.sort((a, b) => {
    let va, vb;
    if (field === 'diff')  { va = a.difficulty; vb = b.difficulty; }
    else if (field === 'score') { va = a.diem; vb = b.diem; }
    else if (field === 'year')  { va = a.nam_hoc; vb = b.nam_hoc; }
    else                        { va = a.id; vb = b.id; }
    if (va < vb) return dir === 'asc' ? -1 : 1;
    if (va > vb) return dir === 'asc' ?  1 : -1;
    return 0;
  });

  state.page = 1;
  render();
}

// ── Render ─────────────────────────────────────────────────────
function render() {
  updateStats();
  renderList();
  renderPagination();
  renderActiveFilters();
}

function updateStats() {
  const total = state.all.length;
  const shown = state.filtered.length;
  document.getElementById('stat-total').textContent = total;
  document.getElementById('result-count').innerHTML =
    `Hiển thị <strong>${shown}</strong> / ${total} câu hỏi`;

  // Update sidebar counts
  const hsg = state.all.filter(q => q.exam_type === 'HSG_tinh').length;
  const ts  = state.all.filter(q => q.exam_type === 'Tuyen_sinh_10').length;
  const hk  = state.all.filter(q => q.exam_type === 'Hoc_ky').length;
  document.getElementById('cnt-hsg').textContent = hsg;
  document.getElementById('cnt-ts').textContent  = ts;
  document.getElementById('cnt-hk').textContent  = hk;

  // Topic counts
  const topicCounts = {};
  state.all.forEach(q => q.topics.forEach(t => {
    topicCounts[t] = (topicCounts[t] || 0) + 1;
  }));
  document.querySelectorAll('#filter-topic .check-item').forEach(el => {
    const val = el.querySelector('input').value;
    el.querySelector('.count').textContent = topicCounts[val] || 0;
  });
}

function renderList() {
  const list   = document.getElementById('questions-list');
  const empty  = document.getElementById('empty-state');
  const paged  = state.filtered.slice(
    (state.page - 1) * PAGE_SIZE,
    state.page * PAGE_SIZE
  );

  if (state.filtered.length === 0) {
    list.innerHTML = '';
    empty.style.display = 'flex';
    return;
  }
  empty.style.display = 'none';

  list.innerHTML = paged.map(q => buildCard(q)).join('');

  // Attach events to new cards
  list.querySelectorAll('.btn-toggle-sol').forEach(btn => {
    btn.addEventListener('click', () => {
      const id  = btn.dataset.id;
      const sol = document.getElementById(`sol-${id}`);
      const isOpen = sol.classList.toggle('show');
      btn.classList.toggle('open', isOpen);
      btn.innerHTML = isOpen
        ? '▲ Ẩn lời giải'
        : '▼ Xem lời giải';
    });
  });

  list.querySelectorAll('.btn-similar').forEach(btn => {
    btn.addEventListener('click', () => {
      const id  = btn.dataset.id;
      const box = document.getElementById(`sim-${id}`);
      box.classList.toggle('show');
    });
  });

  list.querySelectorAll('.sim-chip').forEach(chip => {
    chip.addEventListener('click', () => {
      const targetId = chip.dataset.target;
      scrollToQuestion(targetId);
    });
  });
}

function buildCard(q) {
  const stmtHtml = LP.convert(q.statement_latex);
  const solHtml  = LP.convert(q.solution_latex);
  const searched = state.search.length >= 2
    ? highlightSearch(stmtHtml, state.search)
    : stmtHtml;

  const simChips = q.similar_ids.length
    ? q.similar_ids.map(sid =>
        `<span class="sim-chip" data-target="${sid}">${sid}</span>`
      ).join('')
    : '<span style="color:#9ca3af;font-size:13px">Không có bài tương tự</span>';

  const hasSub = q.sub_parts.length > 0;
  const partLabel = hasSub
    ? `<span style="font-size:11.5px;color:#6b7280;margin-left:4px">(${q.sub_parts.join(', ')})</span>`
    : '';

  return `
<article class="q-card" id="card-${q.id}">
  <div class="q-card-head">
    <span class="q-id-badge">${q.id}</span>
    <div class="q-meta">
      ${typeBadge(q.exam_type)}
      <span class="badge badge-year">📅 ${q.nam_hoc}</span>
      <span class="badge badge-score">💯 ${q.diem} điểm</span>
      ${partLabel}
    </div>
    <div class="q-right">
      <span class="diff-stars" title="Độ khó ${q.difficulty}/5">
        ${diffStars(q.difficulty)}
      </span>
    </div>
  </div>

  <div class="q-topics">
    ${topicTags(q.topics)}
    ${q.key_techniques.slice(0, 3).map(t =>
      `<span style="font-size:11px;color:#6b7280;background:#f9fafb;
        border:1px solid #e5e7eb;border-radius:3px;padding:2px 7px;"
      >${t.replace(/_/g,' ')}</span>`
    ).join('')}
  </div>

  <div class="q-statement">${searched}</div>

  <div class="q-actions">
    <button class="btn-toggle-sol" data-id="${q.id}">
      ▼ Xem lời giải
    </button>
    <button class="btn-similar" data-id="${q.id}">
      🔗 ${q.similar_ids.length} bài tương tự
    </button>
  </div>

  <div class="q-solution" id="sol-${q.id}">
    <div class="sol-label">
      <span>▷</span>
      <span>LỜI GIẢI &amp; ĐÁP ÁN</span>
    </div>
    <div class="content">${solHtml}</div>
  </div>

  <div class="q-similar" id="sim-${q.id}">
    <div class="similar-label">📎 Bài tập tương tự (từ đề khác):</div>
    <div class="similar-chips">${simChips}</div>
  </div>
</article>`;
}

// ── Pagination ─────────────────────────────────────────────────
function renderPagination() {
  const total    = state.filtered.length;
  const pages    = Math.ceil(total / PAGE_SIZE);
  const cur      = state.page;
  const pag      = document.getElementById('pagination');

  if (pages <= 1) { pag.innerHTML = ''; return; }

  let html = `
    <button class="page-btn" ${cur === 1 ? 'disabled' : ''}
      onclick="goPage(${cur - 1})">‹ Trước</button>`;

  const range = buildPageRange(cur, pages);
  range.forEach(p => {
    if (p === '…') {
      html += `<span class="page-ellipsis">…</span>`;
    } else {
      html += `<button class="page-btn ${p === cur ? 'active' : ''}"
        onclick="goPage(${p})">${p}</button>`;
    }
  });

  html += `<button class="page-btn" ${cur === pages ? 'disabled' : ''}
    onclick="goPage(${cur + 1})">Sau ›</button>`;

  pag.innerHTML = html;
}

function buildPageRange(cur, total) {
  if (total <= 7) return Array.from({length: total}, (_, i) => i + 1);
  const pages = [];
  pages.push(1);
  if (cur > 3) pages.push('…');
  for (let p = Math.max(2, cur - 1); p <= Math.min(total - 1, cur + 1); p++) {
    pages.push(p);
  }
  if (cur < total - 2) pages.push('…');
  pages.push(total);
  return pages;
}

window.goPage = function(p) {
  state.page = p;
  renderList();
  renderPagination();
  document.getElementById('main').scrollIntoView({behavior: 'smooth', block: 'start'});
};

// ── Active filters display ──────────────────────────────────────
function renderActiveFilters() {
  const el = document.getElementById('active-filters');
  const tags = [];

  if (state.search) {
    tags.push(`<span class="filter-tag">
      🔍 "${state.search}"
      <button onclick="clearSearch()">×</button>
    </span>`);
  }
  if (state.year) {
    tags.push(`<span class="filter-tag">
      📅 ${state.year}
      <button onclick="clearYear()">×</button>
    </span>`);
  }
  if (state.types.size < 3) {
    [...state.types].forEach(t => {
      tags.push(`<span class="filter-tag">${TYPE_LABELS[t]}</span>`);
    });
  }

  el.innerHTML = tags.join('');
}

window.clearSearch = function() {
  document.getElementById('search-input').value = '';
  state.search = '';
  applyFilters();
};
window.clearYear = function() {
  document.getElementById('year-select').value = '';
  state.year = '';
  applyFilters();
};

// ── Scroll to question ──────────────────────────────────────────
function scrollToQuestion(id) {
  // Check if on current page
  const card = document.getElementById(`card-${id}`);
  if (card) {
    card.scrollIntoView({behavior: 'smooth', block: 'center'});
    card.style.outline = '3px solid #1e64b4';
    setTimeout(() => { card.style.outline = ''; }, 2000);
    return;
  }
  // Find which page it's on
  const idx = state.filtered.findIndex(q => q.id === id);
  if (idx === -1) {
    // Not in current filter set — clear filters and search
    const q = state.idMap[id];
    if (!q) return;
    state.search = '';
    state.types  = new Set(['HSG_tinh', 'Tuyen_sinh_10', 'Hoc_ky']);
    state.topics = new Set(Object.keys(TOPIC_LABELS));
    state.diffs  = new Set([1, 2, 3, 4, 5]);
    state.year   = '';
    resetCheckboxes();
    applyFilters();
    setTimeout(() => scrollToQuestion(id), 300);
    return;
  }
  goPage(Math.floor(idx / PAGE_SIZE) + 1);
  setTimeout(() => {
    const c = document.getElementById(`card-${id}`);
    if (c) {
      c.scrollIntoView({behavior: 'smooth', block: 'center'});
      c.style.outline = '3px solid #1e64b4';
      setTimeout(() => { c.style.outline = ''; }, 2000);
    }
  }, 200);
}

// ── Year select population ─────────────────────────────────────
function populateYears() {
  const years = [...new Set(state.all.map(q => q.nam_hoc))].sort().reverse();
  const sel   = document.getElementById('year-select');
  years.forEach(y => {
    const opt = document.createElement('option');
    opt.value = y;
    opt.textContent = `Năm ${y}`;
    sel.appendChild(opt);
  });
}

// ── Bind events ────────────────────────────────────────────────
function bindEvents() {
  // Search
  let searchTimer;
  document.getElementById('search-input').addEventListener('input', e => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(() => {
      state.search = e.target.value.trim();
      applyFilters();
    }, 300);
  });

  // Sort
  document.getElementById('sort-select').addEventListener('change', e => {
    state.sort = e.target.value;
    applyFilters();
  });

  // Year
  document.getElementById('year-select').addEventListener('change', e => {
    state.year = e.target.value;
    applyFilters();
  });

  // Type checkboxes
  document.querySelectorAll('#filter-type input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', () => {
      state.types = new Set(
        [...document.querySelectorAll('#filter-type input:checked')].map(c => c.value)
      );
      applyFilters();
    });
  });

  // Topic checkboxes
  document.querySelectorAll('#filter-topic input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', () => {
      state.topics = new Set(
        [...document.querySelectorAll('#filter-topic input:checked')].map(c => c.value)
      );
      applyFilters();
    });
  });

  // Difficulty checkboxes
  document.querySelectorAll('#filter-diff input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', () => {
      state.diffs = new Set(
        [...document.querySelectorAll('#filter-diff input:checked')].map(c => +c.value)
      );
      applyFilters();
    });
  });

  // Reset
  document.getElementById('btn-reset').addEventListener('click', () => {
    document.getElementById('search-input').value = '';
    document.getElementById('year-select').value  = '';
    state.search = '';
    state.year   = '';
    state.types  = new Set(['HSG_tinh', 'Tuyen_sinh_10', 'Hoc_ky']);
    state.topics = new Set(Object.keys(TOPIC_LABELS));
    state.diffs  = new Set([1, 2, 3, 4, 5]);
    resetCheckboxes();
    applyFilters();
  });
}

function resetCheckboxes() {
  document.querySelectorAll('#filter-type input, #filter-topic input, #filter-diff input')
    .forEach(cb => { cb.checked = true; });
}

// ── Bootstrap ──────────────────────────────────────────────────
async function init() {
  try {
    const res  = await fetch('questions.json');
    const data = await res.json();

    state.all = data.questions;
    state.idMap = Object.fromEntries(state.all.map(q => [q.id, q]));

    populateYears();
    bindEvents();
    applyFilters();

    document.getElementById('loading').style.display = 'none';
  } catch (err) {
    document.getElementById('loading').innerHTML = `
      <div style="font-size:18px">⚠️ Không thể tải dữ liệu</div>
      <div style="font-size:13px;opacity:.8;max-width:400px;text-align:center">
        Hãy mở trang bằng <strong>Python server</strong>:<br><br>
        <code style="background:rgba(255,255,255,.15);padding:6px 12px;border-radius:4px">
          python serve.py
        </code><br><br>
        Sau đó truy cập <a href="http://localhost:8000" style="color:#93c5fd">
          http://localhost:8000
        </a>
      </div>
      <div style="font-size:12px;opacity:.5;margin-top:16px">Lỗi: ${err.message}</div>
    `;
  }
}

// Chờ KaTeX tải xong rồi mới init
window.addEventListener('load', init);
