import pygame
from csv import reader
from os import walk


def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(path):
    surface_list = []
    for _,__, img_files in walk(path):
        for image in img_files:
            full_path = f"{path}/{image}"
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

#import_folder('graphics/grass')
#print(import_csv_layout('map/map_FloorBlocks.csv'))