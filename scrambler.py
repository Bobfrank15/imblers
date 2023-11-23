import os
import pygame
import random

url = input("image path:\n")

image = pygame.image.load(url)

for x in range(image.get_width()):
	for y in range(image.get_height()):
		input_colour = image.get_at([x, y])
		input_colour = [input_colour[0], input_colour[1], input_colour[2]]
		new_colour = []

		num = random.choice(input_colour)
		input_colour.remove(num)
		new_colour.append(num)

		num = random.choice(input_colour)
		input_colour.remove(num)
		new_colour.append(num)

		num = random.choice(input_colour)
		input_colour.remove(num)
		new_colour.append(num)

		new_colour.append(255)

		image.set_at([x, y], new_colour)

print("done")

pygame.image.save(image,  url.replace(".", "_MODIFIED."))