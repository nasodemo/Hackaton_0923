import streamlit as st
import random
import my_widgets
from time import time
import session_states

# Traditional 음식에 관한 세부 페이지입니다. #
class DescriptionPage:
    def __init__(self, item_name, title_center, description, description_center, recommend_product, recipe):
        session_states.session_init()
        self.item_name = item_name
        self.description = description
        self.recommend_product = recommend_product
        self.recipe = recipe
        self.title_center = title_center
        self.description_center = description_center
    
    # 페이지를 그리는 함수 draw() #
    def draw(self):
        
        # Title #
        title_col1, title_col2, title_col3 = st.columns([1, self.title_center, 1])
        with title_col2:
            st.header(self.item_name)
         
        # Description #
        sub1_col1, sub1_col2, sub1_col3 = st.columns([1, self.description_center, 1])
        with sub1_col2:
            st.text(self.description)
        
        st.subheader('Recommend Product')
        
    
    