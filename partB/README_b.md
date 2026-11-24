# אבן נייר ומספריים - התרגיל - חלק ב'
מקווים שאתם לא נבהלים מהקוד שמוצג בפניכם כי המשימה שלכם כעת היא

להמשיך את הקוד שקיבלתם כך שיתקבל הפלט הנדרש.

באפשרותכם להוסיף ולממש כל מחלקה או פונקציה נוספת שיעזרו לכם להגיע לפתרון.


### הנחיות
- המתודה `rules_for()`: מקבלת מהלך ומחזירה את החוקים שלו (`rock: beats scissors | loses to paper`).
- אם המהלך לא קיים במשחק, `rules_for` מחזירה `invalid move: ` ואת הצורה (`invalid move: banana`).
- המשחק עצמו (`play()` ו-`score()`) עובד כמו קודם.
- אסור שהתכנית תקרוס


סיימתם כש-`python main_b.py` מדפיס:

```text
rock: beats scissors | loses to paper
paper: beats rock | loses to scissors
invalid move: banana
scissors beats paper
scissors: beats paper | loses to rock
Score: 1-0
```

#### שימו לב - על הקוד להיות קריא ככל הניתן, גנרי, ושומר על עקרונות הSOLID כך שכל אדם אחר שיסתכל על הקוד שלכם יוכל להבין אותו בקלות ולהרחיב אותו.