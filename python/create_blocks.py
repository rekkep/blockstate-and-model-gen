import create_files as cf


class Blocks:
    
    def __init__(self, name: str, texture_name: str = "default", texture_bottom: str = "default",
                 texture_side: str = "default", texture_top: str = "default",
                 texture_mod_id: str = "minecraft",
                 mod_id: str = "missingblocks", tab: str = "ModItemGroup.MISSING_BLOCKS",
                 block_type: str = "", block_variant: str = "", sign_type:str="",
                 save_path: str ="") -> None:
        
        self.name = name.replace(" ", "_").lower()
        self.texture_name = texture_name
        self.texture_bottom = texture_bottom
        self.texture_side = texture_side
        self.texture_top = texture_top
        self.texture_mod_id = texture_mod_id
        self.mod_id = mod_id
        self.tab = tab
        
        self.block_type = block_type
        self.block_variant = block_variant
        self.sign_type = sign_type
        
        if texture_name == "default":
            self.texture_name = self.name
        if texture_bottom == "default":
            self.texture_bottom = self.texture_name
        if texture_side == "default":
            self.texture_side = self.texture_name
        if texture_top == "default":
            self.texture_top = self.texture_name
      
        self.V1_19_2 = self.update_V1_19_2()
        
        
        if save_path != '':
            cf.change_file_path(save_path)
      
    def update_V1_19_2(self):
        
        return {
            "MOD_BLOCKS_CODE": f"public static final Block {self.name.upper()}_{self.block_type.upper()} = create{self.block_variant.capitalize()}{''.join([i.capitalize() for i in self.block_type.split('_')])}({self.name.upper().replace('BRICK', 'BRICKS')}, {self.tab}{self.sign_type});",
            "BLOCK": {},
            "BUTTON": {
                "BLOCK_BUTTON": {"parent": "minecraft:block/button",
                                 "textures": {
                                     "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                 }},
                "BLOCK_BUTTON_INVENTORY": {"parent": "minecraft:block/button_inventory",
                                           "textures": {
                                               "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                           }},
                "BLOCK_BUTTON_PRESSED": {"parent": "minecraft:block/button_pressed",
                                         "textures": {
                                             "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                         }},
                "ITEM_BUTTON": {"parent": f"{self.mod_id}:block/{self.name}_button_inventory"},
                "BLOCKSTATES": {"variants": {
                    "face=ceiling,facing=east,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "x": 180,
                        "y": 270
                    },
                    "face=ceiling,facing=east,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "x": 180,
                        "y": 270
                    },
                    "face=ceiling,facing=north,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "x": 180,
                        "y": 180
                    },
                    "face=ceiling,facing=north,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "x": 180,
                        "y": 180
                    },
                    "face=ceiling,facing=south,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "x": 180
                    },
                    "face=ceiling,facing=south,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "x": 180
                    },
                    "face=ceiling,facing=west,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "x": 180,
                        "y": 90
                    },
                    "face=ceiling,facing=west,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "x": 180,
                        "y": 90
                    },
                    "face=floor,facing=east,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "y": 90
                    },
                    "face=floor,facing=east,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "y": 90
                    },
                    "face=floor,facing=north,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button"
                    },
                    "face=floor,facing=north,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed"
                    },
                    "face=floor,facing=south,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "y": 180
                    },
                    "face=floor,facing=south,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "y": 180
                    },
                    "face=floor,facing=west,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "y": 270
                    },
                    "face=floor,facing=west,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "y": 270
                    },
                    "face=wall,facing=east,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "uvlock": True,
                        "x": 90,
                        "y": 90
                    },
                    "face=wall,facing=east,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "uvlock": True,
                        "x": 90,
                        "y": 90
                    },
                    "face=wall,facing=north,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "uvlock": True,
                        "x": 90
                    },
                    "face=wall,facing=north,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "uvlock": True,
                        "x": 90
                    },
                    "face=wall,facing=south,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "uvlock": True,
                        "x": 90,
                        "y": 180
                    },
                    "face=wall,facing=south,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "uvlock": True,
                        "x": 90,
                        "y": 180
                    },
                    "face=wall,facing=west,powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_button",
                        "uvlock": True,
                        "x": 90,
                        "y": 270
                    },
                    "face=wall,facing=west,powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_button_pressed",
                        "uvlock": True,
                        "x": 90,
                        "y": 270
                    }
                }}
            },
            "DOOR": {
                "BLOCK_DOOR_BOTTOM_LEFT": {"parent": "minecraft:block/door_bottom_left",
                                           "textures": {
                                               "bottom": f"{self.texture_mod_id}:block/{self.texture_name}",#_door_bottom",
                                               "top": f"{self.texture_mod_id}:block/{self.texture_name}"#_door_top"
                                           }},
                "BLOCK_DOOR_BOTTOM_LEFT_OPEN": {"parent": "minecraft:block/door_bottom_left_open",
                                                "textures": {
                                                    "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                                    "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                                }},
                "BLOCK_DOOR_BOTTOM_RIGHT": {"parent": "minecraft:block/door_bottom_right",
                                       "textures": {
                                           "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                           "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                       }},
                "BLOCK_DOOR_BOTTOM_RIGHT_OPEN": {"parent": "minecraft:block/door_bottom_right_open",
                                            "textures": {
                                                "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                                "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                            }},
                "BLOCK_DOOR_TOP_LEFT": {"parent": "minecraft:block/door_top_left",
                                   "textures": {
                                       "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                       "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                   }},
                "BLOCK_DOOR_TOP_LEFT_OPEN": {"parent": "minecraft:block/door_top_left_open",
                                        "textures": {
                                            "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                            "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                        }},
                "BLOCK_DOOR_TOP_RIGHT": {"parent": "minecraft:block/door_top_right",
                                      "textures": {
                                          "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                          "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                      }},
                "BLOCK_DOOR_TOP_RIGHT_OPEN": {"parent": "minecraft:block/door_top_right_open",
                                           "textures": {
                                               "bottom": f"{self.texture_mod_id}:block/{self.texture_name}", #TODO:_door_bottom",
                                               "top": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_door_top"
                                           }},
                "ITEM_DOOR": {"parent": "minecraft:item/generated",
                              "textures": {
                                  # TODO: create own texture or use minecraft block
                                  "layer0": f"{self.texture_mod_id}:block/{self.texture_name}" #f"{self.mod_id}:item/{self.name}_door"
                              }},
                "BLOCKSTATES": {"variants": {
                    "facing=east,half=lower,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left"
                    },
                    "facing=east,half=lower,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left_open",
                        "y": 90
                    },
                    "facing=east,half=lower,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right"
                    },
                    "facing=east,half=lower,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right_open",
                        "y": 270
                    },
                    "facing=east,half=upper,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left"
                    },
                    "facing=east,half=upper,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left_open",
                        "y": 90
                    },
                    "facing=east,half=upper,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right"
                    },
                    "facing=east,half=upper,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right_open",
                        "y": 270
                    },
                    "facing=north,half=lower,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left",
                        "y": 270
                    },
                    "facing=north,half=lower,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left_open"
                    },
                    "facing=north,half=lower,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right",
                        "y": 270
                    },
                    "facing=north,half=lower,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right_open",
                        "y": 180
                    },
                    "facing=north,half=upper,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left",
                        "y": 270
                    },
                    "facing=north,half=upper,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left_open"
                    },
                    "facing=north,half=upper,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right",
                        "y": 270
                    },
                    "facing=north,half=upper,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right_open",
                        "y": 180
                    },
                    "facing=south,half=lower,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left",
                        "y": 90
                    },
                    "facing=south,half=lower,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left_open",
                        "y": 180
                    },
                    "facing=south,half=lower,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right",
                        "y": 90
                    },
                    "facing=south,half=lower,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right_open"
                    },
                    "facing=south,half=upper,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left",
                        "y": 90
                    },
                    "facing=south,half=upper,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left_open",
                        "y": 180
                    },
                    "facing=south,half=upper,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right",
                        "y": 90
                    },
                    "facing=south,half=upper,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right_open"
                    },
                    "facing=west,half=lower,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left",
                        "y": 180
                    },
                    "facing=west,half=lower,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_left_open",
                        "y": 270
                    },
                    "facing=west,half=lower,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right",
                        "y": 180
                    },
                    "facing=west,half=lower,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_bottom_right_open",
                        "y": 90
                    },
                    "facing=west,half=upper,hinge=left,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left",
                        "y": 180
                    },
                    "facing=west,half=upper,hinge=left,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_left_open",
                        "y": 270
                    },
                    "facing=west,half=upper,hinge=right,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right",
                        "y": 180
                    },
                    "facing=west,half=upper,hinge=right,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_door_top_right_open",
                        "y": 90
                    }
                }}
            },
            "FENCE_GATE": {
                "BLOCK_FENCE_GATE": {"parent": "minecraft:block/template_fence_gate",
                                     "textures": {
                                         "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                     }},
                "BLOCK_FENCE_GATE_OPEN": {"parent": "minecraft:block/template_fence_gate_open",
                                          "textures": {
                                              "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                          }},
                "BLOCK_FENCE_GATE_WALL": {"parent": "minecraft:block/template_fence_gate_wall",
                                          "textures": {
                                              "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                          }},
                "BLOCK_FENCE_GATE_WALL_OPEN": {"parent": "minecraft:block/template_fence_gate_wall_open",
                                               "textures": {
                                                   "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                               }},
                "ITEM_FENCE_GATE": {"parent": f"{self.mod_id}:block/{self.name}_fence_gate"},
                "BLOCKSTATES": {"variants": {
                    "facing=east,in_wall=false,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate",
                        "uvlock": True,
                        "y": 270
                    },
                    "facing=east,in_wall=false,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_open",
                        "uvlock": True,
                        "y": 270
                    },
                    "facing=east,in_wall=true,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall",
                        "uvlock": True,
                        "y": 270
                    },
                    "facing=east,in_wall=true,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall_open",
                        "uvlock": True,
                        "y": 270
                    },
                    "facing=north,in_wall=false,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate",
                        "uvlock": True,
                        "y": 180
                    },
                    "facing=north,in_wall=false,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_open",
                        "uvlock": True,
                        "y": 180
                    },
                    "facing=north,in_wall=true,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall",
                        "uvlock": True,
                        "y": 180
                    },
                    "facing=north,in_wall=true,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall_open",
                        "uvlock": True,
                        "y": 180
                    },
                    "facing=south,in_wall=false,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate",
                        "uvlock": True
                    },
                    "facing=south,in_wall=false,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_open",
                        "uvlock": True
                    },
                    "facing=south,in_wall=true,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall",
                        "uvlock": True
                    },
                    "facing=south,in_wall=true,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall_open",
                        "uvlock": True
                    },
                    "facing=west,in_wall=false,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate",
                        "uvlock": True,
                        "y": 90
                    },
                    "facing=west,in_wall=false,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_open",
                        "uvlock": True,
                        "y": 90
                    },
                    "facing=west,in_wall=true,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall",
                        "uvlock": True,
                        "y": 90
                    },
                    "facing=west,in_wall=true,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_fence_gate_wall_open",
                        "uvlock": True,
                        "y": 90
                    }
                }},
            },
            "FENCE": {
                "BLOCK_FENCE_INVENTORY": {"parent": "minecraft:block/fence_inventory",
                                          "textures": {
                                              "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                          }},
                "BLOCK_FENCE_POST": {"parent": "minecraft:block/fence_post",
                                     "textures": {
                                         "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                     }},
                "BLOCK_FENCE_SIDE": {"parent": "minecraft:block/fence_side",
                                     "textures": {
                                         "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                     }},
                "ITEM_FENCE": {"parent": f"{self.mod_id}:block/{self.name}_fence_inventory"},
                "BLOCKSTATES": {"multipart": [
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_fence_post"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_fence_side",
                            "uvlock": True
                        },
                        "when": {
                            "north": "true"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_fence_side",
                            "uvlock": True,
                            "y": 90
                        },
                        "when": {
                            "east": "true"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_fence_side",
                            "uvlock": True,
                            "y": 180
                        },
                        "when": {
                            "south": "true"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_fence_side",
                            "uvlock": True,
                            "y": 270
                        },
                        "when": {
                            "west": "true"
                        }
                    }
                ]},

            },
            "PRESSURE_PLATE": {
                "BLOCK_PRESSURE_PLATE": {"parent": "minecraft:block/pressure_plate_up",
                                         "textures": {
                                             "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                         }},
                "BLOCK_PRESSURE_PLATE_DOWN": {"parent": "minecraft:block/pressure_plate_down",
                                              "textures": {
                                                  "texture": f"{self.texture_mod_id}:block/{self.texture_name}"
                                              }},
                "ITEM_PRESSURE_PLATE": {"parent": f"{self.mod_id}:block/{self.name}_pressure_plate"},
                "BLOCKSTATES": {"variants": {
                    "powered=false": {
                        "model": f"{self.mod_id}:block/{self.name}_pressure_plate"
                    },
                    "powered=true": {
                        "model": f"{self.mod_id}:block/{self.name}_pressure_plate_down"
                    }
                }},

            },
            "SIGN": {
                "BLOCK_SIGN": {"textures": {
                    "particle": f"{self.texture_mod_id}:block/{self.texture_name}"
                }},
                "ITEM_SIGN": {"parent": "minecraft:item/generated",
                              "textures": {
                                  "layer0": f"{self.mod_id}:item/{self.name}_sign"
                              }},
                "BLOCKSTATES_SIGN": {"variants": {
                    "": {
                        "model": f"{self.mod_id}:block/{self.name}_sign"
                    }
                }},
                },
            "WALL_SIGN":{
                "BLOCKSTATES_WALL_SIGN": {"variants": {
                    "": {
                        "model": f"{self.mod_id}:block/{self.name}_sign"
                    }
                }}             
                },
            "SLAB": {
                "BLOCK_SLAB": {"parent": "minecraft:block/slab",
                               "textures": {
                                   "bottom": f"{self.texture_mod_id}:block/{self.texture_name}",
                                   "side": f"{self.texture_mod_id}:block/{self.texture_name}",
                                   "top": f"{self.texture_mod_id}:block/{self.texture_name}"
                               }},
                "BLOCK_SLAB_TOP": {"parent": "minecraft:block/slab_top",
                                   "textures": {
                                       "bottom": f"{self.texture_mod_id}:block/{self.texture_name}",
                                       "side": f"{self.texture_mod_id}:block/{self.texture_name}",
                                       "top": f"{self.texture_mod_id}:block/{self.texture_name}"
                                   }},
                "ITEM_SLAB": {"parent": f"{self.mod_id}:block/{self.name}_slab"},
                "BLOCKSTATES": {"variants": {
                    "type=bottom": {
                        "model": f"{self.mod_id}:block/{self.name}_slab"
                    },
                    "type=double": {
                        "model": f"{self.texture_mod_id}:block/{self.texture_name}" #TODO: use modded textures
                    },
                    "type=top": {
                        "model": f"{self.mod_id}:block/{self.name}_slab_top"
                    }
                }}
            },
            "STAIRS": {
                "BLOCK_STAIRS": {"parent": "minecraft:block/stairs",
                                 "textures": {
                                     "bottom": f"{self.texture_mod_id}:block/{self.texture_bottom}",
                                     "side": f"{self.texture_mod_id}:block/{self.texture_side}",
                                     "top": f"{self.texture_mod_id}:block/{self.texture_top}"
                                 }},
                "BLOCK_STAIRS_INNER": {"parent": "minecraft:block/inner_stairs",
                                       "textures": {
                                           "bottom": f"{self.texture_mod_id}:block/{self.texture_bottom}",
                                           "side": f"{self.texture_mod_id}:block/{self.texture_side}",
                                           "top": f"{self.texture_mod_id}:block/{self.texture_top}"
                                       }},
                "BLOCK_STAIRS_OUTER": {"parent": "minecraft:block/outer_stairs",
                                       "textures": {
                                           "bottom": f"{self.texture_mod_id}:block/{self.texture_bottom}",
                                           "side": f"{self.texture_mod_id}:block/{self.texture_side}",
                                           "top": f"{self.texture_mod_id}:block/{self.texture_top}"
                                       }},
                "ITEM_STAIRS": {"parent": f"{self.mod_id}:block/{self.name}_stairs"},
                "BLOCKSTATES": {"variants": {
                                "facing=east,half=bottom,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 270
                                },
                                "facing=east,half=bottom,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner"
                                },
                                "facing=east,half=bottom,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 270
                                },
                                "facing=east,half=bottom,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer"
                                },
                                "facing=east,half=bottom,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs"
                                },
                                "facing=east,half=top,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180
                                },
                                "facing=east,half=top,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 90
                                },
                                "facing=east,half=top,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180
                                },
                                "facing=east,half=top,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 90
                                },
                                "facing=east,half=top,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "x": 180
                                },
                                "facing=north,half=bottom,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 180
                                },
                                "facing=north,half=bottom,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 270
                                },
                                "facing=north,half=bottom,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 180
                                },
                                "facing=north,half=bottom,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 270
                                },
                                "facing=north,half=bottom,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "y": 270
                                },
                                "facing=north,half=top,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 270
                                },
                                "facing=north,half=top,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180
                                },
                                "facing=north,half=top,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 270
                                },
                                "facing=north,half=top,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180
                                },
                                "facing=north,half=top,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 270
                                },
                                "facing=south,half=bottom,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner"
                                },
                                "facing=south,half=bottom,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 90
                                },
                                "facing=south,half=bottom,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer"
                                },
                                "facing=south,half=bottom,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 90
                                },
                                "facing=south,half=bottom,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "y": 90
                                },
                                "facing=south,half=top,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 90
                                },
                                "facing=south,half=top,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 180
                                },
                                "facing=south,half=top,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 90
                                },
                                "facing=south,half=top,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 180
                                },
                                "facing=south,half=top,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 90
                                },
                                "facing=west,half=bottom,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 90
                                },
                                "facing=west,half=bottom,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "y": 180
                                },
                                "facing=west,half=bottom,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 90
                                },
                                "facing=west,half=bottom,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "y": 180
                                },
                                "facing=west,half=bottom,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "y": 180
                                },
                                "facing=west,half=top,shape=inner_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 180
                                },
                                "facing=west,half=top,shape=inner_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_inner",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 270
                                },
                                "facing=west,half=top,shape=outer_left": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 180
                                },
                                "facing=west,half=top,shape=outer_right": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs_outer",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 270
                                },
                                "facing=west,half=top,shape=straight": {
                                    "model": f"{self.mod_id}:block/{self.name}_stairs",
                                    "uvlock": True,
                                    "x": 180,
                                    "y": 180
                                }
                                }}
            },
            "TRAPDOOR": {
                "BLOCK_TRAPDOOR_BOTTOM": {"parent": "minecraft:block/template_orientable_trapdoor_bottom",
                                          "textures": {
                                              "texture": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_trapdoor"
                                          }},
                "BLOCK_TRAPDOOR_OPEN": {"parent": "minecraft:block/template_orientable_trapdoor_open",
                                        "textures": {
                                            "texture": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_trapdoor"
                                        }},
                "BLOCK_TRAPDOOR_TOP": {"parent": "minecraft:block/template_orientable_trapdoor_top",
                                       "textures": {
                                           "texture": f"{self.texture_mod_id}:block/{self.texture_name}"#TODO:_trapdoor"
                                       }},
                "ITEM_TRAPDOOR": {"parent": f"{self.mod_id}:block/{self.name}_trapdoor_bottom"},
                "BLOCKSTATES": {"variants": {
                    "facing=east,half=bottom,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_bottom",
                        "y": 90
                    },
                    "facing=east,half=bottom,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "y": 90
                    },
                    "facing=east,half=top,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_top",
                        "y": 90
                    },
                    "facing=east,half=top,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "x": 180,
                        "y": 270
                    },
                    "facing=north,half=bottom,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_bottom"
                    },
                    "facing=north,half=bottom,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open"
                    },
                    "facing=north,half=top,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_top"
                    },
                    "facing=north,half=top,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "x": 180,
                        "y": 180
                    },
                    "facing=south,half=bottom,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_bottom",
                        "y": 180
                    },
                    "facing=south,half=bottom,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "y": 180
                    },
                    "facing=south,half=top,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_top",
                        "y": 180
                    },
                    "facing=south,half=top,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "x": 180,
                        "y": 0
                    },
                    "facing=west,half=bottom,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_bottom",
                        "y": 270
                    },
                    "facing=west,half=bottom,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "y": 270
                    },
                    "facing=west,half=top,open=false": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_top",
                        "y": 270
                    },
                    "facing=west,half=top,open=true": {
                        "model": f"{self.mod_id}:block/{self.name}_trapdoor_open",
                        "x": 180,
                        "y": 90
                    }
                }},

            },
            "WALL": {
                "BLOCK_WALL_INVENTORY": {"parent": "minecraft:block/wall_inventory",
                                         "textures": {
                                             "wall": f"{self.texture_mod_id}:block/{self.texture_name}"
                                         }},
                "BLOCK_WALL_POST": {"parent": "minecraft:block/template_wall_post",
                                    "textures": {
                                        "wall": f"{self.texture_mod_id}:block/{self.texture_name}"
                                    }},
                "BLOCK_WALL_SIDE": {"parent": "minecraft:block/template_wall_side",
                                    "textures": {
                                        "wall": f"{self.texture_mod_id}:block/{self.texture_name}"
                                    }},
                "BLOCK_WALL_SIDE_TALL": {"parent": "minecraft:block/template_wall_side_tall",
                                         "textures": {
                                             "wall": f"{self.texture_mod_id}:block/{self.texture_name}"
                                         }},
                "ITEM_WALL": {"parent": f"{self.mod_id}:block/{self.name}_wall_inventory"},
                "BLOCKSTATES": {"multipart": [
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_post"
                        },
                        "when": {
                            "up": "true"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side",
                            "uvlock": True
                        },
                        "when": {
                            "north": "low"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side",
                            "uvlock": True,
                            "y": 90
                        },
                        "when": {
                            "east": "low"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side",
                            "uvlock": True,
                            "y": 180
                        },
                        "when": {
                            "south": "low"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side",
                            "uvlock": True,
                            "y": 270
                        },
                        "when": {
                            "west": "low"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side_tall",
                            "uvlock": True
                        },
                        "when": {
                            "north": "tall"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side_tall",
                            "uvlock": True,
                            "y": 90
                        },
                        "when": {
                            "east": "tall"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side_tall",
                            "uvlock": True,
                            "y": 180
                        },
                        "when": {
                            "south": "tall"
                        }
                    },
                    {
                        "apply": {
                            "model": f"{self.mod_id}:block/{self.name}_wall_side_tall",
                            "uvlock": True,
                            "y": 270
                        },
                        "when": {
                            "west": "tall"
                        }
                    }
                ]},

            }
        }

    
    def create_button(self, button_type: str):
        self.block_type = "BUTTON"
        self.block_variant = button_type
        
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_BUTTON = self.V1_19_2[self.block_type]["BLOCK_BUTTON"]
        BLOCK_BUTTON_INVENTORY = self.V1_19_2[self.block_type]["BLOCK_BUTTON_INVENTORY"]
        BLOCK_BUTTON_PRESSED = self.V1_19_2[self.block_type]["BLOCK_BUTTON_PRESSED"]
        ITEM_BUTTON = self.V1_19_2[self.block_type]["ITEM_BUTTON"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]
        
        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(BLOCK_NAME, BLOCK_BUTTON)
        cf.add_models_block(f"{BLOCK_NAME}_inventory",
                            BLOCK_BUTTON_INVENTORY)
        cf.add_models_block(f"{BLOCK_NAME}_pressed", BLOCK_BUTTON_PRESSED)
        cf.add_models_item(BLOCK_NAME, ITEM_BUTTON)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)
        
        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
        
    def create_wooden_button(self):
        self.create_button("Wooden")
        self.block_variant = ""


    def create_stone_button(self):
        self.create_button("Stone")
        self.block_variant = ""

    
    def create_door(self):
        self.block_type = "DOOR"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_DOOR_BOTTOM_LEFT = self.V1_19_2[self.block_type]["BLOCK_DOOR_BOTTOM_LEFT"]
        BLOCK_DOOR_BOTTOM_LEFT_OPEN = self.V1_19_2[self.block_type]["BLOCK_DOOR_BOTTOM_LEFT_OPEN"]
        BLOCK_DOOR_BOTTOM_RIGHT = self.V1_19_2[self.block_type]["BLOCK_DOOR_BOTTOM_RIGHT"]
        BLOCK_DOOR_BOTTOM_RIGHT_OPEN = self.V1_19_2[self.block_type]["BLOCK_DOOR_BOTTOM_RIGHT_OPEN"]
        BLOCK_DOOR_TOP_LEFT = self.V1_19_2[self.block_type]["BLOCK_DOOR_TOP_LEFT"]
        BLOCK_DOOR_TOP_LEFT_OPEN = self.V1_19_2[self.block_type]["BLOCK_DOOR_TOP_LEFT_OPEN"]
        BLOCK_DOOR_TOP_RIGHT = self.V1_19_2[self.block_type]["BLOCK_DOOR_TOP_RIGHT"]
        BLOCK_DOOR_TOP_RIGHT_OPEN = self.V1_19_2[self.block_type]["BLOCK_DOOR_TOP_RIGHT_OPEN"]
        ITEM_DOOR = self.V1_19_2[self.block_type]["ITEM_DOOR"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]
        
        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}_bottom_left",BLOCK_DOOR_BOTTOM_LEFT)
        cf.add_models_block(f"{BLOCK_NAME}_bottom_left_open",BLOCK_DOOR_BOTTOM_LEFT_OPEN)
        cf.add_models_block(f"{BLOCK_NAME}_bottom_right", BLOCK_DOOR_BOTTOM_RIGHT)
        cf.add_models_block(f"{BLOCK_NAME}_bottom_right_open", BLOCK_DOOR_BOTTOM_RIGHT_OPEN)
        cf.add_models_block(f"{BLOCK_NAME}_top_left", BLOCK_DOOR_TOP_LEFT)
        cf.add_models_block(f"{BLOCK_NAME}_top_left_open", BLOCK_DOOR_TOP_LEFT_OPEN)
        cf.add_models_block(f"{BLOCK_NAME}_top_right", BLOCK_DOOR_TOP_RIGHT)
        cf.add_models_block(f"{BLOCK_NAME}_top_right_open", BLOCK_DOOR_TOP_RIGHT_OPEN)
        cf.add_models_item(BLOCK_NAME, ITEM_DOOR)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
    
    
    def create_fence_gate(self):
        self.block_type = "FENCE_GATE"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_FENCE_GATE = self.V1_19_2[self.block_type]["BLOCK_FENCE_GATE"]
        BLOCK_FENCE_GATE_OPEN = self.V1_19_2[self.block_type]["BLOCK_FENCE_GATE_OPEN"]
        BLOCK_FENCE_GATE_WALL = self.V1_19_2[self.block_type]["BLOCK_FENCE_GATE_WALL"]
        BLOCK_FENCE_GATE_WALL_OPEN = self.V1_19_2[self.block_type]["BLOCK_FENCE_GATE_WALL_OPEN"]
        ITEM_FENCE_GATE = self.V1_19_2[self.block_type]["ITEM_FENCE_GATE"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]
        
        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}", BLOCK_FENCE_GATE)
        cf.add_models_block(f"{BLOCK_NAME}_open", BLOCK_FENCE_GATE_OPEN)
        cf.add_models_block(f"{BLOCK_NAME}_wall", BLOCK_FENCE_GATE_WALL)
        cf.add_models_block(f"{BLOCK_NAME}_wall_open", BLOCK_FENCE_GATE_WALL_OPEN)
        cf.add_models_item(BLOCK_NAME, ITEM_FENCE_GATE)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)
        
        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
    
    
    def create_fence(self):
        self.block_type = "FENCE"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()

        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_FENCE_INVENTORY = self.V1_19_2[self.block_type]["BLOCK_FENCE_INVENTORY"]
        BLOCK_FENCE_POST = self.V1_19_2[self.block_type]["BLOCK_FENCE_POST"]
        BLOCK_FENCE_SIDE = self.V1_19_2[self.block_type]["BLOCK_FENCE_SIDE"]
        ITEM_FENCE = self.V1_19_2[self.block_type]["ITEM_FENCE"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]

        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}_inventory", BLOCK_FENCE_INVENTORY)
        cf.add_models_block(f"{BLOCK_NAME}_post", BLOCK_FENCE_POST)
        cf.add_models_block(f"{BLOCK_NAME}_side", BLOCK_FENCE_SIDE)
        cf.add_models_item(BLOCK_NAME, ITEM_FENCE)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
        
    def create_pressure_plate(self, pressure_plate_type:str):
        self.block_type = "PRESSURE_PLATE"
        self.block_variant = pressure_plate_type
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()

        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_PRESSURE_PLATE = self.V1_19_2[self.block_type]["BLOCK_PRESSURE_PLATE"]
        BLOCK_PRESSURE_PLATE_DOWN = self.V1_19_2[self.block_type]["BLOCK_PRESSURE_PLATE_DOWN"]
        ITEM_PRESSURE_PLATE = self.V1_19_2[self.block_type]["ITEM_PRESSURE_PLATE"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]

        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}", BLOCK_PRESSURE_PLATE)
        cf.add_models_block(f"{BLOCK_NAME}_down", BLOCK_PRESSURE_PLATE_DOWN)
        cf.add_models_item(BLOCK_NAME, ITEM_PRESSURE_PLATE)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
    
    def create_all_pressure_plate(self):
        self.create_pressure_plate("All")
        self.block_variant = ""
    
    
    def create_mob_pressure_plate(self):
        self.create_pressure_plate("Mob")
        self.block_variant = ""
    
    
    def create_sign(self, sign_type):
        self.block_type = "SIGN"
        self.sign_type = ", " + sign_type
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()

        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_SIGN = self.V1_19_2[self.block_type]["BLOCK_SIGN"]
        ITEM_SIGN = self.V1_19_2[self.block_type]["ITEM_SIGN"]
        BLOCKSTATES_SIGN = self.V1_19_2[self.block_type]["BLOCKSTATES_SIGN"]
        

        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(BLOCK_NAME, BLOCK_SIGN)
        cf.add_models_item(BLOCK_NAME, ITEM_SIGN)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES_SIGN)
        

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
        self.create_wall_sign()

    
    def create_wall_sign(self):
        self.block_type = "WALL_SIGN"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        BLOCKSTATES_WALL_SIGN = self.V1_19_2[self.block_type]["BLOCKSTATES_WALL_SIGN"]
        
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES_WALL_SIGN)
        
        self.sign_type = ""
        
       
    def create_slab(self):
        self.block_type = "SLAB"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_SLAB = self.V1_19_2[self.block_type]["BLOCK_SLAB"]
        BLOCK_SLAB_TOP = self.V1_19_2[self.block_type]["BLOCK_SLAB_TOP"]
        ITEM_SLAB = self.V1_19_2[self.block_type]["ITEM_SLAB"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]
        
        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(BLOCK_NAME, BLOCK_SLAB)
        cf.add_models_block(f"{BLOCK_NAME}_top", BLOCK_SLAB_TOP)
        cf.add_models_item(BLOCK_NAME, ITEM_SLAB)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)
        
        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
 
    def create_stairs(self):
        self.block_type = "STAIRS"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()
        
        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_STAIRS = self.V1_19_2[self.block_type]["BLOCK_STAIRS"]
        BLOCK_STAIRS_OUTER = self.V1_19_2[self.block_type]["BLOCK_STAIRS_OUTER"]
        BLOCK_STAIRS_INNER = self.V1_19_2[self.block_type]["BLOCK_STAIRS_INNER"]
        ITEM_STAIRS = self.V1_19_2[self.block_type]["ITEM_STAIRS"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]
        
        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(BLOCK_NAME, BLOCK_STAIRS)
        cf.add_models_block(f"{BLOCK_NAME}_outer", BLOCK_STAIRS_OUTER)
        cf.add_models_block(f"{BLOCK_NAME}_inner", BLOCK_STAIRS_INNER)
        cf.add_models_item(BLOCK_NAME, ITEM_STAIRS)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)
        
        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
        
        
    def create_trapdoor(self):
        self.block_type = "TRAPDOOR"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()

        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_TRAPDOOR_BOTTOM = self.V1_19_2[self.block_type]["BLOCK_TRAPDOOR_BOTTOM"]
        BLOCK_TRAPDOOR_OPEN = self.V1_19_2[self.block_type]["BLOCK_TRAPDOOR_OPEN"]
        BLOCK_TRAPDOOR_TOP = self.V1_19_2[self.block_type]["BLOCK_TRAPDOOR_TOP"]
        ITEM_TRAPDOOR = self.V1_19_2[self.block_type]["ITEM_TRAPDOOR"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]

        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}_bottom", BLOCK_TRAPDOOR_BOTTOM)
        cf.add_models_block(f"{BLOCK_NAME}_open", BLOCK_TRAPDOOR_OPEN)
        cf.add_models_block(f"{BLOCK_NAME}_top", BLOCK_TRAPDOOR_TOP)
        cf.add_models_item(BLOCK_NAME, ITEM_TRAPDOOR)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))


    def create_wall(self):
        self.block_type = "WALL"
        BLOCK_NAME = self.get_block_name()

        self.V1_19_2 = self.update_V1_19_2()

        MOD_BLOCKS_CODE = self.V1_19_2["MOD_BLOCKS_CODE"]
        BLOCK_WALL_INVENTORY = self.V1_19_2[self.block_type]["BLOCK_WALL_INVENTORY"]
        BLOCK_WALL_POST = self.V1_19_2[self.block_type]["BLOCK_WALL_POST"]
        BLOCK_WALL_SIDE = self.V1_19_2[self.block_type]["BLOCK_WALL_SIDE"]
        BLOCK_WALL_SIDE_TALL = self.V1_19_2[self.block_type]["BLOCK_WALL_SIDE_TALL"]
        ITEM_WALL = self.V1_19_2[self.block_type]["ITEM_WALL"]
        BLOCKSTATES = self.V1_19_2[self.block_type]["BLOCKSTATES"]

        cf.add_mod_blocks(f"{BLOCK_NAME}_bottom_left", MOD_BLOCKS_CODE, self.block_type)
        cf.add_models_block(f"{BLOCK_NAME}_inventory", BLOCK_WALL_INVENTORY)
        cf.add_models_block(f"{BLOCK_NAME}_post", BLOCK_WALL_POST)
        cf.add_models_block(f"{BLOCK_NAME}_side", BLOCK_WALL_SIDE)
        cf.add_models_block(f"{BLOCK_NAME}_side_tall", BLOCK_WALL_SIDE_TALL)
        cf.add_models_item(BLOCK_NAME, ITEM_WALL)
        cf.add_blockstates(BLOCK_NAME, BLOCKSTATES)

        cf.add_lang(f"block.{self.mod_id}.{BLOCK_NAME}",
                    ' '.join([i.capitalize() for i in BLOCK_NAME.split('_')]))
    

    
    def get_block_name(self):
        name = self.name.capitalize()
        
        if self.name[-1] == 's' and self.name.find('Glass') == -1:
            name = self.name = self.name[0:-1].lower()
    
        return name + '_' + self.block_type


#snow_block = Blocks("snow_block", texture_name='snow')

#snow_block.create_wooden_button()
#snow_block.create_door()
#snow_block.create_fence_gate()
#snow_block.create_fence()
#snow_block.create_all_pressure_plate()
#snow_block.create_sign("OAK")
#snow_block.create_slab()
#snow_block.create_stairs()
#snow_block.create_trapdoor()
#snow_block.create_wall()

'''
MOD_BLOCK_CODE = f"""public static final Block {self.name.upper()}_{block_type.upper()} = 
                    create{block_variant.capitalize()}{block_type.capitalize()}
                    ({self.name.upper()}, {self.tab});"""
'''

