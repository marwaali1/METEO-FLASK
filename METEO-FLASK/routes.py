from flask import Flask, render_template
import getData


app=Flask(__name__)


@app.route("/")
def home():
   return render_template('home.html', dateLyouma=getData.dateLyouma2,lyouma=getData.Lyouma,dataMeteo=getData.dataMeteo,current_H=getData.current_H,Pb=getData.Pb,Pm=getData.Pm,current_M=getData.current_M)





    
