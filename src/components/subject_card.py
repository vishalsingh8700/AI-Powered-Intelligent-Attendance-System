import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background: linear-gradient(180deg, #ffffff 0%, #f7f8ff 100%); padding:24px; border-radius:24px; border:1px solid rgba(148,163,184,0.18); box-shadow:0 18px 38px rgba(15,23,42,0.08); margin-bottom:24px;">
            <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:12px; align-items:flex-start;">
                <div>
                    <h3 style="margin:0; color:#0f172a; font-size:1.5rem;">{name}</h3>
                    <p style="color:#475569; margin:0.75rem 0 0; font-size:0.98rem;">Code: <span style="background:#e0efff; color:#1d4ed8; padding:5px 10px; border-radius:999px;">{code}</span> &nbsp;|&nbsp; Section: {section}</p>
                </div>
            </div>
    """
    
    if stats:
        html+= """
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
        """
        for icon, label, value in stats:
            html+= f'<div style="background: #EB459E10; padding:5px 12px; border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        
        html+= "</div>"

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()