from flask import Flask, render_template

# Inicializa o aplicativo Flask
app = Flask(__name__, template_folder="modelos")

# Rota principal
@app.route('/')
def home():
    return render_template("index.html")

# Execução do sistema
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",   # Permite acesso externo no Codespaces
        port=5000,        # Porta padrão
        debug=True        # Modo desenvolvedor
    )
