from flask import Flask, render_template, request

app = Flask(__name__)

def shifty_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift_amount) % 26 + base)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        encoded_text = shifty_cipher(text, shift)
        return render_template('index.html', encoded_text=encoded_text, original_text=text, shift=shift)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)