from flask import Flask, render_template, request

app = Flask(__name__)

# Liste für gespeicherte Schichten (nur im Arbeitsspeicher)
shifts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        day = request.form.get('day')
        time = request.form.get('time')

        if name and day and time:
            # Neue Schicht zur Liste hinzufügen
            shifts.append({'name': name, 'day': day, 'time': time})

    return render_template('index.html', shifts=shifts)

if __name__ == '__main__':
    app.run(debug=True)