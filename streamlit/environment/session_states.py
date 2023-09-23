import streamlit as st

# session_states를 관리하는 파일입니다.

# session_states 초기화
def session_init():
    if 'path' not in st.session_state:
        st.session_state.path = []
    
session_init()
    
# State "path"를 수정합니다.
def update_path(path):
    st.session_state.path = path
    st.experimental_rerun()