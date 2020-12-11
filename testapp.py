from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
            'card-age.html',
            username='Keiji',
            age=19,
            email='keiji@example.com')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

