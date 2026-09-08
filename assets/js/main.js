/* United Pharma — Minimal interaction layer
   No heavy libraries. Minimal animation as per brief. */
(function () {
  'use strict';

  /* ── Mobile nav toggle ── */
  var toggle = document.getElementById('nav-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var expanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', String(!expanded));
      document.body.classList.toggle('nav-open');
    });
  }

  /* ── Sticky header shadow ── */
  var header = document.getElementById('site-header');
  if (header) {
    window.addEventListener('scroll', function () {
      header.style.boxShadow = window.scrollY > 10
        ? '0 2px 20px rgba(0,0,0,0.10)'
        : '';
    }, { passive: true });
  }

  /* ── Scroll reveal ── */
  var reveals = document.querySelectorAll('.reveal');
  if (reveals.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { observer.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ── Tab switching (product detail) ── */
  var tabBtns = document.querySelectorAll('.tab-btn');
  tabBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = this.dataset.tab;
      tabBtns.forEach(function (b) { b.classList.remove('active'); });
      this.classList.add('active');
      document.querySelectorAll('.tab-panel').forEach(function (p) {
        p.style.display = (p.id === target) ? 'block' : 'none';
      });
    });
  });

  /* ── Product filter (client-side demo) ── */
  var filterInputs = document.querySelectorAll('.filter-opt input[type="checkbox"]');
  filterInputs.forEach(function (input) {
    input.addEventListener('change', runFilters);
  });

  function runFilters() {
    var active = { solution: [], brand: [], type: [] };
    document.querySelectorAll('.filter-opt input:checked').forEach(function (inp) {
      var g = inp.dataset.group;
      if (g && active[g]) active[g].push(inp.value);
    });

    document.querySelectorAll('[data-solution]').forEach(function (card) {
      var s = card.dataset.solution || '';
      var b = card.dataset.brand || '';
      var t = card.dataset.type || '';
      var ok =
        (!active.solution.length || active.solution.indexOf(s) > -1) &&
        (!active.brand.length   || active.brand.indexOf(b)   > -1) &&
        (!active.type.length    || active.type.indexOf(t)    > -1);
      card.closest('.card-wrap') ? card.closest('.card-wrap').style.display = ok ? '' : 'none'
                                 : card.style.display = ok ? '' : 'none';
    });

    renderChips(active);
  }

  function renderChips(active) {
    var container = document.getElementById('active-chips');
    if (!container) return;
    container.innerHTML = '';
    Object.keys(active).forEach(function (g) {
      active[g].forEach(function (val) {
        var chip = document.createElement('span');
        chip.className = 'f-chip';
        chip.innerHTML = val + ' <button onclick="clearF(\'' + g + '\',\'' + val + '\')" aria-label="Remove filter">×</button>';
        container.appendChild(chip);
      });
    });
  }

  window.clearF = function (group, val) {
    var inp = document.querySelector('.filter-opt input[data-group="' + group + '"][value="' + val + '"]');
    if (inp) { inp.checked = false; runFilters(); }
  };

  /* ── URL Parameter Parsing ── */
  var params = new URLSearchParams(window.location.search);

  // 1. Request form pre-fill
  var prefill = params.get('product');
  if (prefill) {
    var field = document.getElementById('products-of-interest');
    if (field) field.value = decodeURIComponent(prefill);
  }

  // 2. Product catalogue filter pre-fill
  var prefillBrand = params.get('brand');
  var prefillSolution = params.get('solution');
  var prefillType = params.get('type');
  var hasFilter = false;

  if (prefillBrand) {
    var bInput = document.querySelector('.filter-opt input[data-group="brand"][value="' + prefillBrand + '"]');
    if (bInput) { bInput.checked = true; hasFilter = true; }
  }
  if (prefillSolution) {
    var sInput = document.querySelector('.filter-opt input[data-group="solution"][value="' + prefillSolution + '"]');
    if (sInput) { sInput.checked = true; hasFilter = true; }
  }
  if (prefillType) {
    var tInput = document.querySelector('.filter-opt input[data-group="type"][value="' + prefillType + '"]');
    if (tInput) { tInput.checked = true; hasFilter = true; }
  }

  if (hasFilter && typeof runFilters === 'function') {
    runFilters();
  }

  /* ── Hero Live Search Bar Logic ── */
  var searchInput = document.getElementById('hero-live-search');
  var resultsPanel = document.getElementById('search-results-panel');
  var resultsList = document.getElementById('search-results-list');
  var countText = document.getElementById('search-count-text');
  var clearBtn = document.getElementById('clear-search-btn');

  if (searchInput && resultsPanel && resultsList) {
    var allCatalogue = [];

    function initSearchData() {
      if (window.PRODUCTS_CATALOGUE_DATA || window.MERIL_CATALOGUE_DATA) {
        allCatalogue = (window.PRODUCTS_CATALOGUE_DATA || []).concat(window.MERIL_CATALOGUE_DATA || []);
      } else {
        fetch('assets/data/products-catalogue.json')
          .then(function(res) { return res.json(); })
          .then(function(data) {
            allCatalogue = data;
            fetch('assets/data/meril-catalogue.json')
              .then(function(res2) { return res2.json(); })
              .then(function(data2) { allCatalogue = allCatalogue.concat(data2); })
              .catch(function() {});
          })
          .catch(function() {});
      }
    }

    initSearchData();

    var selectedIndex = -1;

    searchInput.addEventListener('input', function () {
      var q = this.value.trim().toLowerCase();
      if (clearBtn) clearBtn.style.display = q ? 'block' : 'none';

      if (!q || q.length < 2) {
        resultsPanel.style.display = 'none';
        return;
      }

      var matches = allCatalogue.filter(function (p) {
        var t = (p.title || '').toLowerCase();
        var b = (p.brand || '').toLowerCase();
        var s = (p.solution || '').toLowerCase();
        var o = (p.overview || '').toLowerCase();
        var type = (p.type || '').toLowerCase();

        return t.indexOf(q) > -1 || b.indexOf(q) > -1 || s.indexOf(q) > -1 || o.indexOf(q) > -1 || type.indexOf(q) > -1;
      });

      renderSearchResults(matches.slice(0, 6), q);
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', function () {
        searchInput.value = '';
        clearBtn.style.display = 'none';
        resultsPanel.style.display = 'none';
        searchInput.focus();
      });
    }

    function renderSearchResults(items, query) {
      resultsList.innerHTML = '';
      selectedIndex = -1;

      if (!items.length) {
        countText.textContent = 'No matching products found';
        resultsList.innerHTML = '<div style="padding:16px; text-align:center; color:rgba(255,255,255,0.6); font-size:13px;">No clinical products matching "' + escapeHtml(query) + '"</div>';
        resultsPanel.style.display = 'block';
        return;
      }

      countText.textContent = items.length + ' matching product' + (items.length > 1 ? 's' : '');

      items.forEach(function (item) {
        var a = document.createElement('a');
        a.className = 'search-result-item';
        a.href = 'product-detail.html?id=' + item.id;
        
        var brandLabel = item.brand || 'United Pharma Partner';
        var typeLabel = item.type || 'Product';
        var solutionLabel = item.solution || 'Clinical Solution';

        a.innerHTML = 
          '<div>' +
            '<div class="sr-title">' + escapeHtml(item.title) + '</div>' +
            '<div class="sr-meta">' +
              '<span>' + escapeHtml(brandLabel) + '</span> • ' +
              '<span>' + escapeHtml(solutionLabel) + '</span>' +
            '</div>' +
          '</div>' +
          '<div><span class="sr-badge">' + escapeHtml(typeLabel) + '</span></div>';

        resultsList.appendChild(a);
      });

      resultsPanel.style.display = 'block';
    }

    function escapeHtml(str) {
      return String(str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Keyboard navigation
    searchInput.addEventListener('keydown', function (e) {
      var items = resultsList.querySelectorAll('.search-result-item');
      if (!items.length || resultsPanel.style.display === 'none') return;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        selectedIndex = (selectedIndex + 1) % items.length;
        updateSelection(items);
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        selectedIndex = (selectedIndex - 1 + items.length) % items.length;
        updateSelection(items);
      } else if (e.key === 'Enter') {
        if (selectedIndex >= 0 && items[selectedIndex]) {
          e.preventDefault();
          window.location.href = items[selectedIndex].href;
        }
      } else if (e.key === 'Escape') {
        resultsPanel.style.display = 'none';
      }
    });

    function updateSelection(items) {
      items.forEach(function (el, idx) {
        if (idx === selectedIndex) {
          el.classList.add('selected');
          el.scrollIntoView({ block: 'nearest' });
        } else {
          el.classList.remove('selected');
        }
      });
    }

    // Close on click outside
    document.addEventListener('click', function (e) {
      if (!searchInput.contains(e.target) && !resultsPanel.contains(e.target)) {
        resultsPanel.style.display = 'none';
      }
    });
  }

}());
