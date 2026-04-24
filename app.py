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
        "title": "Market Signals Dashboard",
        "category": "Fintech Platform",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&q=80",
    },
    {
        "title": "Signature Blend Store",
        "category": "E-Commerce",
        "image": "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?w=1200&q=80",
    },
    {
        "title": "Motion Systems Lab",
        "category": "Creative Agency",
        "image": "https://images.unsplash.com/photo-1558655146-9f40138edfeb?w=1200&q=80",
    },
    {
        "title": "CareFlow Portal",
        "category": "Healthcare SaaS",
        "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=1200&q=80",
    },
]

TESTIMONIALS = [
    {
        "quote": "Cloud Digital transformed our outdated website into a conversion machine. Our leads increased by 340% in the first quarter.",
        "author": "Kavya Sharma",
        "company": "Fintech Platform",
        "rating": "4.7",
        "avatar": "/static/images/review-kavya.jpg",
    },
    {
        "quote": "The attention to detail is unmatched. They did not just build us a website, they built us a brand experience.",
        "author": "Arjun Mehta",
        "company": "E-Commerce Brand",
        "rating": "4.0",
        "avatar": "/static/images/review-arjun.jpg",
    },
    {
        "quote": "Working with Cloud Digital felt like having an in-house team. They understood our vision from day one.",
        "author": "Priya Nair",
        "company": "Creative Agency",
        "rating": "4.2",
        "avatar": "/static/images/review-priya.jpg",
    },
    {
        "quote": "We launched on a tight timeline and the team kept every milestone under control. The final site feels premium and performs exactly how we needed.",
        "author": "Rahul Verma",
        "company": "Startup Launch",
        "rating": "4.9",
        "avatar": "/static/images/review-rahul.jpg",
    },
    {
        "quote": "Our mobile conversion rate jumped almost immediately. Every section feels intentional, fast, and easy for customers to move through.",
        "author": "Ananya Iyer",
        "company": "Retail Experience",
        "rating": "4.0",
        "avatar": "/static/images/review-ananya.jpg",
    },
    {
        "quote": "They simplified a messy content structure into something clear and persuasive. Internal teams finally have a site they are proud to share.",
        "author": "Neeraj Patel",
        "company": "Brand Refresh",
        "rating": "4.9",
        "avatar": "/static/images/review-neeraj.jpg",
    },
    {
        "quote": "Communication stayed sharp from kickoff to launch. Feedback rounds were quick, practical, and the execution quality stayed consistent throughout.",
        "author": "Rohan Kulkarni",
        "company": "Growth Campaign",
        "rating": "4.4",
        "avatar": "/static/images/review-rohan.jpg",
    },
    {
        "quote": "This was the first agency partnership that felt genuinely strategic. They improved the story, the visuals, and the customer journey together.",
        "author": "Isha Kapoor",
        "company": "Direct-to-Consumer",
        "rating": "4.0",
        "avatar": "/static/images/review-isha.jpg",
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
