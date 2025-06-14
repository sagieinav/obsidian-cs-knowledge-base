## 1 מטלה 2 - עבודה עם Gradle ובדיקות יחידה

#### 1.1.1 **1. היכנסו לשירותי ה-GitHub וצרו חשבון ומאגר קוד משותף**

א. על מנת ששני (או יותר) חברי הצוות יוכלו לשתף קוד ביניהם ועם מרצה הקורס, עליכם לפתוח מאגר קוד **פרטי משותף** (Private Repository) בסביבת הענן של GitHub, עליכם להתחיל את הפרויקט מששכול באמצעות הפקודה clone, מהפרויקט הנמצא בכתובת הכתובה מטה, על פי הפעולות הבאות:

1. יש ליצור תיקיה חדשה עבור הפרויקט בסביבה העבודה שלכם, ולהכנס אליה.

2. יש לשכפל לתיקיה זו באמצעות הפקודה git clone את הפרויקט שנכתב על ידי המרצה, תוך שימוש בפקודה:
`git clone https://github.com/TomCo2210/25B-10142-Gradle_UnitTesting_Assignment.git`

3. יש לשנות את מאגר הקוד המרוחק (remote repository) ולשנותו למאגר הקוד שיצרתם ב- GitHub, באמצעות הפקודות הבאות:
`git remote remove origin` 
`git remote add origin https://github.com/your-username/your-repo.git`

ב. יש לשתף את המאגר עם השותפים לקבוצה, כדי לעשות זאת יש להיכנס להגדרות המאגר ותחת תפריט Collaborators להוסיף את שאר חברי הצוות בעזרת לחיצה על Add people.

ג. על מנת להתחבר למשתמש בסביבת vLab הייעודית, יש להנפיק Token חיבור עבור המשתמש האישי שלכם בשרותי GitHub ולהתחבר בסביבת הטרמינל, באמצעות הפקודות הבאות:
`git config --global user.name "Your Name"`
`git config --global user.email "your_email@example.com"`
**שימו לב שיש להחליף את הפרטים בפרטי החשבון שלכם.**
כאשר תדרשו להקיש את הסיסמה – עליכם יהיה להכניס את ה-Token שהנפנפם קודם לכן.

#### 1.1.2 **2. כתיבת בדיקות היחידה**

א. על כל חבר צוות, לבחור 3 פונקציות (שונות) מתוך קובץ ה-App הנתון.

ב. יש לכתוב בדיקות יחידה תוך שימוש בפונקציות Assert השונות, בקובץ AppTest, כפי שנלמד בכיתה.

#### 1.1.3 **3. הכנת התרגיל להגשה באמצעות GitHub**

א. יש להכין קובץ Readme.md במאגר הקוד של התרגיל בסביבת GitHub. בקובץ זה יש לפרט מי הם חברי הצוות, מה הפונקציות שבחר כל אחד מהחברים לבדוק, ומה על המשתמש לעשות על מנת להריץ כל הבדיקות שנכתבו – החל משלב שכפול הפרויקט אליכם ועד שלב ההרצה בפועל.

ב. בסיום כתיבת התרגיל, יש לשתף בגישה למאגר הקוד כמו שהוסבר בסעיף 1.ב. את מרצה הקורס בעזרת שם המשתמש Tomco2210.

ג. בסביבת המודל נפתחה עבורכם תיבת הגשה ייעודית המותאמת על פי הצוותים שבחרתם, על ראש הצוות להגיש את התרגיל באמצעות הדבקת הקישור למאגר הקוד בתיבת ההגשה.