import streamlit as st
from session_states import update_path
import my_widgets

# 네 가지 Big Category에 대한 페이지입니다.

# 페이지를 그리는 함수 draw()
def draw():
    title_col1, title_col2, title_col3 = st.columns([1, 12, 1])
    with title_col2:
        st.header('Let’s learn about various Korean foods!')
        
    sub1_col1, sub1_col2, sub1_col3 = st.columns([1, 4, 1])
    with sub1_col2:
        st.text('Choose one category and get recommended Korean foods')
        
    sub2_col1, sub2_col2, sub2_col3 = st.columns([1, 2.1, 1])
    with sub2_col2:
        st.text('that can be made with Ottogi’s products.')
    
    main_col1, main_col2, main_col3, main_col4 = st.columns([1, 1, 1, 1])
    with main_col1:
        my_widgets.direction_button('Traditional', [])
    with main_col2:
        my_widgets.direction_button('Fusion', [])
    with main_col3:
        my_widgets.direction_button("K-POP Star's Pick", [])
    with main_col4:
        my_widgets.direction_button('Home', [])