from turtle import *
hideturtle()
shape("turtle")
speed(8)
def ft(x) :
	colors=['#E6E6FA','#D8BFD8','#DDA0DD',	'#EE82EE','#DA70D6','#FF00FF','#FF00FF','#BA55D3','#9370DB','#8A2BE2','#9400D3','#9932CC']
	fillcolor(colors[x])
	begin_fill()
	left(45)
	circle(200,90)
	left(90)
	circle(200,90)
	end_fill()
for i in range(12) :
	ft(i)
	left(15)
done()