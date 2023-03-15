import streamlit as st
from app import connect_sftp, read_database

st.title("Uppdatera Nielsen Data")

if st.button('Uppdatera Nu'):
    st.write(connect_sftp())

else:
    pass

st.caption("Senaste nerladdade filerna")
st.dataframe(read_database())
