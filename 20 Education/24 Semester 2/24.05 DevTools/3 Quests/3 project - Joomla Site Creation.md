> [!toc] *Table of Contents*
> ```toc
> ```
## 1 שלב ההתארגנות בצוות עבודה

את הפרויקט המסכם יש לבצע בצוותים בני 2-3 משתתפים.
לכל צוות יש ראש צוות ותפקידו להגיש את תוצרי הפרויקט באמצעות תיבת ההגשה שתפתח לכם במודל.
על ראשי הצוותים בלבד לפרסם בפורום למרות הצוותים - עד יום שישי, 14 ביוני בשעה 23:59 את פרטי חברי הצוות.

*   ראש הצוות יפרסם הודעה בפורום עם שמות חברי הצוות ומספרי הזהות שלהם.
*   סטודנטים וסטודנטיות שמחפשים צוות להצטרף אליו, יכולים לפרסם הודעה לחיפוש צוות בפורום.
*   לאחר סגירת מועד ההרשמה - הסטודנטים יצורפו לקבוצות בהתאם למה שנכתב בפורום, ותפתח עבורם האפשרות להגיש את המטלה.

<font color="red"><u>**סטודנטים שלא יצטרפו לצוות - לא יוכלו להגיש את הפרויקט!**</u></font>

## 2 תיאור הפרויקט

על כל צוות להקים אתר Joomla.
Joomla היא מערכת לניהול תוכן המאפשרת בניית עמודי אתרים, היא אחד השירותים הנפוצים בעולם לאתרי בלוג, לצד וורדפרס ודרופאל.
לצידה של Joomla, על מנת לשמור את התכנים שיכתבו באתר, יש לשמור את הנתונים בבסיס נתונים של MySQL.
את שני חלקי הפרויקט יש להפעיל באמצעות שירות ה-Docker.

### 2.1 חלק ראשון: התקנות בסיסיות באמצעות Docker

1.  **הקמת סביבת Docker לעבודה עם מסד נתונים.**
    א. על מנת ששני (או יותר) קונטיינרים יכירו האחד את השני, יש להגדיר רשת עבורם באמצעות הפקודה: `docker network create <name>`

2.  **עליכם להתקין באמצעות Docker בסיס נתונים של MySQL.**
    א. יש להיעזר בהוראות ההקמה של בסיס הנתונים בדף הרשמי של בסיס הנתונים באתר התמונות הרשמי של Docker.
    התמונה של התמונה של MySQL נמצאת בכתובת: [https://hub.docker.com/_/mysql](https://hub.docker.com/_/mysql)
    ב. לתשומת ליבכם, הקמת בסיס הנתונים מתבצעת על הרצת פקודת `docker`, בדומה לאופן שבו הקמנו בסיס נתונים על גבי מכונת Linux בשיעורים במהלך הסמסטר.
    ג. עליכם לוודא כי הגרסה של בסיס הנתונים היא הגרסה העדכנית ביותר של Image.
    הדמיון להורדה מ-Docker Hub: `docker pull mysql:latest`
    ד. עליכם לוודא כי בסיס הנתונים חושף למכונה הלינוקס שעליה הוא רץ את Port ברירת המחדל עבור בסיס נתונים. (3306 - MySQL).
    ה. עליכם לוודא כי הסיסמא של משתמש העל (root) של בסיס הנתונים היא:
    `my-secret-pw`
    לתשומת לבכם: נפחו של Image של בסיס הנתונים של MySQL הוא 632 מגה.
    שימו לב על מנת להריץ את הפקודה כראוי - מומלץ להשתמש בשני משתני מערכת כדי להגדיר image ו-container name-ים, ומחרוזת איתם בסיס הנתונים ירוץ, כנכתב בעמודי התיעוד של השירות. (משתנים עבור שם בסיס הנתונים, שם המשתמש והסיסמה עבור חיבור לבסיס הנתונים וכו')

3.  **עליכם להתקין את יישום Joomla באמצעות Docker.**
    א. יש להיעזר בהוראות ההקמה של Joomla, יישום הכתוב בשפת PHP ובשפת JavaScript, שוות חשית לאתרי בלוג, הנמצאים בדף הרשמי של שירות זה באתר התמונות הרשמי של Docker.
    Repository של התמונה של Joomla נמצא בכתובת: [https://hub.docker.com/_/joomla](https://hub.docker.com/_/joomla)
    ב. לתשומת לבכם: הריצו את ה-Docker של Joomla כך שייחשף על מכונת ה-Linux שלכם ל-port שמספרו 8080, הפונה ל-port 80 המצוי בתוך הקונטיינר באמצעות הוספת הפקודה ההרצה של Docker את הפורטים: `p8080:80`

    לתשומת לבכם: נפחו של Image של Joomla הוא כ-750 מגה.
    שימו לב כי היישום מתבצע בצורה שונה מגרסתו הרגילה, יש לדאוג ל-Volumes בהתאם, על מנת להריץ את השירות כראוי - מומלץ להשתמש בהוראות הכתובות בעמוד השירות של Joomla.

**הערות:**

*   בפקודת ההרצה יש לזכור לחבר את הקונטיינרים לאותה הרשת אותה הגדרתם בסעיף 1.
*   במידת הצורך יש להגדיר את משתני הסביבה בשורת ההרצה של כל אחד מהקונטיינרים.
*   במידת הצורך יש להגדיר את ה-Volumes עבור כל אחד מהקונטיינרים בשורת ההרצה של כל אחד מהקונטיינרים.

### 2.2 חלק שני: קונפיגורציה של Joomla

1.  **בדיקה רציפה של הקונטיינרים**
    ראשית, כדאי לבדוק שהקונטיינר של Joomla אכן רץ.
    הפעילו פקודה של Docker שמציגה את כל הקונטיינרים הרצים וודאו שאתם רואים גם את הקונטיינרים שהפעלתם.

2.  **קונפיגורציה של Joomla באמצעות דפדפן.**
    יתכן ויהיה צורך לבצע פעולות נוספות על מנת להקים אתר Joomla.
    על מנת להיכנס לממשק של Joomla ניתן לגשת אל הכתובת [http://localhost:8080](http://localhost:8080)
    על מנת להיכנס לממשק המנהל יש להיכנס באמצעות הקישור הבא: [http://localhost:8080/administrator](http://localhost:8080/administrator)
    לתשומת ליבכם: ייתכן שלצורך התקנת Joomla באותו אתר שאתם מקימים כעת, כדי למנוע תקלות הנובעות משינויי כתובות IP במכונות שבהן אתם עובדים, מומלץ להגדיר בקישור את ה-Name של המכונה שלכם כ-`localhost`, אם כי זה עלול להגביל אתכם מלגשת לאתר ממחשבים אחרים.
    אם תתחברו לשרת עם ה-HOSTNAME האמיתי של מכונת ה-LINUX או עם כתובת ה-IP שלו, תוכלו להתחבר אליו גם ממחשבים אחרים.
    אולם, אם אתם עובדים עם מכונות וירטואליות, כמו המכונות הוירטואליות של אפקה, יתכן שתצטרכו להקים מחדש אתר בכל פעם אתם עולים על הכלי.
    לצורך בירור כתובת ה-IP או ה-HOSTNAME של מכונת ה-LINUX שלכם, תוכלו לחפש פקודות LINUX נפוצות שעושות זאת.

3.  **הגדרות כלליות**
    *   במידת הצורך עליכם להגדיר את חיבור השירות לבסיס הנתונים באמצעות שימוש בשם הקונטיינר שהוגדר עבור בסיס הנתונים, שם המשתמש והסיסמה שלו.
    *   עליכם ליצור חשבון מנהל לאתר Joomla שלכם עם שם המשתמש `demoadmin` והסיסמה `secretpass`.
    *   בנוסף, עליכם להגדיר חשבונות משתמשים עבור כל אחד מחברי הצוות.

### 2.3 חלק שלישי: הרצה של Joomla ויצירת תכנים ראשונית

1.  גלשו לאחר ה-Joomla שהקמתם, בכתובת: [http://localhost:8080](http://localhost:8080).
    א. ודאו שאתם אכן רואים את הדף הראשי של האתר שהקמתם.
    ב. עמוד זה ישמש אתכם לראות אם התכנים שיעלו תוצגועד בראוי באתר.

2.  גלשו לממשק הניהול של אתר Joomla שהקמתם בכתובת: [http://localhost:8080/administrator](http://localhost:8080/administrator).
    בצעו LOGIN לאתר, והוסיפו תכנים:
    *   ראשית ישתמשו במשתמש המנהל שהוגדרתם על מנת ליצור משתמשים עבור כל אחד מחברי הצוות.
    *   לאחר חיבור כל אחד מחברי הצוות, על כל חבר בצוות לבצע התחברות בעצמו ולעזרת ממשק הניהול ליצור "מאמרים" חדשים, עבור ערכי מילון המונחים שהוגדרו במילון המונחים במודל הקורס.

### 2.4 חלק רביעי: גיבוי המידע ובסיס הנתונים

**עבור MySQL:**
נדרשתם התקנת יישום MySQLdump:
הפעילו את הפקודות הבאות לביצוע ההתקנה:

```bash
sudo apt update
sudo apt install MySQL-client-core-8.0
```

1.  **בצעו גיבוי לבסיס הנתונים**
    הפעילו את הפקודה לביצוע הגיבוי, על ה-Container המריץ את בסיס הנתונים שלכם (ההדרו בהתאם לשם ה-Docker איך לעשות זאת):

    ```bash
    docker exec $CONTAINER_NAME sh -c 'exec mysqldump --all-databases -uroot -p$MYSQL_ROOT_PASSWORD' | gzip > my-joomla.backup.sql.gz
    ```

    שימו לב שיש להחליף את משתני הסביבה בפרטים כפי שהוגדר בבסיס הנתונים בחלק הראשון בפרויקט.

**המשך כללי:**

1.  בדקו האם צריך לבצע גיבוי לקבצי הקונטיינר של Joomla שלכם
    אם עשיתם שינויים ויזואליים באתר, ישנה אפשרות טובה ליצירת תיקיה משותפת אליה יש לטעון את קבצי המידע בבסיס Joomla על מנת לגבות ולשחזר בצורה מהירה, ללא צורך בהקמתה מחדש. (Volumes)

### 2.5 חלק חמישי: שחזור גיבוי בסיס הנתונים

1.  לאחר הגיבוי - יש לבדוק שכל הנתונים תקינים וניתן לשחזר את האתר בצורה פשוטה.
2.  היכנסו למכונת Linux אחרת, ובצעו את הפעולות המשחזרות את הנתונים אל בסיס הנתונים של הקונטיינר של בסיס הנתונים, בדומה למה שבוצע בחלק הרביעי.
    עבור MySQL:
    על ידי השימוש בפקודה הבאה:

    ```bash
    docker exec $CONTAINER_NAME sh -c 'exec mysqladmin -u$MYSQL_USER -p$MYSQL_PASS create $DB_NAME'
    gunzip < "$BACKUP_FILE" | docker exec -i "$CONTAINER_NAME" sh -c 'exec mysql -u$MYSQL_USER -p$MYSQL_PASS --force $DB_NAME'
    ```

    פרושת נתוני הגיבוי המגובים אל Docker:
    עבור MySQL:
    שימו לב שיש להחליף את כל משתני ה-$ בערכים הדרושים במקום כפי שהוגדר בבסיס הנתונים בחלק הראשון בפרויקט.
3.  בעת כדאי לעשות restart לשירות ה-Joomla כדי שהשינויים יהיו תוקף.
4.  בדקו שכל המידע שוחזר כראוי.
5.  נקו את המכונה וסיימו את עבודתכם:
    *   יש למחוק את הקונטיינר של Joomla.
    *   יש למחוק את הקונטיינר של בסיס הנתונים.
    *   יש למחוק את התמונות ההרצה של Docker.
    *   יש למחוק את ה-Volumes שיצרו.

### 2.6 חלק שישי: כתיבת סקריפטים

1.  את כל השלבים הקודמים, ניתן לבצע באופן אוטומטי.
2.  עליכם לכתוב סקריפטים להקים את התשתית של Docker.
    א. יצירת network פנימי לעבודה של כמה קונטיינרים יחד.
    ב. הורדה והרצה של כל אחד מהקונטיינרים.
    ג. יש להוסיף הודעות מתאימות למשתמש במידת הצורך.
3.  עליכם לכתוב סקריפט גיבוי בשם backup.sh, שתפקידו לגבות בסיס הנתונים, הקבצים הרלוונטיים מתוך ה-Volumes שהוגדרו (אם הוגדרו כאלה).
    הסקריפט יציג את כל המידע ויציג למשתמש הודעות מתאימות במידת הצורך.
4.  עליכם לכתוב סקריפט שחזור בשם restore.sh, שתפקידו לשחזר את כל המידע, את המידע הסקריפט יקח מקובץ הגיבוי שהוגדר בסעיפים הקודמים. (ניתן להגדיר שהסקריפט ימשוך באמצעות פעולות git מה-Repository שהוגדר עבור הפרויקט בשירות שהתבחרתם).
    הסקריפט יפרט את כל המידע ויציג למשתמש הודעות מתאימות במידת הצורך.
5.  עליכם לכתוב סקריפט לניקוי בשם cleanup.sh, שתפקידו לנקות את כל הקבצים שהוגדרו במערכת עבור הפרויקט ולהשאיר את סביבת העבודה כמו שהייתה לפני שהתחלנו את הכל.

### 2.7 חלק שביעי: שמירת הגיבויים ב-Git

1.  את קבצי הגיבוי שיצרתם - יש להעלות ל-Repository שיתבחרתם git ב-GitHub או BitBucket.
2.  את קבצי הפרויקט, קבצי הגיבוי, קבצי Docker-compose (אם כתבתם) - יש להעלות לאותו Repository.
3.  יש לכתוב עבור הפרויקט קובץ Readme.md ולצרף ל-Repository.
    הקובץ לכלול:
    א. מי אתם.
    ב. מה שנדרשתם לעשות.
    ג. מה עשיתם.
    ד. באיזה טכנולוגיות השתמשתם.
    ה. מדריך Step-by-Step פשוט איך לשחזר את האתר שלכם - החל משלב clone של ה-Repository, פתיחת האתר, הגדרתו וכל שלב שביצעתם בדרך, ועד שלב ניקוי סביבת העבודה ופינוי כל המידע ממכונת ה-Linux.
    ו. כל מידע נוסף שיועיל לסייע למשתמשים מה עשיתם.
4.  את הלינק ל-Repository על ראש הצוות להעלות למודל למערכת ההגשה, יש לדאוג שה-Repository אינו מוגדר כפרטי, או לחילופין, לתת הרשאה למרצה הקורס כפי שנלמד ונעשה בתרגילי הבית.

**בהצלחה!**

---
💡 **טיפים טכניים:**

*   ודאו תמיד לבדוק את סטטוס הקונטיינרים שלכם באמצעות פקודות `docker ps -a`.
*   שימוש ב-Docker Compose יכול לפשט מאוד את תהליך ההקמה והניהול של מספר קונטיינרים.

---
