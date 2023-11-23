import os
import pygame
import random

url = input("image path:\n")

image = pygame.image.load(url)
new_image = pygame.Surface([image.get_width(), image.get_height()])

neighbor_total =0
threshold = int(input("Threshold:\ndefault is 4:"))
width = image.get_width()

for x in range(width):

	for y in range(image.get_height()):
		input_colour = image.get_at([x, y])
		input_colour = [input_colour[0], input_colour[1], input_colour[2]]
		neighbor_total = 0
		for x_n in range(3):
			for y_n in range(3):
				current_neighbor = image.get_at([((-1)+x_n+x)%image.get_width(), ((-1)+y_n+y)%image.get_height()])
				current_neighbor = current_neighbor[2]+current_neighbor[2]+current_neighbor[2]
				if current_neighbor > input_colour[2] + input_colour[2] + input_colour[2]:
					neighbor_total += 1
		if neighbor_total < threshold:
			new_image.set_at([x, y], [255, 255, 255])

	if random.randint(0, 5) == 4:
		print(f'\r{round((x/width)*100)}%', end='')



print("\ndone")

pygame.image.save(new_image,  url.replace(".", "_SLAMBLED.").replace(".jpg", ".png"))