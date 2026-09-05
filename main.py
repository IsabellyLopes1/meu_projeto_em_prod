

import streamlit as st


#procoding -> não ultiliza a ia generativa

st.header ('Calculadora STREAMLIT')

st.write('ADICIONE OS NÚMEROS PARA CALCULAR')

n1 = st.number_input ('digite um número: ', min_value=0)
n2 = st.number_input ('digite um número: ', value=0)

soma_,div_,sub, mult_ = st.columns(4)

if soma_.button('+'):
    soma = n1 + n2
    st.info(soma) 
elif sub.button('-'):
    sub = n1 - n2
    st.info(sub)
elif mult_.button('x'):
  mult = n1 + n2 
  st.info(mult)
elif div_.button(':'):
   div = n1 / n2 
   st.info(div)

st.map




import streamlit as st 
import pandas as pd 

# procoding => não utiliza a IA generativa

dados = pd.read_csv('vendas.csv')

if st.button('mostrar mapa'):
   st.map()
else:
   x = st.map()

st.header('ANALISE DE DADOS')

st.table(dados)
st.bar_chart(dados, x= 'ano', y= 'lucro')
st.scatter_chart(dados, x= 'venda', y= 'lucro')
st.line_chart(dados, x= 'ano', y='venda')