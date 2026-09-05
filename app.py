from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Rota principal: Lê o arquivo index.html que está solto na mesma pasta
@app.route('/')
def home():
    with open('index.html', 'r', encoding='utf-8') as f:
        return f.read()

# Rota do CSS: Lê o arquivo style.css que está solto na mesma pasta
@app.route('/style.css')
def estilos():
    with open('style.css', 'r', encoding='utf-8') as f:
        return f.read(), 200, {'Content-Type': 'text/css'}

# Rota do Vídeo: Entrega o seu arquivo de vídeo local para o navegador
@app.route('/video-meu.mp4')
def servir_video():
    pasta_atual = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(pasta_atual, 'video-meu.mp4', mimetype='video/mp4')

if __name__ == '__main__':
    print("\n Servidor Iniciado com Sucesso no Tablet!")
    print(" Clique no botão verde 'Open in Browser' no canto inferior.\n")
    app.run(host='0.0.0.0', port=5000, debug=True)

