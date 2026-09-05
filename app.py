from flask import Flask, send_from_directory
import os

app = Flask(__name__)

# Rota principal (Home): Lê o arquivo index.html que está solto na mesma pasta
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
    # Configuração de porta dinâmica (obrigatória para servidores como o Render)
    # Se o Render não definir uma porta, o sistema usa a porta padrão 5000 do Codespaces
    porta = int(os.environ.get("PORT", 5000))
    
    print(f"\n Servidor Iniciado com Sucesso!")
    print(f" Rodando na porta: {porta}")
    print(" Pronto para funcionar no Codespaces ou no Render.\n")
    
    app.run(host='0.0.0.0', port=porta, debug=True)
