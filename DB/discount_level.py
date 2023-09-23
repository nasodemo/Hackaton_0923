import json


def get_discount_level(sku:str) -> float:
    level = \
    (inventory_age['INV_AGE_0_TO_90_DAYS'][sku]     *0.01
    +inventory_age['INV_AGE_91_TO_180_DAYS'][sku]   *0.5
    +inventory_age['INV_AGE_181_TO_270_DAYS'][sku]  *1.0
    +inventory_age['INV_AGE_271_TO_365_DAYS'][sku]  *2.0
    +inventory_age['INV_AGE_365_PLUS_DAYS'][sku]    *5.0
    
    +inventory_age['ESTIMATED_EXCESS_QUANTITY'][sku]*1.5)
    return level


with open('./inventory_age.json', 'r', encoding='utf8') as f:
    inventory_age = json.load(f)
    
out = {}
for key in inventory_age['PRODUCT_NAME']:
    out[key] = get_discount_level(key)

out = dict(sorted(out.items(), key=lambda item: -item[1]))

with open("./discount_level.json", "w",  encoding='UTF-8') as json_file:
    json.dump(out, json_file, ensure_ascii=False, indent=4)



