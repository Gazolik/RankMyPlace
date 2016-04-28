#/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------- IMPORTS

from PIL import Image, ImageDraw
import sys, json, os
from math import floor
from ...fs.fs import load_heatmap_psd, list_heatmap_psd

# ---------------------------- CONFIGURATION

# image width
width=5000
# image height
height=5000
# coordinates boundaries
lon_max=5.067  # east
lon_min=4.681  # west
lat_max=45.917 # north
lat_min=45.55  # south
# longitude scale
scale_x=width/(lon_max-lon_min)
# latitude scale
scale_y=height/(lat_max-lat_min)
# background color
bgcl = (255, 255, 255, 0)
# pen colors
line_pen = (0, 0, 0, 0)
point_pen = (255, 0, 0, 0)

# ---------------------------- FUNCTIONS

#
#   TODO : doc
#
def draw_file_data(draw, basename):
    streets = load_heatmap_psd(basename)
    draw_streets(draw, streets)
#
#   TODO : doc
#
def draw_streets(draw, streets) :
    for s in streets :
        draw_multi_line(draw, s['coordinates'])
#
#   TODO : doc
#
def draw_multi_line(draw, points) :
    # on dessine les segments
    for i in range(len(points)-1) :
        draw_line(
        	draw, 
        	floor((points[i][0]-lon_min)*scale_x), 
        	floor((lat_max-points[i][1])*scale_y), 
        	floor((points[i+1][0]-lon_min)*scale_x), 
        	floor((lat_max-points[i+1][1])*scale_y))
#
#   TODO : doc
#
def draw_line(draw, x1, y1, x2, y2) :
    #print('drawing (%s,%s,%s,%s)' % (x1,y1,x2,y2)) # debug do not uncomment !
    draw.line((x1,y1,x2,y2), fill=line_pen)
    # on dessine les points
    draw.point([(x1,y1),(x2,y2)], fill=point_pen)
#
#   TODO : doc
#
def img_init():
    im = Image.new('RGBA', (width, height), bgcl) 
    draw = ImageDraw.Draw(im)
    return im, draw
#
#   TODO : doc
#
def draw_map_part(basename):
    # init image
    im , draw = img_init()
    # draw image part for given basename
    draw_file_data(draw, basename)
    # show image
    im.show()
#
#   TODO : doc
#
def draw_map():
    # init image
    im , draw = img_init()
    # for each basename draw image part
    basenames = list_heatmap_psd()
    for basename in basenames:
        draw_file_data(draw, basename)
    # show image
    im.show()
