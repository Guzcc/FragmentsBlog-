from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Simulación de base de datos en memoria
users = {}
fragments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_number = request.form.get('user_number')
        content = request.form.get('content')
        if user_number and content:
            fragments.append({'user': user_number, 'content': content})
        return redirect(url_for('index'))
    return render_template_string("""
        <html>
        <head><title>Fragmentos</title></head>
        <body>
            <h1>Fragmentos</h1>
            <form method="post">
                Número de usuario: <input type="text" name="user_number"><br>
                Fragmento: <br><textarea name="content" rows="4" cols="50"></textarea><br>
                <input type="submit" value="Publicar">
            </form>
            <hr>
            {% for frag in fragments %}
                <p><b>{{ frag.user }}</b>: {{ frag.content }}</p>
            {% endfor %}
        </body>
        </html>
    """, fragments=fragments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
