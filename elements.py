import pygame.freetype
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from constants import verticies_stack,edges_stack,input_box,input_lines,pop_box,pop_lines,divider,divider_lines,surfaces,lines

class Render:
	def __init__(self):
		self.index = 0  # keeps track of items on the screen
		self.pushed_items = list() #keeps track of items on the screen and their coordinates.
		self.time = 0
		self.pop_limit = True


	# Function to generate the basic frame of the Stack.
	def stack_box(self,input_list,R=123/256,G=201/256,B=80/256):
		glColor3f(131/256,144/256,250/256)
		glBegin(GL_QUADS)
		for edge in surfaces:
			for vertex in edge:
				glVertex3fv(verticies_stack[vertex])
		glEnd()
		glColor3f(1,1,1)

		glColor3f(256/256,256/256,256/256)
		#glColor3f(255/256,186/256,8/256)
		glLineWidth(1)
		glBegin(GL_LINES)
		for edge in edges_stack:
			for vertex in edge:
				glVertex3fv(verticies_stack[vertex])
		glEnd()
		glColor3f(1,1,1)

		glLineWidth(3)
		glColor3f(30/256,144/256,255/256)
		glBegin(GL_LINES)
		for edge in input_lines:
			for vertex in edge:
				glVertex2fv(input_box[vertex])
		glEnd()
		glColor3f(1,1,1)

		glColor3f(0.5,0.5,0.5)
		glBegin(GL_LINES)
		for edge in divider_lines:
			for vertex in edge:
				glVertex2fv(divider[vertex])
		glEnd()
		glColor3f(1,1,1)

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
				self.display_text(385,coordinates,R=255,G=255,B=0,text=str(value).zfill(2))
			
			i=10/8
			for n in range(self.index):
				lines_edges = (
						(0,0+i*(n+1),0), # 0
						(1,0+i*(n+1),0), # 2
						#(0,0+i*(n+1),-1), #5
						(-1,+i*(n+1),-1), #4 
						)
				glColor3f(256/256,256/256,256/256)
				#glColor3f(255/256,186/256,8/256)
				glLineWidth(1)
				glBegin(GL_LINES)
				for edge in lines:
					for vertex in edge:
						glVertex3fv(lines_edges[vertex])
				glEnd()
				glColor3f(1,1,1)

		for index,characters in enumerate(input_list):
			self.display_text(100+(index*15),475,characters)


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
	def display_text(self,x, y, text,R=255,G=255,B=255):
		font = pygame.font.SysFont('arial', 32)
		textSurface = font.render(text, True, (R,G,B,1)).convert_alpha()
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
		if len(self.pushed_items) > 7:
			print("[INFO] Stack is Full") 
			render_obj.stack_box(input_list,R=1,G=0)
			self.display_text(0, 155,R=249,G=86,B=79,text="> Stack is Full")
			pygame.display.flip()
			pygame.time.wait(1000)
			return None

		if self.pop_limit:
			for i in range(540-(60*self.index)): 
				render_obj.stack_box(input_list)
				y_posn = 600 - i 
				render_obj.display_text(385, y_posn,R=255,G=255,B=0,text=str(value).zfill(2))
				pygame.display.flip()
				pygame.time.wait(self.time)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

			''' Maybe required | Change later '''
				# pygame.display.flip()
				# window.fill((0,0,0))

			'''end of animation'''

			self.index += 1 # keeps track of items on the screen
			self.pushed_items.append((value,y_posn)) #keeps track of items on the screen and their coordinates.
		else:
			print("[INFO] Stack is Full") # Some sort of better Error handling.
			render_obj.stack_box(input_list,R=1,G=0)
			self.display_text(0, 155, "> Stack is Full")
			pygame.display.flip()

	def pop_operation(self,render_obj,inp_list):
		if self.pushed_items:
			value, coordinates = self.pushed_items.pop()
			print(f"[INFO] {value} popped by the user")

			for i in range(600-coordinates):
				render_obj.stack_box(inp_list,R=249/256,G=86/256,B=79/256)
				y_posn = coordinates + i 
				render_obj.display_text(385, y_posn,R=255,G=255,B=0,text=str(value).zfill(2))
				pygame.display.flip()
				pygame.time.wait(self.time)
				glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
			
			self.index -= 1 # since we removed one item from the stack.
		else:
			print("[INFO] Stack is empty") # Some sort of better Error handling.
			render_obj.stack_box(inp_list,R=1,G=0)
			self.display_text(0, 155,R=249,G=86,B=79,text="> Stack is Empty")
			pygame.display.flip()
