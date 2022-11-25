import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="環境分析",layout="wide",initial_sidebar_state="auto")
#タイトル
st.title("ベジ・アビオ環境分析")
# データフレーム読み込み
st.sidebar.write("""## ファイルアップロード""")
uploaded_file = st.sidebar.file_uploader("分析したいファイルをアップロードしてください", type='csv')
if uploaded_file:
    @st.cache
    def readcsv():
        return  pd.read_csv(uploaded_file, encoding="shift-jis", index_col=[0], parse_dates=[0])
    df_readfile = readcsv()
    @st.cache
    def ex1():
        return df_readfile[df_readfile["温室"] == 1]
    @st.cache
    def ex2():
        return df_readfile[df_readfile["温室"] == 2]
    @st.cache
    def ex3():
        return df_readfile[df_readfile["温室"] == 3]
    @st.cache
    def ex4():
        return df_readfile[df_readfile["温室"] == 4]
    @st.cache
    def ex5():
        return df_readfile[df_readfile["温室"] == 5]
    @st.cache
    def ex6():
        return df_readfile[df_readfile["温室"] == 6]
    @st.cache
    def ex7():
        return df_readfile[df_readfile["温室"] == 7]
    @st.cache
    def ex8():
        return df_readfile[df_readfile["温室"] == 8]
    @st.cache
    def ex9():
        return df_readfile[df_readfile["温室"] == 9]

    df_ex1 =  ex1()
    df_ex2 =  ex2()
    df_ex3 =  ex3()
    df_ex4 =  ex4()
    df_ex5 =  ex5()
    df_ex6 =  ex6()
    df_ex7 =  ex7()
    df_ex8 =  ex8()
    df_ex9 =  ex9()

    #サイドバーの日付選ぶ
    st.sidebar.write("""
    # オプション設定
    以下のオプションから表示日数・温室を指定できます。
    """)
    st.sidebar.write("""## 表示日付・温室選択""")
    select_dates = st.sidebar.date_input('表示したい日付の選択',value=(df_ex1.index[0],df_ex1.index[-1]),min_value=df_ex1.index[0],max_value=df_ex1.index[-1])

    #ヘッダー
    st.header("温度・相対湿度・日射・CO2濃度のグラフ")

    #温室番号選ぶ
    listnum = ['1','2','3','4','5','6','7','8','9']
    stocks = st.sidebar.selectbox(label="温室番号の選択",
                options = listnum)

    # #カラムを選ぶ?
    # listcol = ['温度','相対湿度','日射','CO2濃度']
    # colstocks = st.sidebar.multiselect(label="カラムの選択",
    #             options = listcol,
    #             default=['温度','日射'])

    # if not colstocks:
    #     st.error('少なくとも1つカラムを選んでください。')

    if '1' in stocks:
        a = df_ex1
    if '2' in stocks:
        a = df_ex2
    if '3' in stocks:
        a = df_ex3
    if '4' in stocks:
        a = df_ex4
    if '5' in stocks:
        a = df_ex5
    if '6' in stocks:
        a = df_ex6
    if '7' in stocks:
        a = df_ex7
    if '8' in stocks:
        a = df_ex8
    if '9' in stocks:
        a = df_ex9

    #温室ごとグラフデータ定義
    a1 = go.Scattergl(x=a[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y= a['温度'] ,
                                marker_color='blue',
                                line_width=3,yaxis='y1',name='温度')
    a2= go.Scattergl(x=a[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=a['相対湿度'] ,
                                marker_color='red',
                                line_width=3,yaxis='y1',name='相対湿度')                         
    a3 = go.Scattergl(x=a[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y= a['日射'] ,
                                marker_color='green',
                                line_width=3,yaxis='y2',name='日射')               
    a4= go.Scattergl(x=a[select_dates[0].strftime("%Y-%m-%d"):select_dates[-1].strftime("%Y-%m-%d")].index,
                                y=a['CO2濃度'] ,
                                marker_color='orange',
                                line_width=3,yaxis='y2',name='CO2濃度')  

    layout = go.Layout(title=dict(text='<b>【比較グラフ】'),xaxis = dict(title = '日付'), font=dict(size=15),
              yaxis1 = dict(side = 'left', showgrid=False,range = [0, 110]),                            
              yaxis2 = dict(side = 'right', overlaying = 'y1', range = [0,900], showgrid=False),
              legend=dict(xanchor='left',yanchor='bottom',x=0.32,y=1.0,orientation='h'))

    
    fig = dict(data = [a1, a2, a3, a4],layout= layout)
    st.plotly_chart(fig,width=900,height=1200)

