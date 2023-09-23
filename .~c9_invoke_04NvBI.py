import streamlit as st
import session_states
import direction_page
import description_page
import data_tools
import chat_bot
# from pages_information import data

session_states.session_init()

Tab_Recomendation, Tab_ChatBot = st.tabs(["Recomendation", "ChatBot"])

with Tab_Recomendation:
    
    if st.session_state.path == []:
        direction_page.DirectionPage(
            [['Traditional', '#219C90'], ['Fusion', "#3D246C"], ["K-POP Star's Pick", "#EE9322"], ['Home', "#D83F31"]],
            'Let’s learn about various Korean foods!',
            12.3,
            'Choose one category and get recommended Korean foods',
            3.5,
            True,
            'that can be made with Ottogi’s products.',
            2.0
            ).draw()
        
    elif len(st.session_state.path) == 1:
        items = data_tools.get_foods_by_category(st.session_state.path[0])
        button_data = data_tools.to_button_datas(items)
    
    if st.session_state.path == ["Traditional"]:
        direction_page.DirectionPage(
            button_data,
            'Specific Food Category Selection',
            5.3,
            'What food do you like? We will find recipes and ingredients of the selected food.',
            85).draw()
            
    if st.session_state.path == ["Fusion"]:
        direction_page.DirectionPage(
            button_data,
            'Specific Food Category Selection',
            5.3,
            'What food do you like? We will find recipes and ingredients of the selected food.',
            85).draw()
    
    if st.session_state.path == ["K-POP Star's Pick"]:
        direction_page.DirectionPage(
            button_data,
            'Specific Food Category Selection',
            5.3,
            'What food do you like? We will find recipes and ingredients of the selected food.',
            85).draw()
            
    if st.session_state.path == ['Home']:
        direction_page.DirectionPage(
            button_data,
            'Specific Food Category Selection',
            5.3,
            'What food do you like? We will find recipes and ingredients of the selected food.',
            85).draw()
    
    # Description page        
    if len(st.session_state.path) == 2:
        
        upper_title = st.session_state.path[0]
        item_name = st.session_state.path[1]
        
        item = data_tools.get_food_by_name(item_name)
        
        st.markdown(f'###### {upper_title}')
        st.markdown('---')
        st.markdown(f'<p style="text-align: center; font-weight:bold; font-size:340%;">{item_name}</p>', unsafe_allow_html=True)
        description = item['SUMMARY']
        
        st.markdown(f'<p style="text-align: center; font-size:90%; color:#888;">{description}</p>', unsafe_allow_html=True)
        
        st.markdown('#### Recommend Product')
        
        cols = st.columns(len(item['LINKS']))
        for i, col in enumerate(cols):
            with col:
                img, txt = st.columns([1,2])
                with img: st.image('./flag.png', width=100)
                with txt:
                    st.write('[OTTUGI] THIS IS SOME SORT OF THE PRODUCT NAME.')
                    st.markdown("""
                    #tabs-bui2-tabpanel-0 > div:nth-child(1) > div > div.css-ocqkz7.esravye3 > div:nth-child(1) > div:nth-child(1) > div > div > div.css-115gedg.esravye1 > div:nth-child(1) > div > div:nth-child(2) > div > div > p > a,
                    #tabs-bui2-tabpanel-0 > div:nth-child(1) > div > div.css-ocqkz7.esravye3 > div:nth-child(2) > div:nth-child(1) > div > div > div.css-115gedg.esravye1 > div:nth-child(1) > div > div:nth-child(2) > div > div > p > a,
                    #tabs-bui2-tabpanel-0 > div:nth-child(1) > div > div.css-ocqkz7.esravye3 > div:nth-child(3) > div:nth-child(1) > div > div > div.css-115gedg.esravye1 > div:nth-child(1) > div > div:nth-child(2) > div > div > p > a
                    {
                        color: #ffffff;
                    }
                    """)
                    st.write(item['LINKS'][i])
                
        st.image(item['IMAGE'], use_column_width='always')
        st.markdown('## Recipe')
        
        recipes = item['RECIPE'].split('\n')[1:]
        for i in range(len(recipes)):
            recipe = recipes[i]
            st.markdown(recipe}')
        
with Tab_ChatBot:
    chat_bot.draw()