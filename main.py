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
	
	gluPerspective(45, (display[0]/display[1]), 0.5, 50.0) # forced perspective so that the object is rendered at the correct position.
	glTranslatef(-0.5,-5,-15) # The stack is translated to a proper position 

	run = True

	while run:
		clock.tick(120)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

		render_obj.stack_box()
		value  = int(input("Enter a number to push onto the stack: ")) # Input from the text field.

		if value == 0: # the condition for the pop button event listener.
			render_obj.pop_operation(render_obj)
		else:
			# pushing items onto the stack
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			render_obj.stack_box()
			render_obj.push_operation(render_obj,value)
			pygame.display.flip()
		
		#redrawing the stack and adding items onto it.
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
		render_obj.stack_box()
		pygame.display.flip() #update the screen .update has a bug! Use .flip instead


	pygame.quit()

if __name__ == "__main__":
	main()