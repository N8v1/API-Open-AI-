# 💬 Веб-чат с ИИ на Flask + OpenAI

Интерактивный веб-чат-бот на Flask с возможностью входа через Google, почту или анонимно. Подключается к ChatGPT API и поддерживает работу с моделью GPT-4o (о4-mini). Интерфейс построен на HTML/CSS, JS.

---

## 🚀 Возможности

- 🔐 Вход через Google, почту или без регистрации
- 🧠 Общение с ChatGPT API (модель GPT-4o/mini)
- 🌐 Локальный веб-интерфейс на Flask

---

## 🛠 Технологии

- Python, Flask
- HTML / CSS / JavaScript
- OpenAI Chat API

---

## 🔧 Как запустить

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/nikita777/chatbot-flask-ai.git
   cd chatbot-flask-ai
2. Установите зависимости:
pip install -r requirements.txt
Вставьте ваш API-ключ OpenAI в .env файл:
OPENAI_API_KEY=ваш_ключ
3. Запустите приложение:
python app.py

![Снимок экрана 2025-06-18 201122](https://github.com/user-attachments/assets/a8e16425-4584-4dbe-8501-a94a38041dee)

Видео:
https://youtu.be/yiilXn7Czu0

📌 Примечания
По умолчанию используется модель GPT-4o-mini.

Вход без регистрации работает в режиме гостя (сессия временная).

Надо будет свое видое указать путь в коде если оно нужно.
