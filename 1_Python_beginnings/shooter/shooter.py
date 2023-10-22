import pygame as p
import random as r
import math as m
p.init()


oknowid = 1200
oknohei = 600
okno = p.display.set_mode((oknowid,oknohei))
back = p.image.load('images.jpg')
backwh = 600


pics = [p.image.load('player.png'),p.image.load('bullet.png'),p.image.load('bug.png'),p.image.load('bug2.png'),p.image.load('bug3.png'),p.image.load('target.png'),p.image.load('heart.png'),p.image.load('bug_dead.png'),p.image.load('bug2_dead.png'),p.image.load('blood.png'),p.image.load('blood2.png'),p.image.load('bug3_dead.png')]


class Hero:
	def __init__(self,icon,wh):
		self.icon = icon
		self.mainicon = self.icon
		self.iconw = self.mainicon.get_width()/2
		self.iconh = self.mainicon.get_height()/2
		self.wh = wh
		self.x = (oknowid - self.wh)/2+self.iconw
		self.y = (oknohei - self.wh)/2+self.iconh
		self.rot = 0
		self.speed = 2
		self.left = False
		self.top = False
		self.right = False
		self.down = False
		self.health = 500
		self.maxhealth = self.health
		self.reccol = (255,0,0)
		self.linw = 50
		self.recw = 50
		self.reclinh = 6
		self.reclinx = self.x-self.iconw+(self.wh-self.linw)/2
		self.recliny = self.y-self.iconh-10
		
	def draw(self):
		global play 
		if(self.left == True):
			self.x -= self.speed
		if(self.right == True):
			self.x += self.speed
		if(self.top == True):
			self.y -= self.speed
		if(self.down == True):
			self.y += self.speed
		self.rot = m.atan2(self.y-my,mx-self.x)*180/m.pi
		self.mainicon = p.transform.rotate(self.icon,self.rot)
		self.iconw = self.mainicon.get_width()/2
		self.iconh = self.mainicon.get_height()/2
		
		if(self.x-self.iconw < 0):
			self.x = self.iconw
		elif(self.x+self.iconw > oknowid):
			self.x = oknowid-self.iconw
		if(self.y-self.iconh < 0):
			self.y = self.iconh
		elif(self.y+self.iconh > oknohei):
			self.y = oknohei-self.iconh
		
		for i in range(len(enemies)):
			if((enemies[i].health > 0) and (enemies[i].x > self.x-self.iconw) and (enemies[i].x < self.x+self.iconw) and (enemies[i].y > self.y-self.iconh) and (enemies[i].y < self.y+self.iconh)):
				self.health -= enemies[i].damage
		if(self.health <= 0):
			play = False
		
		for i in range(len(bulletsenem)):
			if((bulletsenem[i].y+bulletsenem[i].iconh/2 < self.y+self.iconh) and (bulletsenem[i].y+bulletsenem[i].iconh/2 > self.y-self.iconh) and (bulletsenem[i].x+bulletsenem[i].iconw/2 < self.x+self.iconw) and (bulletsenem[i].x+bulletsenem[i].iconw/2 > self.x-self.iconw)):
				bulletsenem[i].out = True
				self.health -= 10
		
		
		
		self.reclinx = self.x-self.iconw+(self.wh-self.linw)/2
		self.recliny = self.y-self.iconh-10
		self.recw = self.linw/self.maxhealth*self.health
		
		

class Heal:
	def __init__(self,w,h,icon,heal):
		self.w = w
		self.h = h
		self.x = r.randint(self.w,oknowid-self.w*2)
		self.y = r.randint(self.h,oknohei-self.h*2)
		self.icon = icon
		self.heal = heal
		self.out = False
	def draw(self):
		if((player.x > self.x) and (player.x < self.x+self.w) and (player.y > self.y) and (player.y < self.y+self.h)):
			player.health += self.heal
			self.out = True
			if(player.health > player.maxhealth):
				player.health = player.maxhealth

healths = []



player = Hero(pics[0],54)


class Bullet:
	def __init__(self,w,h,rot,icon,cenpx,cenpy):
		self.w = w
		self.h = h
		self.rot = rot
		self.icon = icon
		self.icon = p.transform.rotate(self.icon,self.rot)
		self.iconw = self.icon.get_width()
		self.iconh = self.icon.get_height()
		self.x = cenpx-self.iconw/2
		self.y = cenpy-self.iconh/2
		self.speed = 4
		self.out = False
		
	def draw(self):
		self.x += m.cos(self.rot*m.pi/180)*self.speed
		self.y -= m.sin(self.rot*m.pi/180)*self.speed
		if((self.y+self.iconh <= 0) or (self.y >= oknohei) or (self.x+self.iconw <= 0) or (self.x >= oknowid)):
			self.out = True


bullets = []
bulletsenem = []

class Blood:
	def __init__(self,w,h,icon,enx,eny):
		self.w = w
		self.h = h
		self.x = enx-self.w/2
		self.y = eny-self.h/2
		self.icon = icon

bloods = []







class Enemy:
	def __init__(self,w,h,icon,dicon):
		self.w = w
		self.h = h
		self.d = int(m.sqrt(self.w**2 + self.h**2))
		self.rot = 0
		self.mainicon = icon
		self.icon = self.mainicon
		self.iconw = self.icon.get_width()
		self.iconh = self.icon.get_height()
		self.x = r.randint(-0.5*oknowid,1.5*oknowid)
		if(self.x+self.d>0 and self.x<oknowid):
			self.y = r.choice([r.randint(-0.5*oknohei,-self.d),r.randint(oknohei,1.5*oknohei)])
		else:
			self.y = r.randint(-0.5*oknohei,1.5*oknohei)
		self.speed = 1
		if(icon == pics[2]):
			self.health = 1
			self.damage = 3
			self.buls = 50
		elif(icon == pics[3]):
			self.health = 2
			self.damage = 2
			self.buls = 100
		elif(icon == pics[4]):
			self.health = 3
			self.damage = 1
			self.buls = 150
		self.deathicon = dicon
		self.firstdeath = True
		self.waitforbuls = 0
	def draw(self):
		self.waitforbuls += 1
		if((self.waitforbuls >= self.buls) and (self.health > 0)):
			self.waitforbuls = 0
			bulletsenem.append(Bullet(34,8,self.rot,pics[1],self.x,self.y))
		if(self.health > 0):
			self.rot = m.atan2(self.y-player.y,player.x-self.x)*180/m.pi
			self.x += self.speed*m.cos(self.rot*m.pi/180)
			self.y -= self.speed*m.sin(self.rot*m.pi/180)
			self.mainicon = p.transform.rotate(self.icon,self.rot)
			self.iconw = self.mainicon.get_width()/2
			self.iconh = self.mainicon.get_height()/2
			
			for i in range(len(bullets)):
				if((bullets[i].y+bullets[i].iconh/2 < self.y+self.iconh/2) and (bullets[i].y+bullets[i].iconh/2 > self.y-self.iconh/2) and (bullets[i].x+bullets[i].iconw/2 < self.x+self.iconw/2) and (bullets[i].x+bullets[i].iconw/2 > self.x-self.iconw/2)):
					bullets[i].out = True
					self.health -= 1
					if(self.icon == pics[4]):
						if(self.health == 2):
							bloods.append(Blood(41,15,pics[9],self.x,self.y))
						elif(self.health == 1):
							bloods.append(Blood(60,35,pics[10],self.x,self.y))
					elif(self.icon == pics[3]):
						if(self.health == 1):
							bloods.append(Blood(41,15,pics[9],self.x,self.y))
					
					
		elif((self.health <= 0) and (self.firstdeath == True)):
			self.firstdeath = False
			self.mainicon = p.transform.rotate(self.deathicon,self.rot)



count = 0
over = 3

enemies = []
enemdeth = 0
for i in range(over):
	choice = r.randint(1,3)
	if(choice == 1):
		enemies.append(Enemy(48,56,pics[2],pics[7]))
	elif(choice == 2):
		enemies.append(Enemy(58,54,pics[3],pics[8]))
	elif(choice == 3):
		enemies.append(Enemy(114,58,pics[4],pics[11]))

level = 1
timer = 0
p.display.set_caption('Уровеь: '+str(level))
play = True
while(play == True):
	for event in p.event.get():
		if(event.type == p.QUIT):
			play = False
		if(event.type == p.KEYDOWN):
			if(event.key == p.K_a):
				player.left = True
			if(event.key == p.K_w):
				player.top = True
			if(event.key == p.K_d):
				player.right = True
			if(event.key == p.K_s):
				player.down = True
		if(event.type == p.KEYUP):
			if(event.key == p.K_a):
				player.left = False
			if(event.key == p.K_w):
				player.top = False
			if(event.key == p.K_d):
				player.right = False
			if(event.key == p.K_s):
				player.down = False
		if(event.type == p.MOUSEBUTTONDOWN):
			if(event.button == 1):
				bullets.append(Bullet(34,8,player.rot,pics[1],player.x,player.y))
			if(event.button == 3):
				bullets.append(Bullet(34,8,player.rot,pics[1],player.x,player.y))
	
	okno.blit(back,(0,0))
	okno.blit(back,(600,0))
	
	mx = p.mouse.get_pos()[0]
	my = p.mouse.get_pos()[1]
	
	
	for i in range(len(bloods)):
		okno.blit(bloods[i].icon, (bloods[i].x,bloods[i].y))
	for i in range(len(bloods)-20):
		del bloods[0]
		
	
	for i in range(len(enemies)):
		if(enemies[i].health <= 0):
			enemies[i].draw()
			okno.blit(enemies[i].mainicon, (enemies[i].x-enemies[i].iconw,enemies[i].y-enemies[i].iconh))
	for i in range(enemdeth-20):
		del enemies[0]
		enemdeth -= 1
	
	
	
	
	
	for i in range(len(healths)-1,-1,-1):
		healths[i].draw()
		okno.blit(healths[i].icon, (healths[i].x,healths[i].y))
		if(healths[i].out == True):
			del healths[i]
	
	
	player.draw()
	okno.blit(player.mainicon, (player.x-player.iconw,player.y-player.iconh))
	
	
	
	for i in range(len(bullets)-1,-1,-1):
		bullets[i].draw()
		okno.blit(bullets[i].icon, (bullets[i].x,bullets[i].y))
		if(bullets[i].out == True):
			del bullets[i]
	for i in range(len(bulletsenem)-1,-1,-1):
		bulletsenem[i].draw()
		okno.blit(bulletsenem[i].icon, (bulletsenem[i].x,bulletsenem[i].y))
		if(bulletsenem[i].out == True):
			del bulletsenem[i]
	
	for i in range(len(bullets)-1,-1,-1):
		for o in range(len(bulletsenem)-1,-1,-1):
			if((bullets[i].y+bullets[i].iconh/2 < bulletsenem[o].y+bulletsenem[o].iconh/2) and (bullets[i].y+bullets[i].iconh/2 > bulletsenem[o].y-bulletsenem[o].iconh/2) and (bullets[i].x+bullets[i].iconw/2 < bulletsenem[o].x+bulletsenem[o].iconw/2) and (bullets[i].x+bullets[i].iconw/2 > bulletsenem[o].x-bulletsenem[o].iconw/2)):
				del bullets[i]
				del bulletsenem[o]
				break
	
	
	timer += 1
	
	
	if((count >= over) or (timer >= 1500)):
		timer = 0
		over += 1
		count = 0
		level += 1
		p.display.set_caption('Уровеь: '+str(level))
		for i in range(over):
			choice = r.randint(1,3)
			if(choice == 1):
				enemies.append(Enemy(48,56,pics[2],pics[7]))
			elif(choice == 2):
				enemies.append(Enemy(58,54,pics[3],pics[8]))
			elif(choice == 3):
				enemies.append(Enemy(114,58,pics[4],pics[11]))
		ch = r.randint(0,2)
		if(ch == 1):
			healths.append(Heal(25,25,pics[6],r.uniform(0,1)*player.maxhealth))
		'''print(ch)'''
		
	
	
	
	
	for i in range(len(enemies)-1,-1,-1):
		if(enemies[i].health > 0):
			enemies[i].draw()
			okno.blit(enemies[i].mainicon, (enemies[i].x-enemies[i].iconw,enemies[i].y-enemies[i].iconh))
			if(enemies[i].health == 0):
				enemies[i].health -= 1
				enemdeth += 1
				count += 1
	
	
	okno.blit(pics[5], (mx-16,my-16))
	
	p.draw.rect(okno, player.reccol, (player.reclinx, player.recliny, player.linw, player.reclinh), 1)
	p.draw.rect(okno, player.reccol, (player.reclinx, player.recliny, player.recw, player.reclinh), 0)
	
	p.display.update()
	p.time.delay(16)













