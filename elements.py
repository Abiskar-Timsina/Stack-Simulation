import pygame.freetype
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from constants import verticies_stack,edges_stack,input_box,input_lines,pop_box,pop_lines

class Render:
	def __init__(self):
		self.index = 0  # keeps track of items on the screen
		self.pushed_items = list() #keeps track of items on the screen and their coordinates.


	# Function to generate the basic frame of the Stack.
	def stack_box(self,input_list,R=0,G=1,B=0):
		glBegin(GL_LINES)
		for edge in edges_stack:
			for vertex in edge:
				glVertex3fv(verticies_stack[vertex])
		glEnd()

		glBegin(GL_LINES)
		for edge in input_lines:
			for vertex in edge:
				glVertex2fv(input_box[vertex])
		glEnd()

		glColor3f(R,G,B)
		glBegin(GL_QUADS)
		for edge in pop_lines:
			for vertex in edge:
				glVertex2fv(pop_box[vertex])
		glEnd()
		glColor3f(1,1,1)

		''' If items have been pushed onto the stack, render them without animating them.'''
		if self.pushed_items:
			for value,coordinates in self.pushed_items:
				self.display_text(385,coordinates,str(value).zfill(2))

		for index,characters in enumerate(input_list):
			self.display_text(100+(index*15),475,characters)
			print(f"From the stack {characters} -> {input_list}")

		# Text
		self.display_text(95, 355, text= "POP")
		self.display_text(35, 520, text= "PUSH TO STACK:")
		self.display_text(75, 255, text= "Console:")


	# Function to generate individual block for each item on the stack.
	# Not yet used, another implementation may be better.
	def element_box(self):
		glBegin(GL_LINES)
		for edge in edges_element:
			for vertex in edge:
				glVertex3fv(verticies_element[vertex])
		glEnd()

	# Function to render text onto the screen at X,Y positions.
	def display_text(self,x, y, text):
		font = pygame.font.SysFont('arial', 32)
		textSurface = font.render(text, True, (255,255,0,255)).convert_alpha()
		textData = pygame.image.tostring(textSurface, "RGBA", True)
		glWindowPos2d(x, y)
		glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)


	# Function to add items to the item stack and animate them.
	def push_operation(self,render_obj,value,input_list):
		'''Basic Pixel Animation (Top Down)
			# x- 385, y- 60 the position for the text to be centered 


			In range(540-(60*self.index)) becuase, 
			Resolution of the Console = 800x600; 600 in the y axis,
			the first position is going to be 60 units above 0 so,
			simple mathematics,

			600 - 60 = 540;
			now, each additional item is place 60 units above the previou,
			thus,
			600 - 60*n = posn

			we start at 540 because the index is 0 initially.

		'''
		for i in range(540-(60*self.index)): 
			render_obj.stack_box(input_list)
			y_posn = 600 - i 
			render_obj.display_text(385, y_posn, str(value).zfill(2))
			pygame.display.flip()
			pygame.time.wait(1)
			glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

			''' Maybe required | Change later '''
				# pygame.display.flip()
				# window.fill((0,0,0))

			'''end of animation'''

		self.index += 1 # keeps track of items on the screen
		self.pushed_items.append((value,y_posn)) #keeps track of items on the screen and their coordinates.

	def pop_operation(self,render_obj,inp_list):
		if self.pushed_items:
			value, coordinates = self.pushed_items.pop()

			for i in range(600-coordinates):
				render_obj.stack_box(inp_list,R=1,G=0)
				y_posn = coordinates + i 
				render_obj.display_text(385, y_posn, str(value).zfill(2))
				pygame.display.flip()
				pygame.time.wait(1)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			
			self.index -= 1 # since we removed one item from the stack.
		else:
			print("Stack is empty") # Some sort of better Error handling.
