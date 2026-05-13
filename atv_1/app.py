from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return '''
    <h1>Decorator</h1>
    <span>O uso principal dos decorators no Flask é definir <br> rotas (mapear URLs para funções Python) e adicionar <br> comportamentos extras a essas funções de forma <br> limpa e reutilizável, como autenticação ou manipulação <br> de requisições, sem alterar o código original. <br> O decorator @app.route() é o mais comum, associando <br> uma URL a uma view function.</span>
    '''

if __name__ == '__main__':
    app.run(debug=True)