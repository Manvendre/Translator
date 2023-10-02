from flask import Flask,render_template,request
import gtts
import os
import playsound
from googletrans import Translator

translator = Translator()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        txt = request.form.get('textt')
        lang = request.form.get('lang')

        if lang == 'English':
           lang='en'
        elif lang == 'Hindi':
           lang='hi'
        elif lang == 'German':
           lang='de'
        elif lang == 'Russian':
           lang='ru'
        elif lang == 'Spanish':
           lang='es'
    
        
        mytext=translator.translate(txt, dest=lang)

        myobj = gtts.gTTS(mytext.text, lang=lang)

        myobj.save("welcome.mp3")

        playsound.playsound("welcome.mp3")

        os.remove("welcome.mp3")

    return render_template("index.html")
