import streamlit as st
import session_states
import direction_page
import description_page
import data_tools
import chat_bot
# from pages_information import data

session_states.session_init()

Tab_Recomendation, Tab_ChatBot = st.tabs(["Recommendation", "ChatBot"])

with Tab_Recomendation:
    
    if st.session_state.path == []:
        direction_page.DirectionPage(
            [['Traditional', '#219C90'], ['Fusion', "#3D246C"], ["K-POP Star's Pick", "#EE9322"], ['Home', "#D83F31"], ['Vegan', '#1A5D1A']],
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
        st.markdown('---')
        st.markdown('#### Recommend Product')
        
        cols = st.columns(len(item['LINKS']))
        for i, col in enumerate(cols):
            with col:
                img, txt = st.columns([1,2])
                with img: st.image(item['IMAGE_URL'][i], width=min(100, int(200/len(item['LINKS']))))
                with txt:
                    name = item['LINKS'][i].split('www.amazon.com/')[1].split('/dp')[0].replace('-', ' ')
                    st.write(name)
                    st.markdown(f'<a href="{item["LINKS"][i]}" style="color: #dddddd;">Purchase</a>', unsafe_allow_html=True)
        
        st.image('https://jung-yeon-ho1234567890.on.drv.tw/junks'+item['IMAGE'], use_column_width='always')
        st.markdown('## Recipe')
        
        recipes = item['RECIPE'].split('\n')[1:]
        for i in range(len(recipes)):
            st.markdown('> '+recipes[i])
            
        st.write("")
        if st.button("Back"):
            if len(st.session_state.path) == 2:
                session_states.update_path([st.session_state.path[0]])
                
        # st.morkdown("""
        # <script>
        #     const checkbox = document.getElementByName("wideMode");
        #     console.log(checkbox[0])
        # </script>
        # """)
        
with Tab_ChatBot:
    chat_bot.draw()