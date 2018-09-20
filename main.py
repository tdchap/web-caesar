from flask import Flask, request

app = Flask(__name__)
app.config ['DEBUG'] = True
form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form action="/" method="POST">
          <label for="caesar_text_input">Input text to be encrypted:</label>
          <input id="caesar_text_input" type ="text" />
          <textarea id="caesar_text_input" name = "caesar_text_input" rows="3" cols="60">
    </body>
</html>
"""

@app.route("/")
def index():
    return form


app.run()