from PIL import Image, ImageDraw
import sys, json, os
from math import floor

# ---------------------------- CONFIGURATION

width=5000
height=5000
lon_max=5.067 #est
lon_min=4.681 #ouest
lat_max=45.917 #nord
lat_min=45.55 #sud
#longitude
scale_x=width/(lon_max-lon_min)
#latitude
scale_y=height/(lat_max-lat_min)
# background color
bgcl = (255, 255, 255, 0)
# pen color
line_pen = (0, 0, 0, 0)
point_pen = (255, 0, 0, 0)
# basedir where data files are stored
basedir = 'psd/'

# ---------------------------- FUNCTIONS

def drawFileData(draw, filename):
    with open(basedir + filename, 'r') as f:
        streets = json.load(f)
        drawStreets(draw, streets)

def drawStreets(draw, streets) :
    for s in streets :
        drawMultiLine(draw, s['coordinates'])

def drawMultiLine(draw, points) :
    # on dessine les segments
    for i in range(len(points)-1) :
        drawLine(
        	draw, 
        	floor((points[i][0]-lon_min)*scale_x), 
        	floor((lat_max-points[i][1])*scale_y), 
        	floor((points[i+1][0]-lon_min)*scale_x), 
        	floor((lat_max-points[i+1][1])*scale_y))

def drawLine(draw, x1, y1, x2, y2) :
    #print('drawing (%s,%s,%s,%s)' % (x1,y1,x2,y2)) # debug do not uncomment !
    draw.line((x1,y1,x2,y2), fill=line_pen)
    # on dessine les points
    draw.point([(x1,y1),(x2,y2)], fill=point_pen)

# ------------------------- SCRIPT

im = Image.new('RGBA', (width, height), bgcl) 
draw = ImageDraw.Draw(im) 

if len(sys.argv)<2 :
	files = os.listdir(basedir)
	for f in files:
		drawFileData(draw, f)
else:
    drawFileData(draw, sys.argv[1])

im.show()
