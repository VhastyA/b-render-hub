import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'b_render1_architectural_hub_2026'

@app.route('/')
def home():
    # Explicit link list definitions to feed the front-end elements directly
    social_links = [
        {"name": "WhatsApp", "url": "https://tr.ee/pJ4J3yGbgv", "icon": "💬", "color": "#25D366"},
        {"name": "Instagram", "url": "https://tr.ee/WlihOabF86", "icon": "📸", "color": "#E1306C"},
        {"name": "TikTok", "url": "https://tr.ee/FEzx96lXpc", "icon": "🎵", "color": "#00f2fe"},
        {"name": "YouTube", "url": "https://tr.ee/aeYCutRTr3", "icon": "📺", "color": "#FF0000"},
        {"name": "X (Twitter)", "url": "https://tr.ee/7NAcWxIEBZ", "icon": "🐦", "color": "#1DA1F2"},
        {"name": "Facebook", "url": "https://tr.ee/N-TVoA_APA", "icon": "👥", "color": "#1877F2"},
        {"name": "Threads", "url": "https://tr.ee/2lU4tCptEO", "icon": "🧵", "color": "#ffffff"}
    ]
    return render_template('index.html', links=social_links)

if __name__ == '__main__':
    app.run(debug=True)
