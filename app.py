import streamlit as st

st.text('ciao')

if st.checkbox('non sono un robot'):
    st.write('chekkata')


def somma (l1:float, l2:float):
    a = l1+l2
    return a

def main():
    st.text('calcola somma rettangolo')
    num1= st.slider('Inserisci lato1 rettangolo', 0, 100, 20)
    num2= st.slider('Inserisci lato2 rettangolo', 0, 100, 30)
    r = somma(num1, num2)
    st.write('la somma del rettangolo è', r)
if __name__ == '__main__':
    main()

