import pandas as pd
import numpy as np
import streamlit as st

# 이미 한번 읽어논걸 캐싱해논다 따라서 한번 실행할때 마다 캐싱되있는걸갖고옴
@st.cache_data
def load_data(file_path):
    df = pd.read_excel(file_path)
    return df
# df = pd.read_excel('data/kor_news_240326.xlsx')

df = load_data('data/kor_news_240326.xlsx')
st.markdown('1')
st.dataframe(df,hide_index=True)

st.divider()
st.markdown('2')
st.data_editor(df,
               column_order=('식별자','URL','언론사','기고자','제목'),
               column_config={
                   'URL':st.column_config.LinkColumn(
                    max_chars=300,
                    display_text='Site'
                   )
               })

st.divider()
st.markdown('3')


df['대분류']= df['분류'].str.split('>').str[0]
data = pd.DataFrame(df['대분류'].value_counts())
st.dataframe(data)
st.bar_chart(data)

st.divider()
st.markdown('4')
from konlpy.tag import Okt
from collections import Counter

df['대분류'] = df['분류'].str.split('>').str[0]

# titles =df[df['대분류']=='경제']['제목']


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

st.dataframe(make_df(df,'경제'))
st.bar_chart(make_df(df,'경제')[:20])

st.bar_chart(make_df(df,'사회')[:20])