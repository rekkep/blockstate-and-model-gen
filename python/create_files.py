import json


SAVE_PATH = 'Minecraft/blockstate-and-model-gen-main/mod-files'



def change_file_path(save_path):
    global SAVE_PATH
    SAVE_PATH = save_path

def add_mod_blocks(block_name: str, code: str, block_type: str):
    with open(f"Minecraft/blockstate-and-model-gen-main/mod-files/ModBlocks/{block_type}.txt", 'a') as f:
        f.write(str(code) + "\n")
    with open(f"Minecraft/blockstate-and-model-gen-main/mod-files/ModBlocks/block.txt", 'a') as f:
        f.write(str(block_name + "\n"))


def add_models_block(block, code):
    with open(f"{SAVE_PATH}/assets/models/block/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)


def add_models_item(block, code):
    with open(f"{SAVE_PATH}/assets/models/item/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)


def add_blockstates(block, code):
    with open(f"{SAVE_PATH}/assets/blockstates/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)
        
        




def add_lang(block: str, name: list[str], lang: list[str] = ["en_us"]):
    for i, language in enumerate(lang):
        new_names = dict()
        if type(name) == list:
            new_names[block.lower()] = name[i]
        else:
            new_names[block.lower()] = name
        with open(f"{SAVE_PATH}/assets/lang/{language}.json", "r") as f:
            data = json.load(f)
        data.update(new_names)
        with open(f"{SAVE_PATH}/assets/lang/{language}.json", "w") as f:
            json.dump(data, f, indent=4)
        
        
def add_crafting_recipe(block, code):
    with open(f"{SAVE_PATH}/data/recipes/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)


def add_smelting_recipe():
    pass


def add_stonecutter_recipe():
    pass


def add_loot_table(block, code):
    with open(f"{SAVE_PATH}/data/loot_tables/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)
