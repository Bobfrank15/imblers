import os
import pygame
import random
import math

url = input("image path:\n")

image = pygame.image.load(url)
new_image = pygame.Surface([image.get_width(), image.get_height()])

neighbor_total =0
colours = [[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [0, 255, 255], [255, 0, 255], [255, 255, 0],[125, 0, 0], [0, 125, 0], [0, 0, 125], [0, 125, 125], [125, 0, 125], [125, 125, 0]]
width = image.get_width()

def TDDistance(point_a, point_b):
	return math.sqrt(((point_a[0]-point_b[0])**2) + ((point_a[1]-point_b[1])**2) + ((point_a[2]-point_b[2])**2))

def GetClosest(point, list):
	closest_point = 0
	shortest_distance = 9999999
	for index, l_point in enumerate(list):
		current_distance = TDDistance(point, l_point)
		if shortest_distance > current_distance:
			closest_point = index
			shortest_distance = current_distance
	return closest_point
	

for x in range(width):

	for y in range(image.get_height()):
		input_colour = image.get_at([x, y])
		input_colour = [input_colour[0], input_colour[1], input_colour[2]]
		neighbor_total = 0
		best_index = GetClosest(input_colour, colours)

		new_image.set_at([x, y], colours[best_index])

	if random.randint(0, 5) == 4:
		print(f'\r{round((x/width)*100)}%', end='')



print("\ndone")

pygame.image.save(new_image,  url.replace(".", "_SLAMBLED.").replace(".jpg", ".png"))