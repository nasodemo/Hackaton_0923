import streamlit as st
import session_states

# 내 위젯들을 정의하는 파일입니다.

# 다이렉션용 버튼
def direction_button(name: str, before_path: list):
    if st.button(name, use_container_width=True):
        session_states.update_path(before_path + [name])
    if st.session_state.path == []: 
        st.text(' ')
    else:
        st.text(name)