import os
import pygame
import random

url = input("image path:\n")

image = pygame.image.load(url)

flip = True
flop = True

for x in range(image.get_width()):
	flip = flop
	flop = not flop
	for y in range(image.get_height()):
		
		input_colour = image.get_at([x, y])
		input_colour = [125+round(input_colour[0]/2), 125+round(input_colour[1]/2), 125+round(input_colour[2]/2)]
		flip = not flip
		if flip:
			input_colour[0] = 255-input_colour[0]

			input_colour[1] = 255-input_colour[1]

			input_colour[2] = 255-input_colour[2]


		image.set_at([x, y], input_colour)


print("done")

pygame.image.save(image,  url.replace(".", "_JAMBLED.").replace(".jpg", ".png"))