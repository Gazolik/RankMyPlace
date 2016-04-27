from PIL import Image, ImageDraw
import sys, json

width=1000
height=1000
lon_max=5.067 #est
lon_min=4.681 #ouest
lat_max=45.917 #nord
lat_min=45.55 #sud
#longitude
scale_x=width/(lon_max-lon_min)
#latitude
scale_y=height/(lat_max-lat_min)

def drawStreets(streets) :
	im = Image.new('RGBA', (width, height), (0, 255, 0, 0)) 
	draw = ImageDraw.Draw(im) 
	for s in streets :
		drawMultiLine(s['coordinates'])
	im.show()

def drawMultiLine(points) :
	for i in range(len(points)-1) :
		drawLine(points[i][0]*scale_x, points[i][1]*scale_y, points[i+1][0]*scale_x, points[i+1][1]*scale_y)
		

def drawLine(x1, y1, x2, y2) : 
	draw.line((x1,y1,x2,y2), fill=128)
	
if len(sys.argv)<2 :
	print("Usage : ./drawer.py nom_fichier")
	exit()
	
with open(sys.argv[1], 'r') as f :
	streets = json.load(f)
	drawStreets(streets)