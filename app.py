import os

from flask import Flask, render_template

app = Flask(__name__)

SERVICES = [
    {
        "title": "Web Design",
        "description": "Stunning, conversion-focused designs that capture your brand essence and engage your audience from the first click.",
        "icon": "01",
    },
    {
        "title": "Web Development",
        "description": "Lightning-fast, scalable websites built with modern technologies. From simple landing pages to complex web applications.",
        "icon": "02",
    },
    {
        "title": "E-Commerce",
        "description": "Powerful online stores that drive sales. Custom shopping experiences optimized for conversion and customer retention.",
        "icon": "03",
    },
    {
        "title": "Brand Identity",
        "description": "Cohesive visual identities that tell your story. Logos, typography, color systems, and brand guidelines.",
        "icon": "04",
    },
    {
        "title": "SEO & Performance",
        "description": "Get found and load fast. Technical optimization that improves search rankings and user experience.",
        "icon": "05",
    },
    {
        "title": "Maintenance & Support",
        "description": "Keep your digital presence running smoothly. Updates, security, hosting, and ongoing improvements.",
        "icon": "06",
    },
]

PROJECTS = [
    {
        "title": "Apex Ventures",
        "category": "Fintech Platform",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    },
    {
        "title": "Nomad Coffee Co.",
        "category": "E-Commerce",
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=80",
    },
    {
        "title": "Kinetic Studio",
        "category": "Creative Agency",
        "image": "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=1200&q=80",
    },
    {
        "title": "Evergreen Health",
        "category": "Healthcare SaaS",
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80",
    },
]

TESTIMONIALS = [
    {
        "quote": "Cloud Digital transformed our outdated website into a conversion machine. Our leads increased by 340% in the first quarter.",
        "author": "Ananya Sharma",
        "role": "Founder, Apex Ventures",
        "avatar": "/static/images/review-ananya.jpg",
    },
    {
        "quote": "The attention to detail is unmatched. They did not just build us a website, they built us a brand experience.",
        "author": "Rohan Mehta",
        "role": "Founder, Nomad Coffee Co.",
        "avatar": "/static/images/review-rohan.jpg",
    },
    {
        "quote": "Working with Cloud Digital felt like having an in-house team. They understood our vision from day one.",
        "author": "Priya Nair",
        "role": "Marketing Director, Kinetic Studio",
        "avatar": "/static/images/review-priya.jpg",
    },
]

STATS = [
    {"value": "30+", "label": "Projects Delivered"},
    {"value": "98%", "label": "Client Satisfaction"},
    {"value": "2+", "label": "Years Experience"},
]


@app.get("/")
def home():
    return render_template(
        "index.html",
        services=SERVICES,
        projects=PROJECTS,
        testimonials=TESTIMONIALS,
        stats=STATS,
        year=2026,
    )


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
