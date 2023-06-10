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

def apply_exception(df: pd.DataFrame) :
    df_json=pd.read_json(build_path+"db_exception.json")

    def cell_yellow(value):
        return 'background-color: yellow'
    
    df_styled=df.style
    for index, row in df_json.iterrows() :    
        condition = row['category'] == df['category']
        for key,value in row['exception'].items():
            df.loc[condition,key] = value
            df_styled=df_styled.applymap(cell_yellow,subset=pd.IndexSlice[df.loc[condition,key].index, ['reason',key]]) # type: ignore

    df_styled.data=pd.merge(df_styled.data,df_json[['category','reason']],how='left') #columns 가 여러개일 때는 list로 넣어줘야함 # type: ignore
    df_styled.data.fillna('',inplace=True) # type: ignore

    return df_styled


app = Flask(__name__)

@app.route('/')
def display_dataframe():
    df=make_dataframe()
    df_s=apply_exception(df)
    return render_template('table.html',table=df_s.to_html(classes='df_final'),debug=True)

if __name__ == '__main__' :
    app.run(host='127.0.0.1', port=5000)