# Ten_Yad
A gaimified social platform for volunteering and asking for help. </br>
Project Ten Yad - by Israel Avihail, Ofir Golan, Daniel Dahan, Matan Fadida

Live Website Link:
https://bilbisli.pythonanywhere.com/

הנחיות להרצה:
סביבת הרצה PyCharm.
פתיחת פרוייקט עם סביבה וירטואלית Virtualenv.
לוחצים על Terminal ואז מתחילים בתקנה:
1. בעזרת הפקודה pip install virtualenv.
2. נפתח תיקייה חדשה בשם venv בכתיבה virtualenv venv.
יבוא הקבצים מהגיט:
ניגש לתיקייה venv במערכת ההפעלה וניצור שם תיקייה חדשה בשם project ולשם נשים את הקבצים של התוכנית.
לאחר מכן נחזור לפרוייקט ב PyCharm ושם נחזור ל-Terminal וניגש לתיקייה Scripts בצורה הזאת cd venv/Scripts נלחץ enter ואז נרשום activate כך הפעלנו את הסביבה הוירטואלית.
ואז נחזור לתיקייה venv בעזרת cd.. בצורה הזאת.
ונתקין את החבילות הבאות על ידי הפקודות הבאות:
pip install six
pip install django-crispy-forms
pip install django-filter
pip install python-dotenv
pip install whitenoise
pip install python-dotenv
ואז נחזור לתיקיית השורש project וניצור קובץ מסוג מסמך טקסט ואז נגדיר את מפתח האבטחה ואימייל האדמין בתוכו לדוגמא:
SECRET_KEY = "insert a key of 50 characters that will be your security key
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "admin@gmail.com"
EMAIL_HOST_PASSWORD = "admin_password"
ALLOWED_HOSTS = ["bilbisli.pythonanywhere.com", ]
לאחר מכן נדרש את כתובת האתר כמארח מורשה
ונשנה את שמו כולל הסיומת txt. ל - env. ונמקם אותו בשורש הפרוייקט (ישר מתחת לסביבה איפה שהתיקייה TenYad ו-gitignore).
ואז נחזור ל-Terminal ונאתחל את בסיס הנתונים על ידי הפקודות הבאות:
python manage.py makemigrations
python manage.py migrate

ואז ניגש לתיקייה שכוללת את הקובץ manage.py בצורה הבאה:
cd project/Ten_Yad/TenYad/ten_yad
ונרים את השרת בעזרת הפקודה:
python manage.py runserver
