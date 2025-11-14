import os
from dotenv import load_dotenv

# تحميل القيم من ملف .env
load_dotenv()

class Config:
    # إعدادات Twilio
    TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
    TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
    TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

    # قاعدة البيانات
    DATABASE_NAME = "yosif.db"  # هنا الاسم الرسمي لملف قاعدة البيانات
