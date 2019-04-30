
def adjust_height(height):
	print('hello world')
	f= open ("closure.gcode","r")
	g= open ("output.gcode", "w+")
	contents=f.readlines()

	line_number = 0


	for x in contents:
		#print(x)
		#if "Z" in x:
		#	print(x)
		ind=x.find("Z")
		#print (ind)
		if (ind > 0) and (line_number > 6): 
			current_height = float(x[ind+1:-1])
			current_height += height
			g.write(x[:ind+1]+str(current_height)+"\n")
		else: 
			g.write(x)

		line_number += 1

adjust_height(113.5)