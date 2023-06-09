from flask import Flask, render_template
import os
import pandas as pd

build_path=os.path.dirname(os.path.abspath(__file__))+"\\database\\"
def make_dataframe() :

    df_main=pd.read_csv(build_path+"db_main.csv")
    
    df_sub_A_1=pd.read_csv(build_path+"db_sub_A_1.csv")
    df_sub_A_2=pd.read_csv(build_path+"db_sub_A_2.csv")
    df_sub_A_concat=pd.concat([df_sub_A_1,df_sub_A_2])
    df_merge=pd.merge(df_main,df_sub_A_concat,on="sub")

    return df_merge

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    df=make_dataframe() 
    return render_template('table.html',table=df.to_html())

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5000)