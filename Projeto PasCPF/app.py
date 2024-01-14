from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    options = {
        'length': 12,
        'uppercase': False,
        'lowercase': False,
        'numbers': False,
        'symbols': False
    }

    if request.method == 'POST':
        options['length'] = int(request.form.get('length', 12))
        options['uppercase'] = 'uppercase' in request.form
        options['lowercase'] = 'lowercase' in request.form
        options['numbers'] = 'numbers' in request.form
        options['symbols'] = 'symbols' in request.form

        password_characters = ''
        if options['uppercase']:
            password_characters += string.ascii_uppercase
        if options['lowercase']:
            password_characters += string.ascii_lowercase
        if options['numbers']:
            password_characters += string.digits
        if options['symbols']:
            password_characters += string.punctuation
        if password_characters:
            password = ''.join(random.choice(password_characters) for _ in range(options['length']))
        else:
            password = 'Selecione pelo menos um conjunto de caracteres.'

    return render_template('gerar_senha.html', password=password, options=options)

if __name__ == '__main__':
    app.run(debug=True)