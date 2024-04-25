import streamlit as st

st.header('Popover Container')

# expand랑 비슷하긴한데 좀 작은 팝업같은 느낌
with st.popover('Open popover'):
    st.write('Hello')
    name= st.text_input("What's your name?")

st.write('Yore name : ',name)

# use_conttainer_width 테두리
popover = st.popover('좋아하는 색상은?',use_container_width=True)

red = popover.checkbox('red',True)
blue = popover.checkbox('blue')

if red:
    st.write(':red[빨강]')

if blue:
    st.write(':blue[파랑]')

with st.popover('popover 사용시 주의점'):
    st.write('popover를 또 다른 popover 안에 배치 불가')
