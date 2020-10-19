import sys, random, pygame, os
from SimpleDrawEngine import *

## Limpador de tela multiplataforma Magoninho Gamer versão 1.2
def limpa_tela():
    os.system('cls' if os.name=='nt' else 'clear')

limpa_tela()


def main():
	pygame.init()
	old_notes = []
	N = 200
	white = (255, 255, 255)
	black = (0,0,0)
	red = (255, 0, 0)
	largura, altura = 1980, 1080

	screen = pygame.display.set_mode((largura, altura))
	caption = pygame.display.set_caption("cool")


	angle = random.randint(0, 45)


	# posisão das estrelas
	## estrelas menores
	stars = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(N)
	]
	medium_stars = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(30)
	]
	## estrelas grandes

	big_stars = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(50)
	]

	notes = [
		[random.randint(0, largura), random.randint(0, altura)] for x in range(6)
	]
	astronauts = [
		[random.randint(largura*2, largura*3), random.randint(0, altura)]
	]

	pygame.mixer.init()
	pygame.mixer.music.load('./call-me.wav')
	pygame.mixer.music.play(-1)

	clock = pygame.time.Clock()
	
	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		screen.fill(black)
		


		# Drawinings
		## Stars
		for star in stars:
			Rect(screen, white, (star[0], star[1], 2, 2))
			star[0] -= 0.5
			if star[0] < 0:
				star[0] = largura
		for big_star in big_stars:
			Circle(screen, white, (big_star[0], big_star[1]), 3)
			big_star[0] -= 1
			if big_star[0] < 0:
				big_star[0] = largura
		for medium_star in medium_stars:
			Rect(screen, white, (medium_star[0], medium_star[1], 3, 3))
			medium_star[0] -= 0.8
			if medium_star[0] < 0:
				medium_star[0] = largura
		for astronaut in astronauts:
			Astronaut(screen, "./yellow.png", (astronaut[0], astronaut[1]), (50, 55), angle)
			astronaut[0] -= 1.2
			if astronaut[0] < -100:
				angle = random.randint(0, 45)
				astronaut[0] = largura*4
				astronaut[1] = random.randint(0, altura)
		
		for note in notes:
			Note(screen, "./note.png", (note[0], note[1]), (21, 35))
			

			note[0] -= 1
			if note[0] < -30:
				new_notes = [
					[random.randint(largura, largura*2), random.randint(0, altura)] for x in range(6)
				]

				note[0]= new_notes[0][0]

				
		#sadf
		pygame.display.flip()
main()