#constants
verticies_stack = (
	(0,0,0), # 0
	(0,10,0), # 1
	(1,0,0), # 2 
	(1,10,0), # 3
	(-1,0,-1), #4 
	(0,0,-1), #5
	(-1,10,-1), #6
	(0,10,-1), #7 
)

edges_stack = (
	(0,1), # connecting 0 and 1 
	(0,2), # connecting 0 and 2 
	(2,3), # connecting 2 and 3 
	(0,4),
	(2,5),
	(4,5),
	(4,6),
	(1,6),
	(5,7),
	(3,7),
	(1,3),
	(6,7),
)

verticies_element = (
	(0,0,0),
	(0,1,0),
	(1,0,0),
	(1,1,0),
)

edges_element = (
	(0,1),
	(0,2),
	(1,3),
)

surfaces = (
	(0,2,4,5),
	(1,3,6,7),
	(0,1,6,4),
	(2,0,3,1),
	(2,3,7,5),
	(4,5,6,7),
	)


input_box = (
	(-7,8.5), # Rect 0
	(-7,9.5), # 1 
 	(-3,9.5), # 2
	(-3,8.5), # 3
	# input box
	)

input_lines = (
	(0,1),
	(0,3),
	(1,2),
	(2,3),
	)

divider = (
	(-2,50),  #vertical line 1
	(-2,-50), #vertical line 2
	(-2,5),	 #horizontal line 1
	(-50,5), #hortizontal line 2
	)

divider_lines = (
	(0,1), #vertical line
	(2,3), # Horizontal line
	) 

pop_box = (
	# POP box
	(-6.5,6), # Rect 0
	(-6.5,7), # 1 
 	(-4,7), # 2
	(-4,6), # 3
	)

pop_lines = (
	#pop box
	(0,1),
	(0,3),
	(1,2),
	(2,3),
	)

lines = (
	(0,1),
	(0,2),
	)