(function () {
  "use strict";

  if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") {
    // Fallback si GSAP non chargé
    var revealEls = document.querySelectorAll(".reveal");
    if (revealEls.length && "IntersectionObserver" in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) entry.target.classList.add("visible");
        });
      }, { threshold: 0.1 });
      revealEls.forEach(function (el) { observer.observe(el); });
    }
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  // ----- Hero (page d'accueil) — une ligne + CTA type Moteur & Sens
  var heroContent = document.querySelector(".hero-content");
  if (heroContent) {
    var heroLine1 = heroContent.querySelector(".hero-line1");
    var heroCta = heroContent.querySelector(".hero-cta");

    gsap.timeline({ defaults: { ease: "power3.out" } })
      .fromTo(heroLine1, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 1 }, 0.2)
      .fromTo(heroCta, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.7 }, 0.5);
  }

  // ----- Section "Les dernières nouveautés" — titre puis cartes en révélation séquentielle
  var sectionHeader = document.querySelector("#vedettes .section-header");
  if (sectionHeader) {
    var sectionTitleWrap = sectionHeader.querySelector(".section-title-wrap");
    if (sectionTitleWrap) {
      gsap.timeline({
        scrollTrigger: {
          trigger: sectionHeader,
          start: "top 82%",
          toggleActions: "play none none none",
        },
        defaults: { ease: "power3.out" },
      }).fromTo(sectionTitleWrap, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.8 });
    }
  }

  // Cartes : apparition en décalé (type Moteur & Sens — révélations séquentielles)
  var cards = document.querySelectorAll(".vehicules-grid .vehicule-card.card-reveal");
  if (cards.length) {
    cards.forEach(function (card) {
      var body = card.querySelector(".card-body");
      if (!body) return;
      var title = body.querySelector(".card-title");
      var marque = body.querySelector(".card-marque");
      var specsLine = body.querySelector(".card-specs-line");
      var cta = body.querySelector(".card-cta");
      var innerEls = [title, marque, specsLine, cta].filter(Boolean);

      gsap.set(card, { opacity: 0, y: 36 });
      gsap.set(innerEls, { opacity: 0, y: 12 });

      var cardTl = gsap.timeline({
        scrollTrigger: {
          trigger: card,
          start: "top 90%",
          toggleActions: "play none none none",
        },
        defaults: { ease: "power3.out" },
      });
      cardTl.to(card, { opacity: 1, y: 0, duration: 0.6 });
      if (title) cardTl.to(title, { opacity: 1, y: 0, duration: 0.35 }, "-=0.3");
      if (marque) cardTl.to(marque, { opacity: 1, y: 0, duration: 0.3 }, "-=0.2");
      if (specsLine) cardTl.to(specsLine, { opacity: 1, y: 0, duration: 0.3 }, "-=0.2");
      if (cta) cardTl.to(cta, { opacity: 1, y: 0, duration: 0.25 }, "-=0.15");
    });
  }

  // ----- Contact strip
  var contactStrip = document.querySelector(".contact-strip");
  if (contactStrip) {
    var contactTitle = contactStrip.querySelector(".contact-strip-title");
    var contactDesc = contactStrip.querySelector(".contact-strip-desc");
    var contactMethods = contactStrip.querySelector(".contact-methods");
    if (contactTitle) {
      gsap.timeline({
        scrollTrigger: {
          trigger: contactStrip,
          start: "top 88%",
          toggleActions: "play none none none",
        },
        defaults: { ease: "power3.out" },
      })
        .fromTo(contactTitle, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.7 })
        .fromTo(contactDesc, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.6 }, "-=0.5")
        .fromTo(contactMethods, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.5 }, "-=0.4");
    }
  }

  // ----- Page liste véhicules (page-hero)
  var pageHero = document.querySelector(".page-hero");
  if (pageHero) {
    var pageHeroTitle = pageHero.querySelector(".page-hero-title");
    var pageHeroDesc = pageHero.querySelector(".page-hero-desc");
    if (pageHeroTitle) {
      gsap.timeline({ defaults: { ease: "power3.out" } })
        .fromTo(pageHeroTitle, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.8 }, 0.2)
        .fromTo(pageHeroDesc, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6 }, 0.4);
    }
  }

  // ----- Footer (révélation légère)
  var footer = document.querySelector(".site-footer");
  if (footer) {
    gsap.fromTo(footer, { opacity: 0 }, {
      opacity: 1,
      duration: 1,
      scrollTrigger: {
        trigger: footer,
        start: "top 95%",
        toggleActions: "play none none none",
      },
    });
  }

  // ----- Micro-interactions boutons (scale au clic)
  document.querySelectorAll(".btn, .cta-header").forEach(function (btn) {
    btn.addEventListener("mousedown", function () {
      gsap.to(btn, { scale: 0.97, duration: 0.1 });
    });
    btn.addEventListener("mouseup", function () {
      gsap.to(btn, { scale: 1, duration: 0.2, ease: "power2.out" });
    });
    btn.addEventListener("mouseleave", function () {
      gsap.to(btn, { scale: 1, duration: 0.2, ease: "power2.out" });
    });
  });

  // ----- Parallax léger sur le hero background
  var hero = document.querySelector(".hero");
  if (hero && window.innerWidth > 768) {
    gsap.to(".hero-bg-glow", {
      y: -30,
      ease: "none",
      scrollTrigger: {
        trigger: ".hero",
        start: "top top",
        end: "bottom top",
        scrub: 1,
      },
    });
  }
})();
