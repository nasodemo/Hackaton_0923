import streamlit as st
import random
import my_widgets
from time import time
import session_states
import os

# Traditional 음식에 관한 세부 페이지입니다. #
class DirectionPage:
    def __init__(self, items, header, header_center, text, text_center, use_second_text=True, second_text='', second_text_center=1):
        session_states.session_init()
        self.items = items
        random.seed(int(time()) * 10 % 1000)
        random.shuffle(self.items)
        self.before_path = st.session_state.path
        self.header = header
        self.text = text
        self.header_center = header_center
        self.text_center = text_center
        self.use_second_text = use_second_text
        self.second_text = second_text
        self.second_text_center = second_text_center
    
    # 페이지를 그리는 함수 draw() #
    def draw(self):
        
        # Title #
        title_col1, title_col2, title_col3 = st.columns([1, self.header_center, 1])
        with title_col2:
            st.header(self.header)
         
        # Description #
        sub1_col1, sub1_col2, sub1_col3 = st.columns([1, self.text_center, 1])
        with sub1_col2:
            st.text(self.text)
            
        if self.use_second_text:
            sub2_col1, sub2_col2, sub2_col3 = st.columns([1, self.second_text_center, 1])
            with sub2_col2:
                st.text(self.second_text)
        
        # Buttons #
        main_col = list(st.columns([1, 1, 1, 1]))
        
        if len(st.session_state.path) == 1:
            if st.button("Back"):
                session_states.update_path([])
        
        for i in range(len(self.items)):
            background_data = self.items[i][1]
            background = f"background-color: {background_data};" if background_data.startswith("#") else f"background-image: url({background_data});"
            font = "font-size: 28px; font-weight: 600;" if st.session_state.path == [] else "display: none;"
            st.markdown(f"""
            <style>
            #tabs-bui2-tabpanel-0 > div:nth-child(1) > div > div:nth-child(4) > div:nth-child({(i%4+1)}) > div:nth-child(1) > div > div:nth-child({(i//4)*2+1}) > div > button
            {{  
                height: 200px;
                border: None;
                border-radius: 10%;
                {background}
                background-size: cover;
            }}
            #tabs-bui2-tabpanel-0 > div:nth-child(1) > div > div:nth-child(4) > div:nth-child({(i%4+1)}) > div:nth-child(1) > div > div:nth-child({(i//4)*2+1}) > div > button > div > p
            {{
                {font}
            }}
            </style>
            """, unsafe_allow_html=True)
            
        for i in range(4):
            with main_col[i]:
                for j in range(len(self.items)):
                    if j % 4 == i:
                        my_widgets.direction_button(self.items[j][0], self.before_path)
        
    
    