/* =========================================================
   教育時事アーカイブ — フロントエンド
   data/news.json を読み込み、日付ごとにグループ化して描画する。
   HTML は書き換えられず、データだけが毎朝更新される設計。

   セキュリティ方針:
   ニュース本文は外部由来のデータなので、描画は必ず textContent を使い、
   innerHTML には決して渡さない。リンクは http/https のみ許可する。
   ========================================================= */
(function () {
  'use strict';

  var DATA_URL = 'data/news.json';

  var state = {
    entries: [],
    categories: [],
    catLabels: {},
    filters: { q: '', month: '', cats: [] },
    sort: 'date-desc'
  };

  var el = {
    lastUpdated: document.getElementById('last-updated'),
    entryCount:  document.getElementById('entry-count'),
    generator:   document.getElementById('footer-generator'),
    q:           document.getElementById('q'),
    month:       document.getElementById('month'),
    sort:        document.getElementById('sort'),
    chips:       document.getElementById('category-chips'),
    resultCount: document.getElementById('result-count'),
    reset:       document.getElementById('reset'),
    loading:     document.getElementById('loading'),
    error:       document.getElementById('error'),
    empty:       document.getElementById('empty'),
    noresult:    document.getElementById('noresult'),
    archive:     document.getElementById('archive'),
    tpl:         document.getElementById('tpl-entry')
  };

  /* ---------- helpers ---------- */

  function show(node, visible) {
    if (node) { node.hidden = !visible; }
  }

  function isSafeUrl(url) {
    if (typeof url !== 'string') { return false; }
    try {
      var u = new URL(url, window.location.href);
      return u.protocol === 'http:' || u.protocol === 'https:';
    } catch (e) {
      return false;
    }
  }

  // "2026-09-10" -> "2026年9月10日（木）"
  function formatDate(iso) {
    var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(String(iso || ''));
    if (!m) { return String(iso || ''); }
    var y = Number(m[1]), mo = Number(m[2]), d = Number(m[3]);
    var days = ['日', '月', '火', '水', '木', '金', '土'];
    var wd = new Date(Date.UTC(y, mo - 1, d)).getUTCDay();
    return y + '年' + mo + '月' + d + '日（' + days[wd] + '）';
  }

  function formatMonth(ym) {
    var m = /^(\d{4})-(\d{2})$/.exec(String(ym || ''));
    return m ? Number(m[1]) + '年' + Number(m[2]) + '月' : String(ym || '');
  }

  function monthOf(entry) {
    return String(entry.collected_date || '').slice(0, 7);
  }

  function normalize(s) {
    return String(s == null ? '' : s).toLowerCase();
  }

  function searchBlob(entry) {
    if (entry.__blob) { return entry.__blob; }
    var parts = [
      entry.title, entry.one_line, entry.what_happened,
      entry.why_important, entry.question
    ];
    (entry.categories || []).forEach(function (c) {
      parts.push(c, state.catLabels[c] || '');
    });
    (entry.sources || []).forEach(function (s) {
      parts.push(s.title, s.publisher);
    });
    entry.__blob = normalize(parts.join(' '));
    return entry.__blob;
  }

  /* ---------- filtering ---------- */

  function matches(entry) {
    var f = state.filters;

    if (f.month && monthOf(entry) !== f.month) { return false; }

    if (f.cats.length) {
      var cats = entry.categories || [];
      var hit = f.cats.some(function (c) { return cats.indexOf(c) !== -1; });
      if (!hit) { return false; }
    }

    if (f.q) {
      var blob = searchBlob(entry);
      var terms = f.q.split(/\s+/).filter(Boolean);
      for (var i = 0; i < terms.length; i++) {
        if (blob.indexOf(terms[i]) === -1) { return false; }
      }
    }
    return true;
  }

  function sortEntries(list) {
    var sorted = list.slice();
    if (state.sort === 'importance') {
      sorted.sort(function (a, b) {
        var d = (b.importance || 0) - (a.importance || 0);
        if (d !== 0) { return d; }
        return String(b.collected_date).localeCompare(String(a.collected_date));
      });
    } else if (state.sort === 'date-asc') {
      sorted.sort(function (a, b) {
        return String(a.collected_date).localeCompare(String(b.collected_date)) ||
               (b.importance || 0) - (a.importance || 0) ||
               String(a.id).localeCompare(String(b.id));
      });
    } else {
      sorted.sort(function (a, b) {
        return String(b.collected_date).localeCompare(String(a.collected_date)) ||
               (b.importance || 0) - (a.importance || 0) ||
               String(a.id).localeCompare(String(b.id));
      });
    }
    return sorted;
  }

  /* ---------- rendering ---------- */

  function renderEntry(entry) {
    var node = el.tpl.content.firstElementChild.cloneNode(true);

    if (entry.id) { node.id = 'n-' + entry.id; }

    var cats = node.querySelector('.entry__cats');
    (entry.categories || []).forEach(function (c) {
      var tag = document.createElement('span');
      tag.className = 'cat-tag';
      tag.textContent = state.catLabels[c] || c;
      cats.appendChild(tag);
    });

    node.querySelector('.entry__title').textContent = entry.title || '(無題)';
    node.querySelector('.entry__oneline').textContent = entry.one_line || '';

    ['what_happened', 'why_important', 'question'].forEach(function (field) {
      var target = node.querySelector('[data-field="' + field + '"]');
      if (target) { target.textContent = entry[field] || ''; }
    });

    var ul = node.querySelector('.sources');
    var sources = (entry.sources || []).filter(function (s) {
      return s && isSafeUrl(s.url);
    });

    if (!sources.length) {
      var li = document.createElement('li');
      li.textContent = '出典リンクなし';
      ul.appendChild(li);
    } else {
      sources.forEach(function (s) {
        var item = document.createElement('li');
        if (s.publisher) {
          var pub = document.createElement('span');
          pub.className = 'source__pub';
          pub.textContent = s.publisher;
          item.appendChild(pub);
        }
        var a = document.createElement('a');
        a.href = s.url;                 // isSafeUrl() で http/https を確認済み
        a.textContent = s.title || s.url;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        item.appendChild(a);
        ul.appendChild(item);
      });
    }

    return node;
  }

  function renderDayGroup(dateKey, entries) {
    var section = document.createElement('section');
    section.className = 'day';

    var h2 = document.createElement('h2');
    h2.className = 'day__heading';

    var label = document.createElement('span');
    label.textContent = formatDate(dateKey);
    h2.appendChild(label);

    var count = document.createElement('span');
    count.className = 'day__count';
    count.textContent = entries.length + '件';
    h2.appendChild(count);

    section.appendChild(h2);
    entries.forEach(function (e) { section.appendChild(renderEntry(e)); });
    return section;
  }

  function render() {
    var visible = sortEntries(state.entries.filter(matches));

    el.archive.textContent = '';

    if (!state.entries.length) {
      show(el.empty, true);
      show(el.noresult, false);
      show(el.archive, false);
      el.resultCount.textContent = '';
      updateResetButton();
      return;
    }
    show(el.empty, false);

    if (!visible.length) {
      show(el.noresult, true);
      show(el.archive, false);
      el.resultCount.textContent = '0件';
      updateResetButton();
      return;
    }
    show(el.noresult, false);

    if (state.sort === 'importance') {
      // 重要度順のときは日付でまとめず一覧表示する
      var flat = document.createElement('section');
      flat.className = 'day';
      visible.forEach(function (e) { flat.appendChild(renderEntry(e)); });
      el.archive.appendChild(flat);
    } else {
      var order = [];
      var groups = {};
      visible.forEach(function (e) {
        var key = e.collected_date || '不明';
        if (!groups[key]) { groups[key] = []; order.push(key); }
        groups[key].push(e);
      });
      order.forEach(function (key) {
        el.archive.appendChild(renderDayGroup(key, groups[key]));
      });
    }

    show(el.archive, true);
    el.resultCount.textContent = visible.length + '件を表示中（全' + state.entries.length + '件）';
    updateResetButton();
    focusHashTarget();
  }

  function updateResetButton() {
    var f = state.filters;
    var active = Boolean(f.q || f.month || f.cats.length);
    show(el.reset, active);
  }

  /* ---------- controls ---------- */

  function buildCategoryChips() {
    var counts = {};
    state.entries.forEach(function (e) {
      (e.categories || []).forEach(function (c) {
        counts[c] = (counts[c] || 0) + 1;
      });
    });

    el.chips.textContent = '';

    var used = state.categories.filter(function (c) { return counts[c.id]; });
    // データにあるがカテゴリー定義に無いものも拾う
    Object.keys(counts).forEach(function (id) {
      var known = state.categories.some(function (c) { return c.id === id; });
      if (!known) { used.push({ id: id, label: id }); }
    });

    used.forEach(function (cat) {
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'chip';
      btn.setAttribute('aria-pressed', 'false');
      btn.dataset.cat = cat.id;
      btn.textContent = cat.label;

      var n = document.createElement('span');
      n.className = 'chip__count';
      n.textContent = counts[cat.id];
      btn.appendChild(n);

      btn.addEventListener('click', function () {
        var i = state.filters.cats.indexOf(cat.id);
        if (i === -1) {
          state.filters.cats.push(cat.id);
          btn.setAttribute('aria-pressed', 'true');
        } else {
          state.filters.cats.splice(i, 1);
          btn.setAttribute('aria-pressed', 'false');
        }
        render();
      });

      el.chips.appendChild(btn);
    });
  }

  function buildMonthOptions() {
    var months = {};
    state.entries.forEach(function (e) {
      var m = monthOf(e);
      if (m) { months[m] = (months[m] || 0) + 1; }
    });

    Object.keys(months).sort().reverse().forEach(function (m) {
      var opt = document.createElement('option');
      opt.value = m;
      opt.textContent = formatMonth(m) + '（' + months[m] + '件）';
      el.month.appendChild(opt);
    });
  }

  function debounce(fn, wait) {
    var t;
    return function () {
      clearTimeout(t);
      t = setTimeout(fn, wait);
    };
  }

  function bindControls() {
    el.q.addEventListener('input', debounce(function () {
      state.filters.q = normalize(el.q.value).trim();
      render();
    }, 150));

    el.month.addEventListener('change', function () {
      state.filters.month = el.month.value;
      render();
    });

    el.sort.addEventListener('change', function () {
      state.sort = el.sort.value;
      render();
    });

    el.reset.addEventListener('click', function () {
      state.filters = { q: '', month: '', cats: [] };
      el.q.value = '';
      el.month.value = '';
      Array.prototype.forEach.call(
        el.chips.querySelectorAll('.chip'),
        function (c) { c.setAttribute('aria-pressed', 'false'); }
      );
      render();
      el.q.focus();
    });
  }

  function focusHashTarget() {
    if (!window.location.hash) { return; }
    var target = document.getElementById(window.location.hash.slice(1));
    if (target) { target.scrollIntoView({ block: 'start' }); }
  }

  /* ---------- boot ---------- */

  function applyMeta(meta) {
    var updated = meta && meta.last_updated;
    el.lastUpdated.textContent = updated ? formatDate(String(updated).slice(0, 10)) : '未更新';
    el.entryCount.textContent = state.entries.length;
    el.generator.textContent = (meta && meta.generator) || 'scripts/update_news.py';
    if (updated) {
      document.title = '教育時事アーカイブ（最終更新 ' +
        formatDate(String(updated).slice(0, 10)) + '）';
    }
  }

  function load() {
    fetch(DATA_URL, { cache: 'no-cache' })
      .then(function (res) {
        if (!res.ok) { throw new Error('HTTP ' + res.status); }
        return res.json();
      })
      .then(function (data) {
        state.entries = Array.isArray(data.entries) ? data.entries : [];
        state.categories = Array.isArray(data.categories) ? data.categories : [];
        state.categories.forEach(function (c) { state.catLabels[c.id] = c.label; });

        applyMeta(data.meta);
        buildCategoryChips();
        buildMonthOptions();
        bindControls();

        show(el.loading, false);
        render();
      })
      .catch(function (err) {
        show(el.loading, false);
        show(el.error, true);
        el.lastUpdated.textContent = '取得失敗';
        if (window.console) { console.error('[news] load failed:', err); }
      });
  }

  load();
})();
