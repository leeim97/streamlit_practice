import streamlit as st
import pandas as pd
import seaborn as sns

#1) iris 데이터셋을 데이터프레임으로 표시
df = sns.load_dataset('iris')
st.dataframe(df)

# 2) multiselect를 사용하여 품종(species)을 선택하면, 해당 품종의 데이터에 대한 데이터프레임으로 표시
species3 = st.multiselect('품종 선택',
                         options =['setosa', 'versicolor', 'virginica'])


st.data_editor(df[df['species'].isin(species3)])







# 3) 품종을 제외한 4가지 컬럼을 radio 요소를 사용하여 선택하면
#   선택한 컬럼에 대한 히스토그램 그리기(matplotlib)

selected = st.radio(
    '한가지를 고르시오',
    ['sepal_length','sepal_width','petal_length','petal_width'],

)
import matplotlib.pyplot as plt

fig,ax = plt.subplots()

ax.hist(df[selected])
st.pyplot(fig)




# 2. kor_news 데이터셋을 이용
#  분류의 대분류 기준을 선택하면 해당 분야의 주요 키워드 20위에 대한 bar chart 표시

name = st.radio(
    '분야를 고르시오',
    ['지역','경제','사회','정치','문화','IT_과학','스포츠','국제','미분류']
)


df = pd.read_excel('data/kor_news_240326.xlsx')


df['대분류']= df['분류'].str.split('>').str[0]
data = pd.DataFrame(df['대분류'].value_counts())

from konlpy.tag import Okt
from collections import Counter

df['대분류'] = df['분류'].str.split('>').str[0]


def make_df(df, name):
    titles = df[df['대분류'] == name]['제목']

    # def make_tokens(name)
    okt = Okt()
    titles = [title for title in titles]

    tokens = [okt.nouns(title) for title in titles]

    words = []
    for token in tokens:
        for word in token:
            if len(word) > 1:
                words.append(word)

    word_cnt = Counter(words)

    df_word_cnt = pd.DataFrame(pd.Series(word_cnt), columns=['Freq'])
    sorted_cnt = df_word_cnt.sort_values(by='Freq', ascending=False)
    return sorted_cnt

st.bar_chart(make_df(df,name)[:20])



# 3. 경기도인구데이터에 대하여
# 1) 연도별 인구수에 대한 지도시각화  2007년, 2015년, 2019년 연도를 탭으로 제시
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

import json

# data를 불러올때 st.cache로 불러오자
# fname, ext = os.path.splitext(file_path)
# if ext =='csv':
#     return pd.read_csv(~~)
# elif ext in ['xlsx','xls']


with open('data/경기도행정구역경계.json',encoding='utf-8') as f:
    geo_gg = json.loads(f.read())

# 인덱스해당하는 열 이름 index_col 사용
df_gg = pd.read_excel('data/경기도인구데이터.xlsx',index_col='구분')
def mmap(year):
    map = folium.Map(location=[37.5666,126.9782],zoom_start=8)
    folium.GeoJson(geo_gg).add_to(map)


    folium.Choropleth(geo_data=geo_gg,
                      data=df_gg[year],
                      columns=[df_gg.index, df_gg[year]],
                      key_on='feature.properties.name').add_to(map)
    st_folium(map, width=600, height=400)


tab1, tab2, tab3 = st.tabs(['2007','2015','2017'])


with tab1 :
    mmap(2007)

with tab2:
    mmap(2015)

with tab3:
    mmap(2017)



