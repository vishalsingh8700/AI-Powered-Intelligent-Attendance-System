import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(to bottom, #E0E3FF, #B8C6DB) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: rgba(255, 255, 255, 0.9) !important;
                    padding:2.5rem !important;
                    border-radius: 2rem !important;
                    box-shadow: 0 8px 16px rgba(0,0,0,0.1) !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(to bottom, #F7F9FC, #E0E3FF) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    


def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                 

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 2rem !important;
                background: linear-gradient(45deg, #A8DADC, #457B9D) !important;
                color: white !important;
                padding: 12px 24px !important;
                border: none !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
                font-weight: 600 !important;
                }

            button[kind="secondary"]{
                border-radius: 2rem !important;
                background: linear-gradient(45deg, #F4A261, #E76F51) !important;
                color: white !important;
                padding: 12px 24px !important;
                border: none !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
                font-weight: 600 !important;
                }

            button[kind="tertiary"]{
                border-radius: 2rem !important;
                background: linear-gradient(45deg, #A8DADC, #457B9D) !important;
                color: white !important;
                padding: 12px 24px !important;
                border: none !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
                font-weight: 600 !important;
                }

            button:hover{
                transform: scale(1.05) !important;
                box-shadow: 0 6px 12px rgba(0,0,0,0.15) !important;
                }
        </style>  

                """
            ,unsafe_allow_html=True)
    

