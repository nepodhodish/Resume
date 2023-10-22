# -*- coding: utf-8 -*-

import pygame as p
import random as r
import math as m

p.init()
okno = p.display.set_mode((400,500))
bg = p.image.load('bg1.png')
f1 = p.font.Font('FB.ttf',50)
f2 = p.font.Font('FB.ttf',42)
f3 = p.font.Font('FB.ttf',25)
f4 = p.font.Font('FB.ttf',21)

class Earth:
	def __init__(self,img,x):
		self.img = p.image.load(img)
		self.x = x
		self.y = 420
		self.xx = 1.5
	def draw(self):
		if(Flappy.start != 2):
			self.x -= self.xx
			if(self.x <=-24):
				self.x = 408


earth = []
for i in range(18):
	earth.append(Earth('earth.png',24*i))

class Pipes:
	def __init__(self,img1,y1,img2,x):
		self.img1 = p.image.load(img1)
		self.y1 = y1
		self.img2 = p.image.load(img2)
		self.y2 = self.y1+440
		self.x = x
		self.xx = 1.5
		self.out = False
		self.score = 0
	def __del__(self):
		pass
	def draw(self):
		if(Flappy.start == 1):
			self.x -= self.xx
			if(self.x <= -52):
				self.out = True
			if((self.x+52 > 180-self.xx/2) and (self.x+52 < 180+self.xx/2)):
				self.score+=1


pipes = []
x = 500
y1 = r.randint(-290,-50)
pipes.append(Pipes('2.png',y1,'1.png',x))
y1 = r.randint(-290,-50)
pipes.append(Pipes('2.png',y1,'1.png',x+200))
y1 = r.randint(-290,-50)
pipes.append(Pipes('2.png',y1,'1.png',x+400))






class Bird:
	def __init__(self,x,y,img1,img2,img3,img4):
		self.x = x
		self.y = y
		self.schet = 0
		self.vy = 0
		self.img1 = p.image.load(img1)
		self.img2 = p.image.load(img2)
		self.img3 = p.image.load(img3)
		self.img4 = p.image.load(img4)
		self.imgitog = self.img1
		self.img = 1
		self.deg = 0
		self.vdeg = 0
		self.vvdeg = 0
		self.xx = 13
		self.yy = 18
		self.start = 0
		self.tring = 0
		self.result = 'Press space to continue'
	def draw(self):
		if(self.start == 0):
			self.schet += 3
			if(self.schet >= 360):
				self.schet = 0
			self.y += m.sin(self.schet/180*m.pi)*0.5
			  
		elif(self.start == 1):
			self.result = ''
			self.vy+=0.4 
			if(self.vy >= 7):
				self.vy = 7  #скорость падения 
			self.y+=self.vy
			if(self.vy >= 3):
				self.vvdeg = 0.4 #скорость поворота 
			elif(self.vy < 3):
				self.vvdeg = 0
			self.vdeg-=self.vvdeg
			self.deg+=self.vdeg
			if(self.deg <= 10):
				self.vvdeg = 0.6
			if(self.deg <= -90):
				self.deg = -90
			
			self.img += 1
			if(self.img >= 1)and(self.img < 4):
				self.imgitog = self.img1
			elif(self.img >= 4)and(self.img < 7):
				self.imgitog = self.img2
			elif(self.img >= 7)and(self.img < 10):
				self.imgitog = self.img3
			elif(self.img >= 10)and(self.img <= 12):
				self.imgitog = self.img4
				if(self.img == 12):
					self.img = 1
			if(self.deg == -90):
				self.imgitog = self.img1
			self.imgitog = p.transform.rotate(self.imgitog, self.deg)
			if(earth[2].y <= self.y+self.yy):
				self.Off()
			for i in range(3):
				if((pipes[i].x+52 > self.x-self.xx) and (pipes[i].x < self.x+self.xx) and ((pipes[i].y1+310 > self.y-self.yy) or (pipes[i].y2 < self.y+self.yy))):
					self.Off()
					pass
	def Off(self):
		self.start = 2
		self.tring = 1
		self.result = 'Press space to continue'









Flappy = Bird(180,230,'bird1.png','bird2.png','bird3.png','bird4.png')





itog = '0'

play = True
while(play == True):
	for event in p.event.get():
		if(event.type == p.QUIT):
			play = False
		if(event.type == p.KEYDOWN):
			if(event.key == 32):
				Flappy.vy = -7
				Flappy.deg = 30
				Flappy.vdeg = 0
				if(Flappy.tring == 0):
					Flappy.start = 1
				elif(Flappy.tring == 1):
					Flappy.tring = 0
					Flappy.start = 0
					Flappy.y = 230
					Flappy.imgitog = Flappy.img1
					itog = '0'
					for i in range(len(pipes)):
						del pipes[0]
					y1 = r.randint(-290,-50)
					pipes.append(Pipes('2.png',y1,'1.png',x))
					y1 = r.randint(-290,-50)
					pipes.append(Pipes('2.png',y1,'1.png',x+222))
					y1 = r.randint(-290,-50)
					pipes.append(Pipes('2.png',y1,'1.png',x+444))
	okno.blit(bg,(0,0))
	
	if(Flappy.start == 0):
		Flappy.draw()
		okno.blit(Flappy.imgitog,(Flappy.x-17,Flappy.y-12))
		for i in range(len(earth)):
			earth[i].draw()
			okno.blit(earth[i].img,(earth[i].x,earth[i].y))
		x1 = 50
		x2 = 52
		for i in range(len(Flappy.result)):
			text3 = f3.render(Flappy.result[i], False, (0,0,0))
			text4 = f4.render(Flappy.result[i], False, (255,255,255))
			okno.blit(text3, (x1, 150))
			okno.blit(text4, (x2, 153))
			x1 += 13
			x2 += 13
	elif(Flappy.start == 1 or 2):
		for i in range(len(pipes)):
			pipes[i].draw()
			okno.blit(pipes[i].img1,(pipes[i].x,pipes[i].y1))
			okno.blit(pipes[i].img2,(pipes[i].x,pipes[i].y2))
			if(pipes[i].out == True):
				pipes[i].out = False
				pipes[i].y1 = r.randint(-290,-50)
				pipes[i].y2 = pipes[i].y1+440
				a = i+2
				if(a == 3):
					a = 0
				elif(a == 4):
					a = 1
				pipes[i].x = pipes[a].x+200
		
		Flappy.draw()
		okno.blit(Flappy.imgitog,(Flappy.x-17,Flappy.y-12))
		
		for i in range(len(earth)):
			earth[i].draw()
			okno.blit(earth[i].img,(earth[i].x,earth[i].y))
			
		itog = str(pipes[0].score + pipes[1].score + pipes[2].score)
		
		
		
		text1 = f1.render(itog, False, (0,0,0))
		text2 = f2.render(itog, False, (255,255,255))
		okno.blit(text1, (200, 100))
		okno.blit(text2, (202, 103))
		
		x1 = 50
		x2 = 52
		for i in range(len(Flappy.result)):
			text3 = f3.render(Flappy.result[i], False, (0,0,0))
			text4 = f4.render(Flappy.result[i], False, (255,255,255))
			okno.blit(text3, (x1, 150))
			okno.blit(text4, (x2, 153))
			x1 += 13
			x2 += 13
		
		
		

	p.display.update()
	p.time.delay(16)
