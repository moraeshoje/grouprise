from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Recebe a atualização do Telegram
    data = request.json
    print(data)  # Aqui você pode processar os dados recebidos, como responder a mensagens

    # Aqui você pode adicionar a lógica para processar o webhook e enviar respostas ao Telegram
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
  
