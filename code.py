import cv2
import numpy as np
import pygame
import os

pygame.init()

os.system("cls")
image = str(input("Image : "))

img = cv2.imread(image)


win = pygame.display.set_mode((img.shape[1],img.shape[0]))

imgbg = pygame.image.load(image)


list_ = []
run = True
r = 0
while run and (r < 4):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			list_.append(pos[0])
			list_.append(pos[1])
			print(pos)
			r+=1
	win.blit(imgbg,[0,0])
	pygame.display.flip()
pygame.display.quit()

###############################################################################################################

WIDTH = int(input("Width :"))
HEIGHT = int(input("Height :"))
pts1 = np.float32([[list_[0],list_[1]],[list_[2],list_[3]],[list_[4],list_[5]],[list_[6],list_[7]]])
pts2 = np.float32([[0,0],[WIDTH,0],[0,HEIGHT],[WIDTH,HEIGHT]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img , matrix,(WIDTH,HEIGHT))
cv2.imshow("Test",imgOutput)
cv2.waitKey(0)
