/* Villa Belvedere – Menü & Kontaktformular (ohne Cookies, ohne Tracking) */
(function () {
  'use strict';
  // Mobiles Menü
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    var close = function () { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); };
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) { close(); toggle.focus(); }
    });
    window.matchMedia('(min-width: 1061px)').addEventListener('change', close);
  }

  // Kontaktformular per fetch senden (Fallback: normales POST ohne JS)
  var form = document.querySelector('[data-js-form]');
  if (form && window.fetch && window.FormData) {
    var status = form.querySelector('.form-status');
    var button = form.querySelector('button[type="submit"]');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      status.className = 'form-status';
      status.textContent = form.dataset.sending;
      button.disabled = true;
      fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
        .then(function (r) {
          if (!r.ok) throw new Error(r.status);
          form.reset();
          status.className = 'form-status is-ok';
          status.textContent = form.dataset.ok;
        })
        .catch(function () {
          status.className = 'form-status is-err';
          status.textContent = form.dataset.err;
        })
        .then(function () { button.disabled = false; });
    });
  }
})();
