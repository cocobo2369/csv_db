from flask import Flask, render_template
import os
import pandas as pd

build_path=os.path.dirname(os.path.abspath(__file__))+"\\database\\"
def make_dataframe() :

    df_main=pd.read_csv(build_path+"db_main.csv")

    return df_main

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    df=make_dataframe() 
    return render_template('table.html',table=df.to_html())

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5000)