import streamlit as st

# 문제가 많아서 connector페이지로 하는게 났데

#mysql 연결(접속)
conn = st.connection('shopDB',
              type='sql',
            # db이름,비밀번호
              url='mysql://streamlit:1234@localhost:3306/shopDB')
# 질의 수행
df = conn.query('SELECT * from customer;',ttl=600)

st.write(df)
#
# df.itertuples()
# for row in df.itertuples():
#     # 행.열이름
#     st.write(f'{row.customer_name}이 {row.phone}을 가짐')
#
# sql = '''INSERT INTO customer(customer_id,customer_name,phone,birthday)' \
#       values (:id,:name,:phone,:birth);'''
#
# with conn.session as s:
#     s.execute(sql,{'id':6,'name':"홍길동",
#     'phone':"010-1111-1111",'birth':"2001-01-30"})
#     s.commit()

##################################################################


# df = conn.query('SELECT * FROM customer;',ttl=600)
# st.write(df)


