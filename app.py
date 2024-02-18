from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None

    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        usm_id = request.form.get('usm_id')
        usm_email = request.form.get('usm_email')

        # Validate USM ID
        if not (usm_id and re.match(r'^[Ww]\d{2}\d{6}$', usm_id)):
            error = 'Invalid USM ID format. Please use W or w followed by 10 digits.'

        # Validate USM Email
        if not (usm_email and re.match(r'^[a-zA-Z0-9._%+-]+@usm\.edu$', usm_email)):
            error = 'Invalid USM Email format. Please use user@usm.edu.'

    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
