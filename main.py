from flask import Flask, request
from caesar import rotate_string


    
    

app = Flask(__name__)
app.config ['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/" method="POST">
          <label for="caesar_text_input">Input text to be encrypted:</label>
          <textarea id="caesar_text_input" name ="caesar_text_input" type="text" rows="3" cols="60">{Field}</textarea>

          <label for="rot">Rotation amount:</label>
          <input id="rot" type ="text" name ="rot" rows="1" cols="2" value = 0 >

          <input type="submit" value="Caesar me timbers">
        </form>

    </body>
</html>
"""
#if len(caesar_textttttt) == 0
     #return
@app.route("/")
def index():
    return form.format(Field='')

@app.route("/", methods=['POST'])


def encrypt():
    caesar_text = request.form['caesar_text_input']
    rot=request.form['rot']
    rotate_amount = int(rot)
    caesar_encrypted_text=''
    caesar_encrypted_text =  caesar_encrypted_text + rotate_string(caesar_text,rotate_amount)
    return form.format(Field= caesar_encrypted_text)

app.run()

