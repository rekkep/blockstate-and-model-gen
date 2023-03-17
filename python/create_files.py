import json


SAVE_PATH = 'mod/assets'



def change_file_path(save_path):
    global SAVE_PATH
    SAVE_PATH = save_path

def add_mod_blocks(block_name: str, code: str, block_type: str):
    with open(f"mod/ModBlocks/{block_type}.txt", 'a') as f:
        f.write(str(code) + "\n")
    with open(f"mod/ModBlocks/block.txt", 'a') as f:
        f.write(str(block_name + "\n"))


def add_models_block(block, code):
    with open(f"{SAVE_PATH}/models/block/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)


def add_models_item(block, code):
    with open(f"{SAVE_PATH}/models/item/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)


def add_blockstates(block, code):
    with open(f"{SAVE_PATH}/blockstates/{block.lower()}.json", "w") as f:
        #f.write(str(code).replace("'", '"').replace("True", "true"))
        json.dump(json.loads(str(code).replace("'", '"').replace("True", "true")), f, indent=4)



def add_lang(block: str, name: list[str], lang: list[str] = ["en_us"]):
    for i, language in enumerate(lang):
        new_names = dict()
        if type(name) == list:
            new_names[block.lower()] = name[i]
        else:
            new_names[block.lower()] = name
        with open(f"mod/assets/lang/{language}.json", "r") as f:
            data = json.load(f)
        data.update(new_names)
        with open(f"mod/assets/lang/{language}.json", "w") as f:
            json.dump(data, f, indent=4)
        
