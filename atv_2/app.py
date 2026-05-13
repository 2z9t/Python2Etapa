from flask import Flask

app = Flask(__name__)

def exibicao():
    return '''
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Currículo</title>
        <style>
            :root {
                --white: #FFF;
                --blue: #0077ff;
                --black: #000;
                --w-32: 320px;
            }

            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            h1, h3, span {
                text-align: justify;
                white-space: wrap;
            }

            body {
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100vw;
                height: 100vh;
            }

            main {
                display: flex;
                flex-direction: column;
                width: var(--w-32);
                height: auto;
                gap: 1rem;
            }

            nav {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                padding: 0.1rem;
                border-radius: 0.5rem;
                border: 2px solid var(--black);
            }

            nav:hover {
                background-color: var(--black);
                color: var(--white);
                cursor: pointer;
            }

            section {
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: flex-start;
                gap: 1rem;
            }

            .fdiv {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(2, 1fr);
                width: 100%;
                gap: 0.1rem;
            }

            .cdiv {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                width: 100%;
                gap: 0.1rem;
            }

            button {
                padding: 0.1rem 0;
                border: 1px solid var(--black);
                border-radius: 0.1rem;
                outline: none;
                cursor: pointer;
            }

            button:hover {
                background-color: var(--black);
                color: var(--white);
            }

            button:active {
                background-color: var(--blue);
                filter: brightness(1.5);
            }

            #ingles, #github {
                align-self: center;
            }
        </style>
    </head>
    <body>
        <main>
            <nav>
                <h1>Currículo</h1>
                <span>Davi Rodrigues Fontana</span>
            </nav>
            <section>
                <h3>Sobre mim:</h3>
                <span>Meu nome é Davi, tenho 17 anos e estou atualmente no terceiro ano do colégio técnico COTEMIG</span>
                <h3>Conhecimentos:</h3>
                <div class="fdiv">
                    <button>HTML</button>
                    <button>CSS</button>
                    <button>JS</button>
                    <button>C#</button>
                    <button>PHP</button>
                    <button>MySQL</button>
                </div>
                <span id="ingles">Inglês: <strong>Intermediário</strong></span>
                <h3>Contato:</h3>
                <div class="cdiv">
                    <button>(31) 99999-9999</button>
                    <button>meuemail@gmail.com</button>            
                </div>
                <h3 id="github">Github: fontana</h3>
            </section>
        </main>
    </body>
    </html>
    '''

@app.route('/')
def inicio():
    return exibicao()

if __name__ == '__main__':
    app.run(debug=True)