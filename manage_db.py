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

    df_sub_B_1=pd.read_csv(build_path+"db_sub_B_1.csv")
    df_sub_B_2=pd.read_csv(build_path+"db_sub_B_2.csv")
    df_sub_B_3=pd.read_csv(build_path+"db_sub_B_3.csv")
    df_sub_B_concat=pd.concat([df_sub_B_1,df_sub_B_2,df_sub_B_3])
    df_merge=pd.merge(df_merge,df_sub_B_concat,on="sub2")
    return df_merge

app = Flask(__name__)

@app.route('/')
def display_dataframe():
    df=make_dataframe() 
    return render_template('table.html',table=df.to_html(classes='df_final'),debug=True)

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5000)