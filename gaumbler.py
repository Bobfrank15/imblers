import os
import pygame
import random
import math

url = input("image path:\n")

image = pygame.image.load(url)
new_image = pygame.Surface([image.get_width(), image.get_height()])

neighbor_total = [0, 0, 0]
width = image.get_width()
height = image.get_height()

blur_radius = int(input("blur radius:\n"))

image_array = [new_image.get_at([x, y]) for x in range(new_image.get_width()) for y in range(new_image.get_height())]

for x in range(width):

	for y in range(image.get_height()):
		input_colour = image.get_at([x, y])
		input_colour = [input_colour[0], input_colour[1], input_colour[2]]
		neighbor_total = [0, 0, 0]
		for dx in range(-blur_radius, blur_radius):
			for dy in range(-blur_radius, blur_radius ):
				n_x = (dx+x)%(width-1)
				n_y = (dy+y)%(height-1)
				neighbor_colour = image.get_at([n_x, n_y])
				
				neighbor_total[0]+=neighbor_colour[0]
				neighbor_total[1]+=neighbor_colour[1]
				neighbor_total[2]+=neighbor_colour[2]
		
		neighbor_total[0] = round(neighbor_total[0]/((((blur_radius*2))**2)))
		neighbor_total[1] = round(neighbor_total[1]/((((blur_radius*2))**2)))
		neighbor_total[2] = round(neighbor_total[2]/((((blur_radius*2))**2)))
		
		new_image.set_at([x, y], neighbor_total)

	
	print(f'\r{round((x/width)*100)}%', end='')



print("\ndone")

pygame.image.save(new_image,  url.replace(".", f"_GAUMBLER_{blur_radius}.").replace(".jpg", ".png"))