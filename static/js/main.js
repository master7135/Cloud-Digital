const header = document.querySelector(".site-header");
const menuButton = document.querySelector(".menu-toggle");
const mobileNav = document.querySelector(".mobile-nav");
const scrollLinks = document.querySelectorAll("[data-scroll]");
const revealNodes = document.querySelectorAll(".reveal");

const getOffset = () => (header ? header.offsetHeight + 12 : 98);

scrollLinks.forEach((link) => {
  link.addEventListener("click", (event) => {
    const href = link.getAttribute("href");

    if (!href || !href.startsWith("#")) {
      return;
    }

    const target = document.querySelector(href);

    if (!target) {
      return;
    }

    event.preventDefault();
    const top = target.getBoundingClientRect().top + window.scrollY - getOffset();

    window.scrollTo({
      top: Math.max(top, 0),
      behavior: "smooth",
    });

    mobileNav?.classList.remove("is-open");
    menuButton?.setAttribute("aria-expanded", "false");
  });
});

menuButton?.addEventListener("click", () => {
  const isOpen = mobileNav?.classList.toggle("is-open");
  menuButton.setAttribute("aria-expanded", String(Boolean(isOpen)));
});

if (!("IntersectionObserver" in window)) {
  revealNodes.forEach((node) => node.classList.add("is-visible"));
} else {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  revealNodes.forEach((node) => observer.observe(node));
}
