

import pygame as p
import random as r
import math as m

p.init()
oknox = 640
oknoy = 600
okno = p.display.set_mode((oknox,oknoy))
back = p.image.load('bck.jpg')
f1 = p.font.Font('shrift.ttf',50)
f2 = p.font.Font('shrift.ttf',25)

class Blocks:
	def __init__(self,img ,width,height,starter):
		self.width = width/2
		self.height = height
		if(starter == False):
			self.x = r.randint(-self.width,oknox-self.width)
			self.y = r.randint(0,oknoy-self.height)
		elif(starter == True):
			self.x = (oknox-self.width)/2
			self.y = oknoy-self.height
		self.img = p.image.load(img)
		if(img == 'block2.png'):
			self.broke = 1
		else:
			self.broke = -1
	def draw(self):
		if(((dood.up == True) and (dood.vy > 0) and (dood.way > 0) and (self.broke != 0)) or ((dood.up == False) and (dood.y >= oknoy-dood.height))):
			self.y += dood.vy
		elif(self.broke == 0):
			self.y += 5
		if(self.y > oknoy):
			if(self.broke == 0):
				self.broke = 1
			self.x = r.randint(-self.width,oknox-self.width)
			self.y = r.randint(-300, -self.height)
			
blocks = []
for i in range(49):
	kindblock = r.choice(['block.png','block.png','block.png','block.png','block.png','block2.png'])
	blocks.append(Blocks(kindblock,64,17,False))
blocks.append(Blocks('block.png',64,17,True))

class Doodle:
	def __init__(self,imgright,imgleft,width,height):
		self.width = width
		self.height = height
		self.x = (oknox-self.width)/2
		self.y = oknoy-self.height
		self.centerx = self.x+self.width/2
		self.centery = self.y+self.height/2
		self.imgright = p.image.load(imgright)
		self.imgleft = p.image.load(imgleft)
		self.itogimg = self.imgleft
		self.max = 240
		self.way = 0
		self.vx = 0
		self.vy = 10
		self.ay = -0.15
		self.up = True
		self.text1 = ''
		self.text2 = ''
		self.go = 0
	def draw(self,mx,my):
		self.centerx = self.x+self.width/2
		self.centery = self.y+self.height/2
		self.vx = (mx - self.centerx)/10
		if(self.vx > 0):
			self.itogimg = self.imgright
		elif(self.vx < 0):
			self.itogimg = self.imgleft
		self.x += self.vx
		if(self.up == True):
			self.text1 = ''
			self.text2 = ''
			self.vy += self.ay
			self.y -= self.vy
			if(self.go <= self.max):
				self.go += self.vy
			elif((self.up == True) and (self.vy > 0) and (self.way > 0)):
				self.go += self.vy
			if(self.y <= self.max):
				self.y = self.max
				self.way += self.vy
			if(self.vy <= 0):
				self.way = 0
				for i in range(len(blocks)):
					if((blocks[i].x <= self.x+self.width) and (blocks[i].x+blocks[i].width >= self.x) and (blocks[i].y <= self.y+self.height) and (blocks[i].y >= self.y+self.height+self.vy)):
						self.vy = 10
						if(blocks[i].broke > 0):
							blocks[i].broke-=1
			if(self.y+self.height >= oknoy):
				self.up = False
				self.way = 0
		elif(self.up == False):
			self.vy = -5
			if(self.y < oknoy-self.height):
				self.y -= self.vy
				self.way = 0
			elif(self.y >= oknoy-self.height):
				self.y = oknoy-self.height
				self.way -= self.vy
				if(self.way >= oknoy+100):
					self.vy = 0
					self.text1 = 'Ты проиграл!'
					self.text2 = 'Нажми пробел, чтобы продолжить'
dood = Doodle('doodle_right.png','doodle_left.png',46,45)

monst = []
class Monster:
	def __init__(self,width,height,img1,img2,img3,img4):
		self.width = width
		self.height = height
		self.x = r.randint(-self.width/2,oknox+self.width/2)
		self.y = r.randint(-3000, -2000)
		self.img1 = p.image.load(img1)
		self.img2 = p.image.load(img2)
		self.img3 = p.image.load(img3)
		self.img4 = p.image.load(img4)
		self.itogimg = self.img1
		self.chet = 0
		self.vx = 3
	def draw(self):
		self.x += self.vx
		self.chet += 1
		if(self.chet == 3):
			self.itogimg = self.img1
		elif(self.chet == 6):
			self.itogimg = self.img2
		elif(self.chet == 9):
			self.itogimg = self.img3
		elif(self.chet == 12):
			self.itogimg = self.img4
			self.chet = 0
		if((self.x+self.width >= oknox+self.width/2) or (self.x <= -self.width/2)):
			self.vx = -self.vx
		if(((dood.up == True) and (dood.vy > 0) and (dood.way > 0)) or ((dood.up == False) and (dood.y >= oknoy-dood.height))):
			self.y += dood.vy
		if(self.y >= oknoy):
			self.y = r.randint(-3000,-2000)
		for i in range(len(monst)):
			if((dood.x+dood.width > self.x) and (dood.x < self.x+self.width) and (dood.y < self.y+self.height) and (dood.y+dood.width > self.y)):
				dood.up = False

for i in range(1):
	monst.append(Monster(76,44,'m1.png','m2.png','m3.png','m4.png'))



play = True
level1 = 1000
level2 = 1500
while(play == True):
	for event in p.event.get():
		if(event.type == p.QUIT):
			play = False
		if(event.type == p.KEYDOWN and event.key == 32 and dood.up == False):
			level1 = 1000
			level2 = 1500
			dood.go = 0
			dood.way = 0
			dood.up = True
			dood.vy = 10
			dood.x = (oknox-dood.width)/2
			dood.y = oknoy-dood.height
			for i in range(len(blocks)-1,-1,-1):
				del blocks[i]
			for i in range(49):
				kindblock = r.choice(['block.png','block.png','block.png','block.png','block.png','block2.png'])
				blocks.append(Blocks(kindblock,64,17,False))
			blocks.append(Blocks('block.png',64,17,True))
			for i in range(len(monst)-1,-1,-1):
				del monst[i]
			for i in range(1):
				monst.append(Monster(76,44,'m1.png','m2.png','m3.png','m4.png'))
	
	mx = p.mouse.get_pos()[0] 
	my = p.mouse.get_pos()[1]
	okno.blit(back,(0,0))
	okno.blit(back,(0,512))
	okno.blit(back,(320,0))
	okno.blit(back,(320,512))
	
	for i in range(len(blocks)):
		blocks[i].draw()
		okno.blit(blocks[i].img,(blocks[i].x,blocks[i].y))
	
	if(dood.go >= level1):
		level1 += 1000
		for i in range(len(blocks)):
			if(blocks[i].broke == -1):
				blocks[i].img = p.image.load('block2.png')
				blocks[i].broke = 1
				break
	if(dood.go >= level2):
		level2 += 1500
		monst.append(Monster(76,44,'m1.png','m2.png','m3.png','m4.png'))
	
	dood.draw(mx,my)
	okno.blit(dood.itogimg,(dood.x,dood.y))
	
	for i in range(len(monst)):
		monst[i].draw()
		okno.blit(monst[i].itogimg,(monst[i].x,monst[i].y))
	
	text1 = f1.render(dood.text1, False, (0,0,0))
	text2 = f1.render(dood.text2, False, (0,0,0))
	text3 = f2.render(str(int(dood.go)), False, (0,0,0))
	okno.blit(text1, (200, 120))
	okno.blit(text2, (55, 250))
	okno.blit(text3, (0, 0))
	
	#p.draw.line(okno,(255,0,0),(0,240),(640,240),2)
	
	p.display.update()
	p.time.delay(12)










