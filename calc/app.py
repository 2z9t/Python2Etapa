from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    # Recebe os dados enviados pela interface
    dados = request.get_json()
    expressao = dados.get('expressao', '')
    
    try:
        # Avalia a expressão matemática de forma segura usando Python
        # O eval() é usado aqui estritamente para números e operadores básicos permitidos
        resultado = str(eval(expressao))
        return jsonify({'sucesso': True, 'resultado': resultado})
    except Exception:
        return jsonify({'sucesso': False, 'resultado': 'Erro'})

if __name__ == '__main__':
    app.run(debug=True)
