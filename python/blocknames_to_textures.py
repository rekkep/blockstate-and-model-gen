import os, json




TEXTURE_PATH = "mod/assets/textures/VanillaDefault+1.19.2/assets/minecraft/textures/block"
ALL_PATH = "block_variant/all.txt"
EXPERIMENTAL_PATH = "block_variant/experimental.txt"
FENCE_PATH = "block_variant/fence.txt"
OTHER_PATH = "block_variant/other.txt"
STAIRS_PATH = "block_variant/stairs.txt"
WALL_PATH = "block_variant/wall.txt"

ALL_JSON = "block_variant/all.json"
EXPERIMENTAL_JSON = "block_variant/experimental.json"
FENCE_JSON = "block_variant/fence.json"
OTHER_JSON = "block_variant/other.json"
STAIRS_JSON = "block_variant/stairs.json"
WALL_JSON = "block_variant/wall.json"

paths = [ALL_PATH,
         EXPERIMENTAL_PATH,
         FENCE_PATH,
         OTHER_PATH,
         STAIRS_PATH,
         WALL_PATH]

jsons = [ALL_JSON,
         EXPERIMENTAL_JSON,
         FENCE_JSON,
         OTHER_JSON,
         STAIRS_JSON,
         WALL_JSON]

for i, path in enumerate(paths):
    with open(path, "r") as f:
        d = dict()
        for line in f:
            count = 0
            textures = []
            block = line.strip("\n").lower().replace(" ", "_")
            for file in os.listdir(TEXTURE_PATH):
                if file.find(block) != -1:
                    textures.append(file.replace(".png", ""))
                    count += 1
            d[block] = {}
            #d[block]["count"] = count
            d[block]["textures_name"] = textures
        with open(jsons[i], "w") as j:
            json.dump(d, j, indent=4)
    