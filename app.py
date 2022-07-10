import streamlit as st
import joblib
import numpy as np
model = joblib.load('diabetes')
st.title('DIABETES PREDICTION')
st.write("""This is a Webapp to predict wheather the given person has diabeties or not by getting the details given below""")
ip0 = st.number_input('GLUCOSE-LEVEL')
ip1 = st.number_input('BLOOD PRESSURE')
ip2 = st.number_input('SKIN THICKNESS')
ip3 = st.number_input('INSULIN LEVEL')
ip4 = st.number_input('BODY MASS INDEX')
ip5 = st.number_input('DIABETESPEDIGREEFUNCTION')
ip6 = st.number_input('AGE')
ls1=np.append(ip0,ip1)
ls2=np.append(ip2,ip3)
ls3=np.append(ip4,ip5)
lsa=np.append(ls1,ls2)
lsb=np.append(ls3,ip6)
ls=np.append(lsa,lsb)
op = model.predict([ls])
if st.button('Predict'):
  if(op[0]==True):
    st.title("The person is diabeteic")
  else:
    st.title("the person is not diabeteic")    
