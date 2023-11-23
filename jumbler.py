import os
import pygame
import random

url = input("image path:\n")

image = pygame.image.load(url)

for x in range(image.get_width()):
	for y in range(image.get_height()):
		input_colour = image.get_at([x, y])
		input_colour = [input_colour[0], input_colour[1], input_colour[2]]
		
		if random.randint(0, 1) == 0:
			input_colour[0] = 255-input_colour[0]

			input_colour[1] = 255-input_colour[1]

			input_colour[2] = 255-input_colour[2]

			image.set_at([x, y], input_colour)


print("done")

pygame.image.save(image,  url.replace(".", "_JUMBLED."))