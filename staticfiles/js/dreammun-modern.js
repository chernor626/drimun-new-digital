(() => {
  'use strict';

  const body = document.body;
  const menuToggle = document.querySelector('[data-menu-toggle]');
  const menu = document.querySelector('[data-main-menu]');
  const backToTop = document.querySelector('[data-back-to-top]');

  if (menuToggle && menu) {
    menuToggle.addEventListener('click', () => {
      const isOpen = body.classList.toggle('menu-open');
      menuToggle.setAttribute('aria-expanded', String(isOpen));
      menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    });

    menu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => {
        body.classList.remove('menu-open');
        menuToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  const revealItems = document.querySelectorAll('.reveal, .dm-card, .impact-item, .timeline-item');
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16, rootMargin: '0px 0px -60px 0px' });
    revealItems.forEach((item, index) => {
      item.style.transitionDelay = `${Math.min(index % 6, 5) * 70}ms`;
      revealObserver.observe(item);
    });
  } else {
    revealItems.forEach((item) => item.classList.add('visible'));
  }

  const counters = document.querySelectorAll('[data-counter]');
  const animateCounter = (node) => {
    const target = Number(node.dataset.counter || '0');
    const suffix = node.dataset.suffix || '';
    const duration = 1400;
    const startTime = performance.now();
    const step = (time) => {
      const progress = Math.min((time - startTime) / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      node.textContent = `${Math.round(target * eased).toLocaleString()}${suffix}`;
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  if ('IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });
    counters.forEach((counter) => counterObserver.observe(counter));
  } else {
    counters.forEach(animateCounter);
  }

  document.querySelectorAll('[data-read-more]').forEach((button) => {
    const target = document.querySelector(button.getAttribute('data-read-more'));
    if (!target) return;
    button.addEventListener('click', () => {
      const isOpen = target.toggleAttribute('data-open');
      target.hidden = !isOpen;
      button.setAttribute('aria-expanded', String(isOpen));
      button.querySelector('[data-label]').textContent = isOpen ? 'Show Less' : 'Read More';
    });
  });

  document.querySelectorAll('[data-tilt]').forEach((card) => {
    card.addEventListener('pointermove', (event) => {
      const rect = card.getBoundingClientRect();
      const x = event.clientX - rect.left;
      const y = event.clientY - rect.top;
      const rotateY = ((x / rect.width) - 0.5) * 7;
      const rotateX = ((0.5 - y / rect.height)) * 7;
      card.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
    });
    card.addEventListener('pointerleave', () => {
      card.style.transform = '';
    });
  });

  const updateBackToTop = () => {
    if (!backToTop) return;
    backToTop.classList.toggle('show', window.scrollY > 600);
  };
  window.addEventListener('scroll', updateBackToTop, { passive: true });
  updateBackToTop();

  document.querySelectorAll('a[target="_blank"]').forEach((link) => {
    if (!link.rel.includes('noopener')) link.rel = `${link.rel} noopener noreferrer`.trim();
  });
})();
