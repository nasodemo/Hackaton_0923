# import streamlit as st
# import big_category

# col1_selector = '#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div > div:nth-child(1)'
# col2_selector = '#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div > div:nth-child(2)'

# path : 
# if 'path' not in st.session_state:
#     st.session_state.path = []
    
# path_size = len(st.session_state.path)
    
# def update_path(path):
#     st.session_state.path = path

# for item in st.session_state.path:
#     st.button(item)
    
# class Style:
#     button_height = '200px'
    
# MyStyle = Style();
    
# buttons_markdown = st.markdown(f"""
# <style>
# /* Test */
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > div > button,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > div > button
# {{
#     height: {MyStyle.button_height};
#     border: none;
#     border-radius: 10%;
#     background-color: #219C90;
# }}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > button,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > button
# {{
#     height: {MyStyle.button_height};
#     border: none;
#     border-radius: 10%;
#     background-color: #3D246C;
# }}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > button,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > button
# {{
#     height: {MyStyle.button_height};
#     border: none;
#     border-radius: 10%;
#     background-color: #EE9322;
# }}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div > button,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div > button
# {{
#     height: {MyStyle.button_height};
#     border: none;
#     border-radius: 10%;
#     background-color: #D83F31;
# }}
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > div > button > div > p,
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > button > div > p,
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > button > div > p,
# #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.css-1y4p8pa.e1g8pov64 > div:nth-child(1) > div > div.css-434r0z.esravye3 > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div > button > div > p,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(1) > div > button > div > p,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(2) > div > button > div > p,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(1) > div > button > div > p,
# #tabs-bui2-tabpanel-1 > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > div > div:nth-child(2) > div > button > div > p
# {{
#     font-size: 50px;
# }}
# </style>
# """, unsafe_allow_html=True)
    
# def buttons():
#     col1, col2 = st.columns([1, 1], gap='medium')
        
#     with col1:
#         if st.button("Traditional", use_container_width=True): 
#             update_path(['Traditional'])
#         if st.button("K-POP Stars Pick", use_container_width=True):
#             update_path(['K-POP Stars Pick'])
            
#     with col2:
#         if st.button("Fusion", use_container_width=True):
#             update_path(['Fusion'])
#         if st.button("Home", use_container_width=True):
#             update_path(['Home'])
            
# buttons()