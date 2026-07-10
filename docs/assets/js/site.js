(function () {
  "use strict";

  var STORAGE_KEY = "cloud-engineer-roadmap:progress";

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch (e) {
      return {};
    }
  }

  function saveProgress(data) {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
    } catch (e) {
      /* localStorage indisponível (ex: modo privado) - progresso não será salvo */
    }
  }

  function updateAllBars() {
    var progress = loadProgress();
    var totalDone = 0;
    var totalAll = 0;

    document.querySelectorAll(".sidebar-module").forEach(function (module) {
      var moduleCheckboxes = module.querySelectorAll(".progress-checkbox");
      var done = 0;
      moduleCheckboxes.forEach(function (cb) {
        if (progress[cb.getAttribute("data-progress-key")]) done++;
      });
      var total = moduleCheckboxes.length;
      totalDone += done;
      totalAll += total;

      var countEl = module.querySelector("[data-module-count]");
      var fillEl = module.querySelector("[data-module-fill]");
      if (countEl) countEl.textContent = done + "/" + total;
      if (fillEl) fillEl.style.width = (total ? (done / total) * 100 : 0) + "%";
    });

    var overallCount = document.querySelector("[data-overall-count]");
    var overallFill = document.querySelector("[data-overall-fill]");
    if (overallCount) overallCount.textContent = totalDone + "/" + totalAll;
    if (overallFill) overallFill.style.width = (totalAll ? (totalDone / totalAll) * 100 : 0) + "%";
  }

  function initProgress() {
    var checkboxes = document.querySelectorAll(".progress-checkbox");
    if (!checkboxes.length) return;

    var progress = loadProgress();

    checkboxes.forEach(function (checkbox) {
      var key = checkbox.getAttribute("data-progress-key");
      checkbox.checked = !!progress[key];
      checkbox.addEventListener("change", function () {
        var current = loadProgress();
        if (checkbox.checked) {
          current[key] = true;
        } else {
          delete current[key];
        }
        saveProgress(current);
        updateAllBars();
      });
    });

    updateAllBars();
  }

  function initMarkAllButtons() {
    document.querySelectorAll(".sidebar-mark-all").forEach(function (button) {
      button.addEventListener("click", function () {
        var scope = button.getAttribute("data-mark-all-scope");
        var container = scope === "module" ? button.closest(".sidebar-module") : document;
        if (!container) return;

        var checkboxes = container.querySelectorAll(".progress-checkbox");
        if (!checkboxes.length) return;

        var allChecked = Array.prototype.every.call(checkboxes, function (cb) {
          return cb.checked;
        });
        var target = !allChecked;

        var current = loadProgress();
        checkboxes.forEach(function (cb) {
          cb.checked = target;
          var key = cb.getAttribute("data-progress-key");
          if (target) {
            current[key] = true;
          } else {
            delete current[key];
          }
        });
        saveProgress(current);
        updateAllBars();
      });
    });
  }

  function initMobileSidebar() {
    var toggle = document.getElementById("sidebar-toggle");
    var backdrop = document.getElementById("sidebar-backdrop");
    if (!toggle) return;

    var icon = toggle.querySelector("i");

    function setOpen(isOpen) {
      document.body.classList.toggle("sidebar-open", isOpen);
      toggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      toggle.setAttribute("aria-label", isOpen ? "Fechar menu de navegação" : "Abrir menu de navegação");
      if (icon) {
        icon.classList.toggle("fa-bars", !isOpen);
        icon.classList.toggle("fa-xmark", isOpen);
      }
    }

    function close() {
      setOpen(false);
    }

    toggle.addEventListener("click", function () {
      setOpen(!document.body.classList.contains("sidebar-open"));
    });

    if (backdrop) backdrop.addEventListener("click", close);

    document.querySelectorAll(".sidebar a").forEach(function (link) {
      link.addEventListener("click", close);
    });
  }

  function initReadingProgress() {
    var bar = document.getElementById("reading-progress");
    if (!bar) return;

    function update() {
      var scrollTop = window.scrollY || document.documentElement.scrollTop;
      var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = pct + "%";
    }

    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    update();
  }

  function initFadeIn() {
    var targets = [];
    document.querySelectorAll(".main-content > *, .container > *").forEach(function (el) {
      // Grids (ex: cards do roadmap) animam item por item, não como um bloco
      // único — senão só revelam depois que a grade inteira cruza o limiar.
      if (el.classList.contains("roadmap-grid") && el.children.length) {
        targets = targets.concat(Array.prototype.slice.call(el.children));
      } else {
        targets.push(el);
      }
    });
    if (!targets.length || !("IntersectionObserver" in window)) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            var target = entry.target;
            target.classList.add("is-visible");
            observer.unobserve(target);
            // Remove as classes de animação ao fim da transição: sem isso,
            // o transform: translateY(0) do fade-in empata em especificidade
            // com o transform do :hover e, por ordem no CSS, vence — travando
            // o hover dos cards que foram revelados por scroll.
            target.addEventListener(
              "transitionend",
              function () {
                target.classList.remove("fade-in-el", "is-visible");
              },
              { once: true }
            );
          }
        });
      },
      { threshold: 0.1 }
    );

    var viewportHeight = window.innerHeight;
    targets.forEach(function (el) {
      // Só anima o que já nasce abaixo da dobra; o que já está visível no
      // carregamento aparece direto, sem depender de rolagem para revelar.
      if (el.getBoundingClientRect().top > viewportHeight) {
        el.classList.add("fade-in-el");
        observer.observe(el);
      }
    });
  }

  function initThemeToggle() {
    var THEME_KEY = "cloud-engineer-roadmap:theme";
    var button = document.getElementById("theme-toggle");
    if (!button) return;

    button.addEventListener("click", function () {
      var isLight = document.documentElement.getAttribute("data-theme") === "light";
      var next = isLight ? "dark" : "light";
      if (isLight) {
        document.documentElement.removeAttribute("data-theme");
      } else {
        document.documentElement.setAttribute("data-theme", "light");
      }
      try {
        localStorage.setItem(THEME_KEY, next);
      } catch (e) {
        /* localStorage indisponível (ex: modo privado) - preferência não será salva */
      }
    });
  }

  function initExternalLinks() {
    var host = window.location.hostname;
    document.querySelectorAll('a[href^="http"]').forEach(function (link) {
      if (link.hostname && link.hostname !== host) {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "noopener noreferrer");
      }
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initProgress();
    initMarkAllButtons();
    initMobileSidebar();
    initReadingProgress();
    initFadeIn();
    initExternalLinks();
    initThemeToggle();
  });
})();
