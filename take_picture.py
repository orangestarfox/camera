import pygame
import pygame.camera
from pygame import PixelArray
import time
import sys
from pygame.locals import *
import cv2
import dip
import numpy as np

	

"""
camera init
"""
pygame.camera.init()
cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
cam.start()


screen = pygame.display.set_mode( (500, 500) )

i = 0;

while 1:
    img = cam.get_image()
    arr=pygame.surfarray.array3d(img)
    k=np.array([[0,-1,0],[-1,4,-1],[0,-1,0]])
    im=dip.draw(arr)
    img=pygame.surfarray.make_surface(im)
    screen.blit(img, (0,0))
    pygame.display.flip()
    for event in pygame.event.get():
	if event.type ==pygame.QUIT:
            sys.exit()
	if event.type==KEYDOWN:
		print(event.key)
		if event.key==274:
			 pygame.image.save(img, "picture.bmp")
pygame.camera.quit()
