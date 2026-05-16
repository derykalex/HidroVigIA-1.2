from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>🌊 HidroVigIA</h1>
    <h2>Sistema Participativo de Monitoramento da Água</h2>
    <p>Projeto iniciado com sucesso no GitHub Codespaces.</p>
    <ul>
        <li>Cadastro de análises</li>
        <li>Controle de pH</li>
        <li>Registro de turbidez</li>
        <li>Monitoramento comunitário</li>
    </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
