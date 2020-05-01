import pygame
from pygame.locals import *
import random
class cubo():
	def __init__(self,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
	def update(self,pos_x,pos_y):
		self.pos_x = pos_x
		self.pos_y = pos_y
def comprobar_localizacion():
	global x_manzana
	global y_manzana
	for i in serpiente:
		if x_manzana == i.pos_x and y_manzana == i.pos_y:
			x_manzana= random.randint(1,11)*50
			y_manzana= random.randint(1,11)*50
			comprobar_localizacion()

canvas = pygame.display.set_mode((1000,1000))
pygame.init()
runnig = True
serpiente = []
x = 500 
y = 500
x_manzana= random.randint(1,11)*50
y_manzana= random.randint(1,11)*50
serpiente.append(cubo(x,y))
vel = 50
direction = ""
while runnig:
	canvas.fill((0,0,0))
	pygame.time.delay(150)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			runnig = False
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		direction = "up"
	if keys[pygame.K_DOWN]:
		direction = "down"
	if keys[pygame.K_LEFT]:
		direction = "left"
	if keys[pygame.K_RIGHT]:
		direction = "right"


	if direction == "up":
		y -= vel
	elif direction == "down":
		y += vel 
	elif direction == "left":
		x -= vel 
	elif direction == "right":
		x += vel
	longitud_serpinete  = len(serpiente)
	
	if x == x_manzana and y == y_manzana:
		serpiente.append(cubo(5000,5000))
		x_manzana= random.randint(1,21)*50
		y_manzana= random.randint(1,21)*50
		comprobar_localizacion()
	if x >= 1000 or y >= 1000 or x <= 0 or y <= 0:
		runnig = False

	for i in range(longitud_serpinete):
		if i != longitud_serpinete-1:
			serpiente[longitud_serpinete - (i+1)].update(serpiente[(longitud_serpinete-i)-2].pos_x,serpiente[(longitud_serpinete -i)-2].pos_y)
	
	count = 0
	for i in serpiente:
		if count != 0:
			if x == i.pos_x and y == i.pos_y:
				runnig = False
		count += 1
	serpiente[0].update(x,y)

	pygame.draw.rect(canvas,(255,0,0),(x_manzana,y_manzana,50,50))

	for i in serpiente:
		pygame.draw.rect(canvas,(0,0,255),(i.pos_x,i.pos_y,50,50))
	pygame.display.flip()

pygame.quit()





		