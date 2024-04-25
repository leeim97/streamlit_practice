import streamlit as st

st.title('Input Widgets!')
st.header('1. Button elements')
st.subheader('Button')
# primary는 버튼 색이 강조(빨간색), default는 second
st.button('초기화',type='primary')

if st.button('안녕'):
    st.write('반가워 :smile:')
else:
    st.write('잘가! :rasing_hand:')

st.subheader('Link Button')
st.link_button('google','https://www.google.com')

st.subheader('Page Link')
st.page_link('app.py',label='Home',icon='🏠')
st.page_link('pages/1_Text_elements.py',
             label='Text elements')
st.page_link('pages/2_Data_elements.py',
             label='Data elements')
st.page_link('pages/연습문제.py',
             label='Exercise',disabled=True)
st.page_link('https://docs.streamlit.io/develop/api-reference',
             label='Streamlit Docs',icon='🌏')


st.subheader('Form submit_Button',divider=True)

with st.form(key='form1'):
    id= st.text_input('Id')
    pw=st.text_input('Password',type='password')
    submitted = st.form_submit_button('로그인')
if submitted:
    st.write('id :',id,'password :',pw)


form = st.form(key= 'form2')
title = form.text_input('제목')
contents=form.text_area(('질문입력'))
submit = form.form_submit_button('작성')
if submit:
    st.write('제목 : ',title)



st.divider()

st.header('2. Selection elements')
st.subheader('Checkbox')

# 체크되면 True 안되면 False 반환
# default는 False ,value로 설정 가능
# collapsed,hidden는 안보이게 default는 visible
agree = st.checkbox('찬성',label_visibility='visible',value=True)
if agree:
    st.write('Good!')

st.subheader('Toggle')
# 체크되면 True 안되면 False 반환
on = st.toggle('선택')
if on:
    st.write('on')

#라디오는 여러개중에 하나 선택할때 많이 씀
st.subheader('Radio')
# 선택한거 리턴됌
fruit = st.radio(
    '좋아하는 과일은?',
    ['바나나','딸기','메론','사과','배'], # 선택할 목록의값
    # 설명이 추가됌
    captions=['웃어요','달콤해요','시원해요',
              '상큼해요','즙이많아요'],
    horizontal=True, # 수평방향으로 디폴트는 False임
    index=1 # 처음에 체크되어질 곳의 넘버
)

if fruit=='바나나':
    st.write('바나나를 선택했군요')
else:
    st.write('바나나가 아니네~~')

st.subheader('Selectbox')
fruit = st.selectbox('과일을 선택하세요',
             ['바나나','딸기','사과','메론'],
            index=1 ,# 처음에 체크되어질 곳의 넘버,None도 가능
            placeholder='과일을 선택하세요!', # None일경우의 멘트
            # hidden은 한칸 띄어지고 collapse는 띄어진 칸 없다
            label_visibility='hidden'
             )
st.write(f'당신이 선택한 과일은 {fruit}')

st.divider()

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
    )

st.divider()

st.subheader('Multiselect')
# 반환값 리스트 형태
colors = st.multiselect('당신이 좋아하는 색상은?',
               options =['red','green','blue','yellow','pink'],
                        default=['green','blue'])
st.write('선택한 생상은 ',colors)

st.subheader('Selectslider')
color = st.select_slider('당신이 좋아하는 색상은',
                 options=['red','green','blue','yellow'
                     ,'pink','violet','indigo','orange'],
                        value='blue')

colors = st.select_slider('당신이 좋아하는 색상은',
                 options=['red','green','blue','yellow'
                     ,'pink','violet','indigo','orange'],
                        value=('blue','pink'))

# key 안쓰면 오류 생겼음
color_st, color_end = st.select_slider('당신이 좋아하는 색상은',
                 options=['red','green','blue','yellow'
                     ,'pink','violet','indigo','orange'],
                        value=('blue','pink'),key='slider2')

st.write('당신이 좋아하는 색상은',color_st,color_end)

st.subheader('color picker')
color = st.color_picker('Pick A Color','#00f900')
st.write('The current color is',color)

st.header('3. Numeric Input elements')
st.subheader('Number input')
num = st.number_input('숫자입력')
st.write(num)

num = st.number_input('숫자입력',value=None,
                      placeholder='숫자를 입력하세요')
st.write(f'현재숫자: {num}')

# step은 -,+버튼 누르면 step값만큼 증감
num = st.number_input('숫자입력',min_value=-10,
                      max_value=10,step=2,
                      # format='%f'
                      )
st.write(f'현재숫자: {num}')

# min,max가 실수이면 step도 실수여야하는듯?
num = st.number_input('숫자입력',min_value=-10.0,
                      max_value=10.0,step=0.5,
                      format='%.2f'
                      )
st.write(f'현재숫자: {num:.2f}')

st.subheader('slider')
age =st.slider('나이',min_value=0,max_value=100,value=20,
         step=2)
st.write(age)

scores =st.slider('점수대',min_value=0.0,max_value=100.0,value=(25.0,50.0),
       )
st.write(scores)

st.header('4. Text input elements')
st.subheader('Text input')
id = st.text_input('아이디',value='id')
pw = st.text_input('비밀번호',type='password')
st.write(f'아이디: {id}, 비밀번호: {pw}')

st.subheader('Text area')
text = st.text_area('질문을 입력하세요')
st.write(text)
st.write(f'총문자길이는{len(text)}')

st.header('5. Data&Time input element')
st.subheader('Date input')

from datetime import datetime,date,time,timedelta


date = st.date_input(label='일자 선택',value=date(2024,3,1),
                     min_value=date(2023,1,1),
                     max_value=date(2024,12,31),
                     format='YYYY.MM.DD')
st.write(date)

st.subheader('Time input')
time = st.time_input('시간 입력',
              value=time(8,00),
                     # timedelta 필요
                     step=timedelta(minutes=10)
                     )

st.write(time)

import time
with st.spinner('Wait fo it..'):
    time.sleep(5)
st.balloons()
st.success('Done!')

# progress_text = "Operation in progress. Please wait."
# my_bar = st.progress(0, text=progress_text)
#
# for percent_complete in range(100):
#     time.sleep(0.01)
#     my_bar.progress(percent_complete + 1, text=progress_text)
# time.sleep(1)
# my_bar.empty()
#
# st.button("Rerun")