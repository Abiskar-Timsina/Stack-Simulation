import pygame.freetype
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from elements import Render

def main():
	render_obj = Render()

	pygame.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption('Stack Simulation')
	display = (800,600)
	window = pygame.display.set_mode(display,DOUBLEBUF|OPENGL) #clearing the default buffer
	
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	
	gluPerspective(45, (display[0]/display[1]), 0.5, 50.0) #forced perspective
	glTranslatef(-0.5,-5,-15)

	values  = ["5","6","7","8"] # redundant values as of now, must be input from the user later

	run = True

	while run:
		clock.tick(120)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		render_obj.stack_box()

		'''Basic Pixel Animation (Sliding)'''
		
		# x- 385, y-60 the position for the text to be centered 
		for index,value in enumerate(values):
			for i in range(60):
				render_obj.stack_box()
				render_obj.display_text(385, (60*index)-(i*index), value.zfill(2))
				pygame.display.flip()
				pygame.time.wait(1)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		
		'''end of animation'''
			
			pygame.display.flip()
			window.fill((0,0,0))

		pygame.display.flip() #update the screen .update has a bug! Use .flip instead


	pygame.quit()

if __name__ == "__main__":
	main()