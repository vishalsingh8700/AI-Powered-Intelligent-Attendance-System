
import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home
def home_screen():


    header_home()
    style_background_home()
    style_base_layout()

    st.markdown("<h3 style='text-align: center; color: #457B9D;'>Welcome to AI Powered Intelligent Attendance System! Choose your role to get started.</h3>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("👨‍🎓  I'm a Student")
        st.image("https://i.ibb.co/844D9Lrt/mascot-student.png", width=120)
        if st.button('Student Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='home_student_portal'):
            st.session_state['login_type']='student'
            st.rerun()

    with col2:
        st.header("👩‍🏫  I'm a Teacher")
        st.image("https://i.ibb.co/CsmQQV6X/mascot-prof.png", width=145)
        if st.button('Teacher Portal', type='primary', icon=':material/arrow_outward:', icon_position='right', key='home_teacher_portal'):
            st.session_state['login_type']='teacher'
            st.rerun()

    footer_home()