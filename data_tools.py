import json
# Load Datas
with open('./DB/food_data_refined.json', 'r', encoding='utf8') as f:
    food_data = json.load(f)

with open('./DB/sum_of_ordered_quantity.json', 'r', encoding='utf8') as f:
    order_rank = json.load(f)['QUANTITY']

with open('./DB/inventory_age.json', 'r', encoding='utf8') as f:
    inventory_age = json.load(f)

with open('./DB/discount_level.json', 'r', encoding='utf8') as f:
    # discount_level[sku]   -> level  :float
    # discount_level.keys() -> [sku...]:list
    discount_level = json.load(f)

with open('./DB/purchase_url.json', 'r', encoding='utf8') as f:
    # purchase_url[sku] -> url:str
    purchase_url = json.load(f)['AMAZON']

with open('./DB/inventory_image.json', 'r', encoding='utf8') as f:
    # image_url[sku] -> image_url:str
    image_url = json.load(f)['IMAGE_LINK']



def get_foods_by_category(category:str):
    out=[]
    for i in food_data:
        if category in i['CATEGORY_ENG']: out.append(i)
    return out

def to_button_datas(data:dict):
    out = []
    for d in data:
        out.append([d['TITLE_ENG'], 'https://jung-yeon-ho1234567890.on.drv.tw/junks'+d['IMAGE']])
    return out

def get_food_by_name(name:str):
    for i in food_data:
        if name == i['TITLE_ENG']: return i

def sku_to_name(sku:str) -> str:
    return inventory_age['PRODUCT_NAME'][sku]

def sku_to_purchase_url(sku:str) -> str:
    return purchase_url[sku]


def get_discount_level(sku:str) -> float:
    # level = \
    # (inventory_age['INV_AGE_0_TO_90_DAYS'][sku]     *0.01
    # +inventory_age['INV_AGE_91_TO_180_DAYS'][sku]   *0.5
    # +inventory_age['INV_AGE_181_TO_270_DAYS'][sku]  *1.0
    # +inventory_age['INV_AGE_271_TO_365_DAYS'][sku]  *2.0
    # +inventory_age['INV_AGE_365_PLUS_DAYS'][sku]    *5.0
    
    # +inventory_age['ESTIMATED_EXCESS_QUANTITY'][sku]*1.5)
    # return level
    
    return discount_level[sku]
    

def get_food_data() -> list:
    '''
    return list of foods
    ---
    food:dictionary
    
    TITLE_KOR:str
    TITLE_ENG:str
    
    CATEGORY_KOR:list
    CATEGORY_ENG:list
    
    
    
    RECIPE:str
    SUMMARY:str
    
    INGREDIENT:list
    LINKS:list
    '''
    return food_data



if __name__ == "__main__":
    pass