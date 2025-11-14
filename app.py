from flask import Flask, jsonify, request
from routes.bot_routes import bot_bp
from config import Config
from database import init_db

# إنشاء التطبيق
app = Flask(__name__)
app.config.from_object(Config)
from flask import render_template

# تسجيل المسارات (routes)
app.register_blueprint(bot_bp)

# صفحة رئيسية بسيطة
@app.route('/')
def home():
    return jsonify({"message": "🤖 يوسف بوت العقارات جاهز لاستقبال الطلبات!"})
@app.route('/chat')
def chat_page():
    return render_template('chat.html')

# تشغيل التطبيق
if __name__ == "__main__":
    print("🔥 Flask app is starting...")
    init_db()  # إنشاء قاعدة البيانات لو مش موجودة
    app.run(debug=True, host="127.0.0.1", port=5000)
