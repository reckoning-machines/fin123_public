/* fin123 — minimal site interactions */
(function () {
    'use strict';

    /* ── Smooth-scroll nav links ── */
    document.querySelectorAll('.nav a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* ── Active-nav highlight on scroll ── */
    var sections = document.querySelectorAll('section[id]');
    var navLinks = document.querySelectorAll('.nav a[href^="#"]');

    function updateActive() {
        var scrollY = window.scrollY + 120;
        sections.forEach(function (section) {
            var top = section.offsetTop;
            var height = section.offsetHeight;
            var id = section.getAttribute('id');
            if (scrollY >= top && scrollY < top + height) {
                navLinks.forEach(function (a) {
                    a.style.color = '';
                    if (a.getAttribute('href') === '#' + id) {
                        a.style.color = 'var(--fg-bright)';
                    }
                });
            }
        });
    }

    var ticking = false;
    window.addEventListener('scroll', function () {
        if (!ticking) {
            requestAnimationFrame(function () {
                updateActive();
                ticking = false;
            });
            ticking = true;
        }
    });

    updateActive();
})();
