import streamlit as st
import random
import my_widgets
from time import time

# Traditional 음식에 관한 세부 페이지입니다. #

items = ['Curry Udon', 'Curry Rice', 'Cheese Ramen', 'Jjajang rice', 'Jjamjjamyeon', 'Sticky Rice Donuts']
random.seed(int(time()) * 10 % 1000)
random.shuffle(items)
before_path = st.session_state.path

# 페이지를 그리는 함수 draw() #
def draw():
    
    # Title #
    title_col1, title_col2, title_col3 = st.columns([1, 5.3, 1])
    with title_col2:
        st.header('Specific Food Category Selection')
     
    # Description #
    sub1_col1, sub1_col2, sub1_col3 = st.columns([1, 4, 1])
    with sub1_col2:
        st.text('What food do you like? We will find recipes and ingredients of the selected food.')
    
    # Buttons #
    main_col = list(st.columns([1, 1, 1, 1]))
    with main_col[0]:
        my_widgets.direction_button(items[0], before_path)
        my_widgets.direction_button(items[4], before_path)
        my_widgets.direction_button(items[8], before_path)
    with main_col[1]:
        my_widgets.direction_button(items[1], before_path)
        my_widgets.direction_button(items[5], before_path)
    with main_col[2]:
        my_widgets.direction_button(items[2], before_path)
        my_widgets.direction_button(items[6], before_path)
    with main_col[3]:
        my_widgets.direction_button(items[3], before_path)
        my_widgets.direction_button(items[7], before_path)
    
    