import streamlit as st
from database import authenticate_user, register_user

def show_auth_page():
    # Page title and styling
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Heavenly Delusion</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #646464;'>Your Safe Space for Mental Wellbeing</h3>", unsafe_allow_html=True)
    
    # Quote display with styling
    st.markdown("---")
    quote_container = st.container()
    with quote_container:
        st.markdown("""
        <div style='background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
            <p style='font-style: italic; color: #555; text-align: center;'>"Healing is not a destination, but a journey of small steps that lead to profound change."</p>
            <p style='text-align: right; color: #888;'>— Heavenly Delusion Wisdom</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["username"] = None

    if not st.session_state["authenticated"]:
        # Create a clean centered layout
        col1, center_col, col2 = st.columns([1, 2, 1])
        
        with center_col:
            st.subheader("Welcome Back")
            option = st.radio("Login or Register", ["Login", "Register"])
            
            with st.form(key="auth_form"):
                username = st.text_input("Username", key="username_input")
                password = st.text_input("Password", type="password", key="password_input")
                
                if option == "Register":
                    submit_button = st.form_submit_button(label="Sign Up", use_container_width=True)
                    if submit_button:
                        if register_user(username, password):
                            st.success("Account created! Please log in.")
                        else:
                            st.error("Username already exists.")
                
                if option == "Login":
                    submit_button = st.form_submit_button(label="Log In", use_container_width=True)
                    if submit_button:
                        if authenticate_user(username, password):
                            st.session_state["authenticated"] = True
                            st.session_state["username"] = username
                            st.success(f"Welcome back, {username}!")
                            st.rerun()
                        else:
                            st.error("Invalid username or password.")
            
            # Add a helpful message
            st.markdown("<div style='text-align: center; margin-top: 20px; color: #888;'>Your journey to mental wellness begins here</div>", unsafe_allow_html=True)
