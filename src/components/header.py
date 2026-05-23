import streamlit as st


def header_home():

    logo_url = "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;'/>
            <h3 style='text-align:center; color:#457B9D'>AI Powered<br/>Intelligent Attendance System</h3>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://cdn-icons-png.flaticon.com/512/4436/4436481.png"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#457B9D'>AI Powered<br/>Intelligent Attendance System</h2>
        </div>   
                
                """, unsafe_allow_html=True)