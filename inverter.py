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

		new_image.set_at([x, y], [255-input_colour[0], 255-input_colour[1], 255-input_colour[2]])

	if random.randint(0, 5) == 4:
		print(f'\r{round((x/width)*100)}%', end='')



print("\ndone")

pygame.image.save(new_image,  url.replace(".", "_INVERTED.").replace(".jpg", ".png"))