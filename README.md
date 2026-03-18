# Calculator EGE — API + Front (Flask)

Небольшой сервис для оценки шансов поступления:
- парсит проходные баллы (сейчас стабильно работает МИФИ / MEPhI)
- отдаёт данные через API
- отображает UI (HTML/CSS/JS) + расчёт вероятности

## Быстрый старт

### 1) Установка
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt

### Быстрый старт
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python scripts/update_database.py
python run.py