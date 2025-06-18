from flask import Flask, render_template, request, jsonify
from openai import OpenAI

client = OpenAI(api_key='тут должен быть ключ OpenAI')

app = Flask(__name__, static_folder='static', template_folder='templates')
SYSTEM_PROMPT = """
тут описание для GPT-4o-mini, например:
Ты - умный помощник, который отвечает на вопросы пользователей. Твоя задача - давать точные и полезные ответы, основываясь на предоставленной информации. Будь вежливым и дружелюбным.
"""
chat_history: list[dict] = []
@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    user_message = data.get('message', '').strip()
    if not user_message:
        return jsonify({'reply': 'Сообщение не может быть пустым!'}), 400
    chat_history.append({'role': 'user', 'content': user_message})
    if len(chat_history) > 10:
        del chat_history[0:len(chat_history) - 10]
    try:
        resp = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'system', 'content': SYSTEM_PROMPT}] + chat_history
        )
        bot_reply = resp.choices[0].message.content.strip()
        chat_history.append({'role': 'assistant', 'content': bot_reply})
        return jsonify({'reply': bot_reply})
    except Exception as e:
        return jsonify({'reply': f'Ошибка при вызове OpenAI: {e}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)