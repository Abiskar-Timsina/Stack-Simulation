import pygame.freetype
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from constants import verticies_stack,edges_stack

class Render:
	def __init__(self):
		pass

	def stack_box(self):
		glBegin(GL_LINES)
		for edge in edges_stack:
			for vertex in edge:
				glVertex3fv(verticies_stack[vertex])
		glEnd()

	def element_box(self):
		glBegin(GL_LINES)
		for edge in edges_element:
			for vertex in edge:
				glVertex3fv(verticies_element[vertex])
		glEnd()

	def display_text(self,x, y, text):
		font = pygame.font.SysFont('arial', 32)
		textSurface = font.render(text, True, (255,255,0,255)).convert_alpha()
		textData = pygame.image.tostring(textSurface, "RGBA", True)
		glWindowPos2d(x, y)
		glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)