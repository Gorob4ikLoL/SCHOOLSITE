from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Головна сторінка
@app.route('/')
def index():
    return render_template('index.html')

# Сторінка "Онлайн-курси"
@app.route('/courses')
def courses():
    return render_template('courses.html')

# Сторінка "Лекції"
@app.route('/lectures')
def lectures():
    return render_template('lectures.html')

# Сторінка "Домашні завдання"
@app.route('/homework')
def homework():
    return render_template('homework.html')

# Сторінка "Відгуки студентів"
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/contact', methods=['POST'])
def contact():
    email = request.form.get('email')
    reason = request.form.get('reason')

    if email and reason:
        # Process the data (e.g., save to a database or send an email)
        print(f"Email: {email}, Reason: {reason}")
        return redirect(url_for('index'))  # Redirect to the main page after submission
    else:
        return "Error: Please fill in all fields."

if __name__ == '__main__':
    app.run(debug=True)
