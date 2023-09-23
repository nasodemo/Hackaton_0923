import streamlit as st
import random
import my_widgets
from time import time
import session_states

# Traditional 음식에 관한 세부 페이지입니다. #

session_states.session_init()

items = ['Seaweed soup', 'Nurungji', 'Abalone porridge', 'Ramen tteokbokki', 'Honey citrus tea', 'Bulgogi', 'Jeonju Bibimbap', 'Dakdori-tang', 'Banquet noodles']
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
        
    for i in range(4):
        with main_col[i]:
            for j in range(len(items)):
                if j % 4 == i:
                    my_widgets.direction_button(items[j], before_path)
    
    
    