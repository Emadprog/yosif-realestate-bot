from flask import Blueprint, request, jsonify, render_template

bot_bp = Blueprint('bot', __name__)

# صفحة الشات
@bot_bp.route('/chat')
def chat_page():
    return render_template('chat.html')

# استقبال الرسائل والرد عليها
@bot_bp.route('/chat', methods=['POST'])
def chat_reply():
    user_message = request.json.get('message', '').strip().lower()

    # الردود الذكية والهزار 😄
    if not user_message:
        reply = "قولّي حاجه عشان أقدر أرد 😊"
    elif "السلام" in user_message or "hi" in user_message or "hello" in user_message:
        reply = "وعليكم السلام 👋، يوسف بوت العقارات في خدمتك!"
    elif "شقة" in user_message or "عقار" in user_message or "بيت" in user_message:
        reply = "🏠 عندنا شقق في التجمع، المعادي، ومدينة نصر! تحب أبعثلك التفاصيل؟"
    elif "السعر" in user_message:
        reply = "💰 الأسعار بتبدأ من 1,000,000 جنيه حسب المنطقة والمواصفات."
    elif "يوسف" in user_message:
        reply = "ايوه يا باشا! يوسف البوت تحت أمرك 😎"
    elif "شكرا" in user_message:
        reply = "العفو يا غالي 🌹 أي خدمة تانية؟"
    elif "هزار" in user_message or "ضحكني" in user_message or "نكتة" in user_message:
        reply = "😂 مرة واحد راح يشتري شقة قالوله السعر بالمتر، قالهم طب لو أقعد واقف؟"
    else:
        reply = "مش فاهمك أوي 😅، ممكن توضّح أكتر؟"

    return jsonify({"reply": reply})
