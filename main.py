import pygame.freetype
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import ctypes

from elements import Render


title = "Stack Simulation"
ctypes.windll.kernel32.SetConsoleTitleW(title)
def main():
	print(f"[INFO] Program Execution Started")
	render_obj = Render()
	pygame.init()
	clock = pygame.time.Clock()
	pygame.display.set_caption(title)
	display = (800,600)
	window = pygame.display.set_mode(display,DOUBLEBUF|OPENGL) #clearing the default GL_COLOR_BUFFER_BIT

	# glClearColor(102/256,78/256,76/256,1)
	# glClearColor(102/256,133/256,134/256,1)
	glClearColor(12/256,10/256,62/256,1)

	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	
	gluPerspective(45, (display[0]/display[1]), 0.5, 50.0) # forced perspective so that the object is rendered at the correct position.
	glTranslatef(-0.5,-5,-15) # The stack is translated to a proper position 

	run = True
	value = " "
	inp_str = " "
	inp_list = []
	while run:
		clock.tick(120)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if event.type ==pygame.KEYDOWN:
				# If the user clicked on the input_box rect.
				if event.key == pygame.K_DOWN:
					render_obj.pop_operation(render_obj,inp_list)

				# elif event.key == pygame.K_UP:
				# 	value += 1

				# 	render_obj.stack_box()
				# 	#  value  = int(input()) # Input from the text field.
				# 	if value == 0: # the condition for the pop button event listener.
				# 		render_obj.pop_operation(render_obj)
				# 	else:
				# 		# pushing items onto the stack
				# 		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				# 		render_obj.stack_box()
				# 		render_obj.push_operation(render_obj,value)
				# 		pygame.display.flip()
					
				# 	#redrawing the stack and adding items onto it.
				# 	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
				# 	render_obj.stack_box()
				# 	pygame.display.flip() #update the screen .update has a bug! Use .flip instead

				elif event.key == pygame.K_RETURN:
					try:
						value = int(inp_str)
						print(f"[INFO] {value} pushed by the user")
						render_obj.stack_box(inp_list)
						inp_str = str()
						inp_list = []

						# pushing items onto the stack
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						render_obj.stack_box(inp_list)
						render_obj.push_operation(render_obj,value,inp_list)
						pygame.display.flip()
						
						#redrawing the stack and adding items onto it.
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						render_obj.stack_box(inp_list)
						pygame.display.flip() #update the screen .update has a bug! Use .flip instead
					except:
						print(f"[ERROR] Input Field Cannot Be Null")
						pygame.display.flip()
						render_obj.display_text(0, 155,R=249,G=86,B=79,text="> Input Field is Null")
						pygame.display.flip()
						pygame.time.wait(1000)
						glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
						
				else:
					try:
						if (chr(event.key).isnumeric()):
							inp_str += chr(event.key)
							inp_list.append(chr(event.key))
							render_obj.stack_box(inp_list)
							pygame.display.flip()
						else:
							print("[ERROR] None Numeric value")

					except:
						print("[ERROR] None Numeric value")


			if event.type == pygame.MOUSEBUTTONDOWN:
				render_obj.pop_operation(render_obj,inp_list)

	
	pygame.quit()

if __name__ == "__main__":
	main()