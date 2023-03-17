from json import load
import create_blocks as cb

'''

'''




error_file = "block_variant/python/ERROR.txt"
file = "block_variant/block_pairs/json/compressed.json"


def error_log(message: str, error = 'Something went wrong!', path: str = error_file):
    with open(path, 'a') as f:
        f.write(f"ERROR [{str(error)}]: {str(message)}")


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
                    save_path="""Modding/1.19.2_TestMod/fabric-missing-blocks-1.19.2/src/main/resources/\
                                    assets/missingblocks""")
        
        print(f"NEW BLOCK\n{block}")
        #if "button" in blocks[block]["block_types"]:
        #    print(f"Generating button for {block}")
        #    b.create_button()
        if "door" in blocks[block]["block_types"]:
            print(f"Generating door for {block}")
            b.create_door()
        if "fence" in blocks[block]["block_types"]:
            print(f"Generating fence for {block}")
            b.create_fence()
        if "fence_gate" in blocks[block]["block_types"]:
            print(f"Generating fence_gate for {block}")
            b.create_fence_gate()
        #if "pressure_plate" in blocks[block]["block_types"]:
        #    print(f"Generating pressure_plate for {block}")
        #    b.create_pressure_plate()
        #if "sign" in blocks[block]["block_types"]:
        #    print(f"Generating sign for {block}")
        #    b.create_sign()
        if "slab" in blocks[block]["block_types"]:
            print(f"Generating slab for {block}")
            b.create_slab()
        if "stairs" in blocks[block]["block_types"]:
            print(f"Generating stairs for {block}")
            b.create_stairs()
        if "trapdoor" in blocks[block]["block_types"]:
            print(f"Generating trapdoor for {block}")
            b.create_trapdoor()
        if "wall" in blocks[block]["block_types"]:
            print(f"Generating wall for {block}")
            b.create_wall()
    
    


