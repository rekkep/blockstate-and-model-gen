from json import load
import create_blocks as cb
import os

'''

'''




error_file = "Minecraft/blockstate-and-model-gen-main/ERROR.txt"
file = "Minecraft/blockstate-and-model-gen-main/block_pairs/json/compressed.json"



def error_log(message: str, error = 'Something went wrong!', path: str = error_file):
    with open(path, 'a') as f:
        f.write(f"ERROR [{str(error)}]: {str(message)}")


def generate_mod_files(button: bool = False, door: bool = True, fence: bool = True, fence_gate: bool = True, 
                       pressure_plate: bool = False, sign: bool = False, slab: bool = True, stairs: bool = True, 
                       trapdoor: bool = True, wall: bool = True):
    with open(file, 'r') as f:
        blocks = load(f) 
    for block in blocks:
        if "experimental" in blocks[block]["block_types"]:
            pass
        else:
            try:
                texture_bottom = blocks[block]["textures_name"]["texture_bottom"]
            except:
                try:
                    texture_bottom = blocks[block]["textures_name"]["texture_top"]
                except:
                    try:
                        texture_bottom = blocks[block]["textures_name"]["texture"]
                    except:
                        texture_bottom = list(blocks[block]["textures_name"].values())[0]
                        error_log(f"used '{texture_bottom}' as texture_bottom for {block}\n", 
                                error='missing texture_bottom')
                        
            try:
                texture_side = blocks[block]["textures_name"]["texture_side"]
            except:
                try:
                    texture_side = blocks[block]["textures_name"]["texture"]
                except:
                    texture_side = list(blocks[block]["textures_name"].values())[0]
                    error_log(f"used '{texture_side}' as texture_side for {block}\n",
                            error='missing texture_side')
            
            try:
                texture_top = blocks[block]["textures_name"]["texture_top"]
            except:
                try:
                    texture_top = blocks[block]["textures_name"]["texture"]
                except:
                    texture_top = list(blocks[block]["textures_name"].values())[0]
                    error_log(f"used '{texture_top}' as texture_top for {block}\n",
                            error='missing texture_top')
                    
            try:
                texture_name = blocks[block]["textures_name"]["texture"]
            except:
                try:
                    texture_name = blocks[block]["textures_name"]["texture_side"]
                except:
                    try:
                        texture_name = blocks[block]["textures_name"]["texture_top"]
                    except:
                        try:
                            texture_name = blocks[block]["textures_name"]["texture_bottom"]
                        except:
                            texture_name = "default"
                            error_log(f"used '{texture_name}' as texture_name for {block}\n",
                                    error='missing texture_name')

            try:
                block_name = blocks[block]["textures_name"]["name"]
            except:
                block_name = block
                pass
            
            
            
            
            b = cb.Blocks(block_name, texture_bottom=texture_bottom, texture_side=texture_side, 
                        texture_top=texture_top, texture_name=texture_name, 
                        save_path='')
            
            print(f"NEW BLOCK\n{block}")
            
            if button:
                #if "button" in blocks[block]["block_types"]:
                #    print(f"Generating button for {block}")
                #    b.create_button()
                pass

            if door:
                if "door" in blocks[block]["block_types"]:
                    print(f"Generating door for {block}")
                    b.create_door()

            if fence:
                if "fence" in blocks[block]["block_types"]:
                    print(f"Generating fence for {block}")
                    b.create_fence()

            if fence_gate:
                if "fence_gate" in blocks[block]["block_types"]:
                    print(f"Generating fence_gate for {block}")
                    b.create_fence_gate()

            if pressure_plate:
                #if "pressure_plate" in blocks[block]["block_types"]:
                #    print(f"Generating pressure_plate for {block}")
                #    b.create_pressure_plate()
                pass
            
            if sign:
                #if "sign" in blocks[block]["block_types"]:
                #    print(f"Generating sign for {block}")
                #    b.create_sign()
                pass
            
            if slab:
                if "slab" in blocks[block]["block_types"]:
                    print(f"Generating slab for {block}")
                    b.create_slab()

            if stairs:
                if "stairs" in blocks[block]["block_types"]:
                    print(f"Generating stairs for {block}")
                    b.create_stairs()

            if trapdoor:
                if "trapdoor" in blocks[block]["block_types"]:
                    print(f"Generating trapdoor for {block}")
                    b.create_trapdoor()

            if wall:
                if "wall" in blocks[block]["block_types"]:
                    print(f"Generating wall for {block}")
                    b.create_wall()
        
        
def delete_mod_files():
    DIR = "e:/VS Code/Minecraft/blockstate-and-model-gen-main/mod-files/"
    MOD_BLOCKS = ["block.txt", "DOOR.txt", "FENCE_GATE.txt", "FENCE.txt", "SLAB.txt", "STAIRS.txt", "TRAPDOOR.txt", "WALL.txt"]
    ASSETS = ["blockstates/", "models/block/", "models/item/"]
    LANG = "Minecraft/blockstate-and-model-gen-main/mod-files/assets/lang/en_us.json"
    DATA = ["loot_tables/", "recipes/"]
    
    
    
    for file in MOD_BLOCKS:
        try:
            os.remove(DIR + 'ModBlocks/' + file)
            print(f"{file} removed")
        except:
            print(f"{DIR + 'ModBlocks/' + file} not found")
        
    for ordner in ASSETS:
        for file in os.listdir(DIR + "assets/" + ordner):
            os.remove(DIR + "assets/" + ordner + file)
            print(f"{file} removed")
            
    for ordner in ASSETS:
        for file in os.listdir(DIR + "assets/" + ordner):
            os.remove(DIR + "assets/" + ordner + file)
            print(f"{file} removed")
            
    
    with open(LANG, 'w') as f:
        f.write('{}')
        print("resetted en_en lang")
    
    
delete_mod_files()

'''generate_mod_files(button = False, door = True, fence = True, fence_gate = True, 
                       pressure_plate = False, sign = False, slab = True, stairs = True, 
                       trapdoor = True, wall = True)'''
