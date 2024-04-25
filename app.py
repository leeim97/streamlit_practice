import streamlit as st

# 메인페이지
# pages에 숫자_이름에서 숫자는 보여지는 순서

#https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
#https://docs.streamlit.io/develop/concepts/multipage-apps/pages-directory


st.set_page_config(
    page_title='Streamlit Practice',
    page_icon="🧘‍♂️",
    layout='wide',
    # expanded 하면 옆에 보임
    initial_sidebar_state="expanded",
)


st.title('스트림릿 맛보기')

st.write('''
- Text elements  
- Data elements 
- Data Column configure  
- Chart elements  
- Input elemnets  
- Layout & Containers
''')