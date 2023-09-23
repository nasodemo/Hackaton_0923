{"changed":true,"filter":false,"title":"main.py","tooltip":"/main.py","value":"import streamlit as st\nimport session_states\nimport direction_page\nimport description_page\nimport data_tools\nimport chat_bot\n# from pages_information import data\n\nsession_states.session_init()\n\nTab_Recomendation, Tab_ChatBot = st.tabs([\"Recommendation\", \"ChatBot\"])\n\nwith Tab_Recomendation:\n    \n    if st.session_state.path == []:\n        direction_page.DirectionPage(\n            [['Traditional', '#219C90'], ['Fusion', \"#3D246C\"], [\"K-POP Star's Pick\", \"#EE9322\"], ['Home', \"#D83F31\"], ['Vegan', '#1A5D1A']],\n            'Let’s learn about various Korean foods!',\n            12.3,\n            'Choose one category and get recommended Korean foods',\n            3.5,\n            True,\n            'that can be made with Ottogi’s products.',\n            2.0\n            ).draw()\n        \n    elif len(st.session_state.path) == 1:\n        items = data_tools.get_foods_by_category(st.session_state.path[0])\n        button_data = data_tools.to_button_datas(items)\n        \n        direction_page.DirectionPage(\n            button_data,\n            'Specific Food Category Selection',\n            5.3,\n            'What food do you like? We will find recipes and ingredients of the selected food.',\n            85).draw()\n    \n    # Description page        \n    if len(st.session_state.path) == 2:\n        \n        upper_title = st.session_state.path[0]\n        item_name = st.session_state.path[1]\n        \n        item = data_tools.get_food_by_name(item_name)\n        \n        st.markdown(f'###### {upper_title}')\n        st.markdown('---')\n        st.markdown(f'<p style=\"text-align: center; font-weight:bold; font-size:340%;\">{item_name}</p>', unsafe_allow_html=True)\n        description = item['SUMMARY']\n        \n        st.markdown(f'<p style=\"text-align: center; font-size:90%; color:#888;\">{description}</p>', unsafe_allow_html=True)\n        st.markdown('---')\n        st.markdown('#### Recommend Product')\n        \n        cols = st.columns(len(item['LINKS']))\n        for i, col in enumerate(cols):\n            with col:\n                img, txt = st.columns([1,2])\n                with img: st.image(data_tools.image_url(item['SKU']), width=int(200/len(item['LINKS'])))\n                with txt:\n                    name = item['LINKS'][i].split('www.amazon.com/')[1].split('/dp')[0].replace('-', ' ')\n                    st.write(name)\n                    st.markdown(f'<a href=\"{item[\"LINKS\"][i]}\" style=\"color: #dddddd;\">구매하러 가기</a>', unsafe_allow_html=True)\n        \n        st.image(item['IMAGE'], use_column_width='always')\n        st.markdown('## Recipe')\n        \n        recipes = item['RECIPE'].split('\\n')[1:]\n        for i in range(len(recipes)):\n            st.markdown('> '+recipes[i])\n            \n        st.write(\"\")\n        if st.button(\"Back\"):\n            if len(st.session_state.path) == 2:\n                session_states.update_path([st.session_state.path[0]])\n                \n        st.morkdown(\"\"\"\n        \n        \"\"\")\n        \nwith Tab_ChatBot:\n    chat_bot.draw()","undoManager":{"mark":0,"position":16,"stack":[[{"start":{"row":16,"column":131},"end":{"row":16,"column":137},"action":"remove","lines":["0f0f0f"],"id":1271,"ignore":true},{"start":{"row":16,"column":131},"end":{"row":16,"column":137},"action":"insert","lines":["1A5D1A"]}],[{"start":{"row":74,"column":70},"end":{"row":76,"column":12},"action":"insert","lines":["","                ","            "],"id":1272,"ignore":true}],[{"start":{"row":76,"column":8},"end":{"row":76,"column":12},"action":"remove","lines":["    "],"id":1273,"ignore":true},{"start":{"row":76,"column":8},"end":{"row":76,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":76,"column":9},"end":{"row":76,"column":11},"action":"insert","lines":["t."],"id":1274,"ignore":true}],[{"start":{"row":76,"column":11},"end":{"row":76,"column":12},"action":"insert","lines":["m"],"id":1275,"ignore":true}],[{"start":{"row":76,"column":12},"end":{"row":76,"column":14},"action":"insert","lines":["or"],"id":1276,"ignore":true}],[{"start":{"row":76,"column":14},"end":{"row":76,"column":15},"action":"insert","lines":["k"],"id":1277,"ignore":true}],[{"start":{"row":76,"column":15},"end":{"row":76,"column":16},"action":"insert","lines":["d"],"id":1278,"ignore":true}],[{"start":{"row":76,"column":16},"end":{"row":76,"column":18},"action":"insert","lines":["ow"],"id":1279,"ignore":true}],[{"start":{"row":76,"column":18},"end":{"row":76,"column":21},"action":"insert","lines":["n()"],"id":1280,"ignore":true}],[{"start":{"row":76,"column":20},"end":{"row":76,"column":22},"action":"insert","lines":["\"\""],"id":1281,"ignore":true}],[{"start":{"row":76,"column":21},"end":{"row":77,"column":8},"action":"insert","lines":["","        "],"id":1282,"ignore":true}],[{"start":{"row":76,"column":21},"end":{"row":77,"column":8},"action":"remove","lines":["","        "],"id":1283,"ignore":true}],[{"start":{"row":76,"column":22},"end":{"row":76,"column":24},"action":"insert","lines":["\"\""],"id":1284,"ignore":true}],[{"start":{"row":76,"column":24},"end":{"row":76,"column":26},"action":"insert","lines":["\"\""],"id":1285,"ignore":true}],[{"start":{"row":76,"column":23},"end":{"row":77,"column":8},"action":"insert","lines":["","        "],"id":1286,"ignore":true}],[{"start":{"row":77,"column":8},"end":{"row":78,"column":8},"action":"insert","lines":["","        "],"id":1287,"ignore":true}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":29,"column":8},"end":{"row":29,"column":8},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1695429128096}