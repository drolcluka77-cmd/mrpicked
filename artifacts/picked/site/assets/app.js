/* Mr. Picked — page behaviour. All text lives in the HTML; this file only adds interaction. */
(function () {
  'use strict';
  var M = window.MP;
  if (!M) return;
  var L = M.lang;
  var root = document.documentElement;
  var reduce = !!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var hadIntro = !root.classList.contains('no-intro') && !reduce;

  var SEP = { EN: ',', SL: '.', HR: '.', IT: '.', DE: '.', HU: ' ' };
  function fmt(n) {
    var s = String(Math.round(Math.abs(n))).replace(/\B(?=(\d{3})+(?!\d))/g, SEP[L]);
    return L === 'EN' ? '€' + s : s + ' €';
  }
  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  var CHECK = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12l5 5L20 7"></path></svg>';

  /* Remember an explicit language choice so the root page stops redirecting. */
  $$('.langs a').forEach(function (a) {
    a.addEventListener('click', function () {
      try { localStorage.setItem('mp-lang', a.getAttribute('data-lang')); } catch (e) {}
    });
  });

  /* ---------- Shared form state ---------- */
  var S = { sent: false, mail: '', busy: false, err: 0, warn: false, rid: '', sig: '' };
  var form = $('#check-form'), thanks = $('#check-thanks');
  var bizIn = $('#cta-biz'), mailIn = $('#cta-mail'), mbar = $('.mbar');
  var msgEl = $('#check-msg'), warnEl = $('#check-warn'), submitBtn = form && $('button[type="submit"]', form);
  var MT = M.mailText || [];
  function validMail(v) { return v.length <= 254 && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v); }
  function uuid() {
    if (window.crypto && crypto.randomUUID) return crypto.randomUUID();
    var b = new Uint8Array(16); crypto.getRandomValues(b);
    b[6] = (b[6] & 15) | 64; b[8] = (b[8] & 63) | 128;
    var h = Array.prototype.map.call(b, function (x) { return (x + 256).toString(16).slice(1); }).join('');
    return h.slice(0, 8) + '-' + h.slice(8, 12) + '-' + h.slice(12, 16) + '-' + h.slice(16, 20) + '-' + h.slice(20);
  }
  function showFormState() {
    if (submitBtn) { submitBtn.disabled = S.busy; submitBtn.textContent = S.busy ? MT[0] : M.btn; }
    if (msgEl) { msgEl.hidden = !(S.busy || S.err); msgEl.className = 'form-msg' + (S.busy ? ' info' : ''); msgEl.textContent = S.busy ? MT[0] : (MT[S.err] || ''); }
    if (warnEl) { warnEl.hidden = !S.warn; warnEl.textContent = MT[4] || ''; }
  }
  function markSent() {
    S.sent = true;
    if (form) form.hidden = true;
    if (thanks) thanks.hidden = false;
    if (mbar) mbar.classList.add('gone');
    showFormState();
    renderDemo();
  }
  // Sends the free-report request to the API server (emails info@mrpicked.eu and confirms to the visitor).
  function sendReport(business, email, consent) {
    if (S.busy || S.sent) return;
    var payload = { email: email, business: business.slice(0, 200), language: M.lang, consent: !!consent };
    var sig = JSON.stringify(payload);
    if (sig !== S.sig) { S.sig = sig; S.rid = uuid(); }  // same request → same id, so a retry is not sent twice
    payload.requestId = S.rid;
    S.busy = true; S.err = 0; showFormState(); renderDemo();
    fetch('/api/report-requests', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) {
        if (!r.ok) throw r.status;
        return r.json().catch(function () { return {}; });
      })
      .then(function (res) { S.busy = false; S.warn = res && res.confirmationSent === false; markSent(); sendToCrm(business, email); })
      .catch(function (st) { S.busy = false; S.err = st === 429 ? 3 : st === 400 ? 1 : 2; showFormState(); renderDemo(); });
  }
  // Copy of the request to the sales CRM (a seller follows up; with city + activity the CRM also runs an AI analysis).
  // Best effort: the visitor's request is already accepted, so failures here are ignored.
  function sendToCrm(business, email) {
    try {
      var n = document.getElementById('demo-name'), c = document.getElementById('demo-city'), k = document.getElementById('demo-cat');
      var ranDemo = n && (n.value || '').trim();
      var body = {
        ime: business.slice(0, 120), podjetje: business.slice(0, 160), email: email,
        jezik: M.lang, stran: location.pathname, vrsta: 'brezplačno poročilo', website: ''
      };
      if (ranDemo && c && (c.value || '').trim()) body.kraj = c.value.trim().slice(0, 80);
      if (ranDemo && k && (k.value || '').trim()) body.dejavnost = k.value.trim().slice(0, 80);
      fetch('https://portal.aureliagroup.eu/api/public/povprasevanje?produkt=picked', {
        method: 'POST', mode: 'cors', keepalive: true,
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body)
      }).catch(function () {});
    } catch (e) { /* ignore */ }
  }
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var v = (mailIn.value || '').trim(), b = (bizIn.value || '').trim();
      if (!b) { S.err = 1; showFormState(); bizIn.setAttribute('aria-invalid', 'true'); bizIn.focus(); return; }
      bizIn.removeAttribute('aria-invalid');
      if (!validMail(v)) { S.err = 1; showFormState(); mailIn.setAttribute('aria-invalid', 'true'); mailIn.focus(); return; }
      mailIn.removeAttribute('aria-invalid');
      S.mail = v;
      var c = form.querySelector('input[name="consent"]');
      sendReport(b, v, c && c.checked);
    });
    bizIn.addEventListener('input', function () { bizIn.setAttribute('data-touched', '1'); });
  }

  /* ---------- Live AI preview ---------- */
  var nameIn = $('#demo-name'), cityIn = $('#demo-city'), out = $('#demo-out'), runBtn = $('#demo-run');
  var D = { stage: 'idle', scan: 0, view: 'today', auto: false, typed: 0, shown: 0, lastPct: '10%', anim: '' };
  var timers = [];
  function clearTimers() { timers.forEach(function (t) { clearTimeout(t); clearInterval(t); }); timers = []; }
  function city() { return (cityIn.value || '').trim() || 'Ljubljana'; }
  var catIn = $('#demo-cat');
  function cat() { return (catIn && (catIn.value || '').trim()) || M.catDef; }
  function fullQ() { return M.dQ.replace('{city}', city()).replace('{cat}', cat()); }
  function shownName() { return (nameIn.value || '').trim() || M.dYour; }

  if (nameIn) nameIn.addEventListener('input', function () {
    if (bizIn && !bizIn.getAttribute('data-touched')) bizIn.value = nameIn.value;
  });

  function cardsHtml() {
    var withP = D.view === 'with';
    var other = function (n, l) { return { n: n, name: M.dOther + ' ' + l, desc: '', mine: false }; };
    var list = withP
      ? [{ n: 1, name: shownName(), desc: M.dDesc, mine: true }, other(2, 'A'), other(3, 'B')]
      : [other(1, 'A'), other(2, 'B'), other(3, 'C')];
    var n = D.auto ? D.shown : 3;
    var h = '';
    for (var i = 0; i < n; i++) {
      var c = list[i], cls = 'rcard' + (c.mine ? ' mine' : '');
      if (D.auto) { if (i === n - 1) cls += ' in'; }
      else if (D.anim === 'view') cls += withP ? (c.mine ? ' rise' : ' shift') : ' in';
      h += '<div class="' + cls + '"><b>' + c.n + '</b><div><div class="nm">' + esc(c.name) + '</div>' +
        (c.desc ? '<div class="ds">' + esc(c.desc) + '</div>' : '') + '</div></div>';
    }
    return h;
  }

  function renderDemo() {
    if (!out) return;
    if (D.stage === 'idle') { out.innerHTML = '<div class="demo-idle">' + esc(M.dIdle) + '</div>'; return; }
    if (D.stage === 'scan') {
      var h = '<div class="scan"><div style="font-weight:600">' + esc(M.dScan) + '</div>';
      ['ChatGPT', 'Gemini', 'Perplexity'].forEach(function (nm, i) {
        var done = D.scan > i, act = D.scan === i;
        h += '<div class="scan-row"><span>' + nm + '</span><span class="scan-st' + (done ? ' done' : act ? ' active' : '') + '">' +
          (done ? CHECK + esc(M.dDone) : act ? '…' : esc(M.dWait)) + '</span></div>';
      });
      h += '<div class="bar"><span style="width:' + Math.round(D.scan / 3 * 100) + '%"></span></div></div>';
      out.innerHTML = h;
      return;
    }
    var withP = D.view === 'with';
    var typing = D.auto && D.typed < fullQ().length;
    var q = D.auto ? fullQ().slice(0, D.typed) : fullQ();
    var showBanner = !D.auto || D.shown >= 3;
    var pct = withP ? '73%' : '10%';
    var html = '<div class="done-wrap">' +
      '<div class="seg" role="group" aria-label="' + esc(M.dToday + ' / ' + M.dWith) + '">' +
      '<button type="button" data-view="today" aria-pressed="' + (!withP) + '">' + esc(M.dToday) + '</button>' +
      '<button type="button" data-view="with" aria-pressed="' + withP + '">' + esc(M.dWith) + '</button></div>' +
      '<div class="bubble-row"><div class="bubble" id="demo-q">' + esc(q) + (typing ? '<span class="caret">|</span>' : '') + '</div></div>' +
      ((!D.auto || D.shown > 0) ? '<div class="muted-s in">' + esc(M.dIntro) + '</div>' : '') +
      cardsHtml();
    if (showBanner) {
      html += '<div class="banner' + (withP ? ' yes' : '') + (D.auto || D.anim === 'view' ? ' in' : '') + '">' +
        '<div class="banner-top"><span>' + esc(withP ? M.dYes : M.dNot) + '</span><span>' +
        esc(M.dScore) + ': ' + (withP ? 22 : 3) + ' ' + esc(M.dOf) + '</span></div>' +
        '<div class="gauge"><span id="demo-gauge" style="width:' + D.lastPct + '"></span></div></div>';
    }
    html += '<div class="demo-foot"><div class="demo-note">' + esc(M.dNote) + '</div>' +
      '<button type="button" class="btn-sm" data-act="again">' + esc(M.dAgain) + '</button></div>';
    if (!D.auto && !S.sent) {
      html += '<div class="ask in"><label for="demo-mail">' + esc(M.dGet) + '</label><div class="ask-row">' +
        '<input id="demo-mail" class="inp-dark" type="email" autocomplete="email" placeholder="' + esc(M.dEmailPh) + '" value="' + esc(S.mail) + '">' +
        '<button type="button" data-act="send"' + (S.busy ? ' disabled' : '') + '>' + esc(S.busy ? MT[0] : M.btn) + '</button></div>' +
        (S.err ? '<div class="form-msg" role="status">' + esc(MT[S.err] || '') + '</div>' : '') +
        '<div class="tiny">' + esc(M.privT) + ' <a href="' + esc(M.privUrl || '#check') + '">' + esc(M.privL) + '</a></div></div>';
    } else if (!D.auto && S.sent) {
      html += '<div class="ask in"><div class="ty-h">' + esc(M.tyH) + '</div><div class="ty-p">' + esc(M.tyP) + '</div>' +
        (S.warn ? '<div class="form-msg warn">' + esc(MT[4] || '') + '</div>' : '') +
        '<a class="btn btn-accent" href="' + esc(M.cal) + '" target="_blank" rel="noopener">' + esc(M.tyBtn) + '</a></div>';
    }
    html += '</div>';
    out.innerHTML = html;
    D.anim = '';
    if (showBanner) {
      var g = $('#demo-gauge');
      requestAnimationFrame(function () { requestAnimationFrame(function () { if (g) g.style.width = pct; }); });
      D.lastPct = pct;
    }
  }

  function startAuto() {
    clearTimers();
    D.stage = 'done'; D.view = 'today'; D.auto = true; D.typed = 0; D.shown = 0; D.lastPct = '10%';
    renderDemo();
    var len = fullQ().length;
    var iv = setInterval(function () {
      D.typed += 1;
      var b = $('#demo-q');
      if (b) b.innerHTML = esc(fullQ().slice(0, D.typed)) + (D.typed < len ? '<span class="caret">|</span>' : '');
      if (D.typed >= len) {
        clearInterval(iv);
        [1, 2, 3].forEach(function (c, i) {
          timers.push(setTimeout(function () { D.shown = c; renderDemo(); }, 300 + i * 320));
        });
        timers.push(setTimeout(function () { D.auto = false; D.view = 'with'; D.anim = 'view'; renderDemo(); }, 300 + 3 * 320 + 1500));
      }
    }, 38);
    timers.push(iv);
  }

  function run() {
    clearTimers();
    D.auto = false; D.stage = 'scan'; D.scan = 0; D.view = 'today'; D.lastPct = '10%';
    renderDemo();
    var iv = setInterval(function () {
      D.scan += 1;
      if (D.scan >= 3) { clearInterval(iv); D.stage = 'done'; D.anim = 'view'; }
      renderDemo();
    }, 650);
    timers.push(iv);
  }

  if (runBtn) runBtn.addEventListener('click', run);
  if (out) {
    out.addEventListener('click', function (e) {
      var t = e.target.closest('button');
      if (!t) return;
      var v = t.getAttribute('data-view'), act = t.getAttribute('data-act');
      if (v) { clearTimers(); D.auto = false; if (D.view !== v) { D.view = v; D.anim = 'view'; } renderDemo(); }
      if (act === 'again') { clearTimers(); D.auto = false; D.stage = 'idle'; D.view = 'today'; renderDemo(); }
      if (act === 'send') {
        var inp = $('#demo-mail'), val = (inp.value || '').trim();
        if (!validMail(val)) { inp.setAttribute('aria-invalid', 'true'); inp.focus(); return; }
        S.mail = val;
        if (mailIn) mailIn.value = val;
        if (bizIn && !bizIn.value) bizIn.value = nameIn.value;
        var biz = ((nameIn && nameIn.value) || (bizIn && bizIn.value) || '').trim();
        if (!biz) { S.err = 1; renderDemo(); if (nameIn) nameIn.focus(); return; }
        sendReport(biz, val, false);
      }
    });
    out.addEventListener('input', function (e) { if (e.target.id === 'demo-mail') S.mail = e.target.value; });
    out.addEventListener('keydown', function (e) {
      if (e.target.id === 'demo-mail' && e.key === 'Enter') { e.preventDefault(); var b = $('[data-act="send"]', out); if (b) b.click(); }
    });
    timers.push(setTimeout(startAuto, reduce ? 300 : hadIntro ? 2700 : 1400));
  }

  /* ---------- How it works tabs ---------- */
  var tabs = $$('.tabs [role="tab"]');
  tabs.forEach(function (tb, i) {
    tb.addEventListener('click', function () {
      tabs.forEach(function (o, j) {
        o.setAttribute('aria-selected', String(i === j));
        o.tabIndex = i === j ? 0 : -1;
        var p = document.getElementById(o.getAttribute('aria-controls'));
        if (p) p.hidden = i !== j;
      });
    });
    tb.addEventListener('keydown', function (e) {
      if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
      var n = (i + (e.key === 'ArrowRight' ? 1 : tabs.length - 1)) % tabs.length;
      tabs[n].click(); tabs[n].focus();
    });
  });

  /* ---------- Pricing builder + ROI ---------- */
  var P = { tier: 1, sel: {} };
  var ADD = M.addons;
  var monthly = M.prices[1];
  function addonMo(a) { return (a.mo1 != null && P.tier >= 1) ? a.mo1 : a.mo; }
  function priceLabel(a) {
    var parts = [], mo = addonMo(a);
    if (mo) parts.push(fmt(mo) + ' ' + M.perMonth);
    if (a.once) parts.push(fmt(a.once) + ' ' + (a.mo ? M.setup : M.once));
    return parts.join(' + ');
  }
  function renderPricing() {
    $$('.tier').forEach(function (b) { b.setAttribute('aria-pressed', String(+b.getAttribute('data-tier') === P.tier)); });
    $$('.incl').forEach(function (u) { u.hidden = +u.getAttribute('data-incl') !== P.tier; });
    var it = $('#incl-title'); if (it) it.textContent = M.inclH + ' ' + M.names[P.tier];
    monthly = M.prices[P.tier];
    var once = M.setups[P.tier] || 0;
    var lines = [[M.names[P.tier], fmt(M.prices[P.tier]) + ' ' + M.perMonth]];
    if (once) lines.push([M.names[P.tier] + ' · ' + M.setup, fmt(once) + ' ' + M.once]);
    ADD.forEach(function (a, i) {
      var btn = $('.addon[data-addon="' + a.id + '"]');
      var included = a.inc != null && P.tier >= a.inc;
      var locked = a.minTier != null && P.tier < a.minTier;  // e.g. Lead Engine: only with Recommended or Concierge
      var on = !included && !locked && !!P.sel[a.id];
      if (btn) {
        btn.disabled = included || locked;
        if (locked) btn.setAttribute('data-locked', ''); else btn.removeAttribute('data-locked');
        btn.setAttribute('aria-pressed', String(on));
        $('.a-pr', btn).textContent = included ? M.included : locked ? (M.lockedNote || '') : priceLabel(a);
      }
      if (on) { monthly += addonMo(a); once += a.once; lines.push([M.addonNames[i], priceLabel(a)]); }
    });
    var sl = $('#sum-lines');
    if (sl) sl.innerHTML = lines.map(function (l) { return '<div><span>' + esc(l[0]) + '</span><span>' + esc(l[1]) + '</span></div>'; }).join('');
    var sm = $('#sum-monthly'); if (sm) sm.textContent = fmt(monthly);
    var so = $('#sum-once-row'); if (so) { so.hidden = once <= 0; $('#sum-once').textContent = fmt(once); }
    renderRoi();
  }
  $$('.tier').forEach(function (b) { b.addEventListener('click', function () { P.tier = +b.getAttribute('data-tier'); renderPricing(); }); });
  $$('.addon').forEach(function (b) {
    b.addEventListener('click', function () { var id = b.getAttribute('data-addon'); P.sel[id] = !P.sel[id];
      var g = null; ADD.forEach(function (a) { if (a.id === id) g = a.group; });
      if (g && P.sel[id]) ADD.forEach(function (a) { if (a.group === g && a.id !== id) P.sel[a.id] = false; });
      renderPricing(); });
  });

  var spendIn = $('#roi-spend'), guestsIn = $('#roi-guests');
  function renderRoi() {
    if (!spendIn) return;
    var spend = +spendIn.value, guests = +guestsIn.value;
    var rev = Math.round(guests * spend * 4.33), net = rev - monthly, max = Math.max(rev, monthly, 1);
    $('#roi-spend-o').textContent = fmt(spend);
    $('#roi-guests-o').textContent = guests;
    $('#roi-rev').textContent = fmt(rev);
    $('#roi-cost').textContent = fmt(monthly);
    $('#roi-rev-bar').style.width = Math.round(rev / max * 100) + '%';
    $('#roi-cost-bar').style.width = Math.round(monthly / max * 100) + '%';
    var nt = $('#roi-net');
    nt.textContent = (net < 0 ? '−' : '+') + fmt(net);
    nt.classList.toggle('neg', net < 0);
    $('#roi-break').textContent = M.roiBreak.replace('{n}', String(Math.ceil(monthly / (spend * 4.33))));
  }
  if (spendIn) { spendIn.addEventListener('input', renderRoi); guestsIn.addEventListener('input', renderRoi); }
  renderPricing();

  /* ---------- Reveal on scroll + Mr. Picked wink ---------- */
  var winking = false;
  function startWink() {
    if (winking || reduce) return;
    winking = true;
    var open = $('#mp-open'), wink = $('#mp-wink'), brow = $('#mp-brow');
    if (!open) return;
    var blink = function () {
      open.style.opacity = 0; wink.style.opacity = 1; brow.style.opacity = 1;
      setTimeout(function () { open.style.opacity = 1; wink.style.opacity = 0; brow.style.opacity = 0; }, 700);
    };
    setTimeout(blink, 1100);
    setInterval(blink, 3800);
  }
  var rvs = $$('[data-rv]');
  if (reduce || !('IntersectionObserver' in window)) {
    rvs.forEach(function (el) { el.classList.add('on'); });
    startWink();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add('on');
        if (en.target.getAttribute('data-rv') === 'promise') startWink();
        io.unobserve(en.target);
      });
    }, { threshold: 0.08 });
    rvs.forEach(function (el) { io.observe(el); });
  }
})();

/* Comparison table: fold/unfold groups (folded by default on phones, except the first) */
(function () {
  var grps = document.querySelectorAll('.cmp-grp');
  if (!grps.length) return;
  var phone = window.matchMedia && window.matchMedia('(max-width:720px)').matches;
  Array.prototype.forEach.call(grps, function (g, i) {
    var b = g.querySelector('.cmp-tg');
    function set(open) { g.classList.toggle('closed', !open); b.setAttribute('aria-expanded', String(open)); }
    set(!phone || i === 0);
    b.addEventListener('click', function () { set(g.classList.contains('closed')); });
  });
})();
