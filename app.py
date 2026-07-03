import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'b_render1_architectural_hub_2026'

@app.route('/')
def home():
    # Explicit link list definitions to feed the front-end elements directly
    social_links = [
        {"name": "WhatsApp", "url": "https://tr.ee/pJ4J3yGbgv", "color": "#25D366"},
        {"name": "Instagram", "url": "https://www.instagram.com/b_render1?igsh=Nmk3MTczYzM1aXFi", "color": "#E1306C"},
        {"name": "TikTok", "url": "https://www.tiktok.com/@b.render5?_r=1&_t=ZS-97hXyN9foQM",: "color": "#00f2fe"},
        {"name": "YouTube", "url": "https://youtube.com/@1b_render?si=MlIqLXb7qqnMnhiV",: "color": "#FF0000"},
        {"name": "X (Twitter)", "url": "https://tr.ee/7NAcWxIEBZ",: "color": "#1DA1F2"},
        {"name": "Facebook", "url": "https://www.facebook.com/share/1JAkCYqSNt/",: "color": "#1877F2"},
         {"name": "Facebook", "url": "https://www.facebook.com/share/1BnoYYRRN9/", :"color": "#1877F2"},
        {"name": "LinkedIn", "url": "https://www.linkedin.com/in/emmanuel-gyarko-a0280a2a7?utm_source=share_via&utm_content=profile&utm_medium=member_android",: "color": "#ffffff"}
    ]
    return render_template('index.html', links=social_links)

if __name__ == '__main__':
    app.run(debug=True)
