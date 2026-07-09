@app.route('/')
def home():
    social_links = [
        {"name": "Instagram", "url": "https://www.instagram.com/b_render1?igsh=Nmk3MTczYzM1aXFi"},
        {"name": "TikTok", "url": "https://www.tiktok.com/@b.render5?_r=1&_t=ZS-97hXyN9foQM"},
        {"name": "YouTube", "url": "https://youtube.com/@1b_render?si=MlIqLXb7qqnMnhiV"},
        {"name": "WhatsApp", "url": "https://wa.me/233552638169"}, # Added this line
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/emmanuel-gyarko-a0280a2a7?utm_source=share_via&utm_content=profile&utm_medium=member_android"},
        {"name": "Facebook Page", "url": "https://www.facebook.com/share/1BnoYYRRN9/"},
        {"name": "Facebook Profile", "url": "https://www.facebook.com/share/1JAkCYqSNt/"}
    ]
    return render_template('index.html', links=social_links)
