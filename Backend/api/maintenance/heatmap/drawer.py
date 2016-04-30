#/usr/bin/python3
# -!- encoding:utf8 -!-

# ---------------------------- IMPORTS

from PIL import Image, ImageDraw, ImageFont
import sys, json, os, math

from ...fs.fs import load_heatmap_psd, list_heatmap_psd, load_heatmap, load_database_psd
from ...printer.printer import print_progress

# ---------------------------- CONFIGURATION

# image width
IMG_WIDTH = 5000 # pixels
# image height
IMG_HEIGHT = 5000 # pixels
# coordinates boundaries
MAX_LON = 5.067  # degrees
MIN_LON = 4.681  # degrees
MAX_LAT = 45.917 # degrees
MIN_LAT = 45.55  # degrees
# longitude scale
LON_TO_X = IMG_WIDTH / (MAX_LON - MIN_LON)
# latitude scale
LAT_TO_Y = IMG_HEIGHT / (MAX_LAT - MIN_LAT)
# pen colors
BG_COLOR = (255, 255, 255, 0)
STREET_COLOR = (0, 0, 0, 0)
INTERSECT_COLOR = (255, 0, 0, 128)
HM_INTERS_COLOR = (0, 0, 255, 128)
CRIT_LOCA_COLOR = (0, 102, 0, 128)

# ---------------------------- FUNCTIONS
#
#   TODO : doc
#
def scale_point(lon, lat):
    x = LON_TO_X * (lon - MIN_LON)
    y = LAT_TO_Y * (MAX_LAT - lat)
    return (math.floor(x), math.floor(y)) 
#
#   TODO : doc
#
def draw_grid_data(draw, grid_basename):
    streets = load_heatmap_psd(grid_basename)
    draw_streets(draw, streets)
#
#   TODO : doc
#
def draw_heatmap_data(draw, heatmap_basename, criteria_name):
    data = load_heatmap(heatmap_basename, criteria_name)
    draw_heatmap(draw, data['heatmap'])
#
#   TODO : doc
#
def draw_criteria_data(draw, criteria_name):
    print('[drawer.py]> drawing criteria elements...')
    data = load_database_psd(criteria_name)
    for obj in data:
        x, y = scale_point(obj['coordinates']['lon'], obj['coordinates']['lat'])
        draw_square(draw, x, y, outline=CRIT_LOCA_COLOR)
    print('[drawer.py]> done !')
#
#   TODO : doc
#
def draw_streets(draw, streets):
    print('[drawer.py]> drawing grid elements...')
    streets_len = len(streets)
    for i in range(streets_len):
        print_progress(i, streets_len)
        draw_multi_line(draw, streets[i]['coordinates'])
    print('[drawer.py]> done !')
#
#   TODO : doc
#
def draw_heatmap(draw, triples):
    print('[drawer.py]> drawing heatmap elements...')
    triples_len = len(triples)
    for i in range(triples_len):
        print_progress(i, triples_len)
        draw_heatmap_triple(draw, triples[i])
    print('[drawer.py]> drawing heatmap elements...done !')
#
#   TODO : doc
#
def draw_multi_line(draw, points):
    # on dessine les segments
    x, y = scale_point(points[0][0], points[0][1])
    draw_point(draw, x, y)
    for i in range(len(points)-1) :
        x1, y1 = scale_point(points[i][0], points[i][1])
        x2, y2 = scale_point(points[i+1][0], points[i+1][1])
        draw_line(draw, x1, y1, x2, y2)
        draw_point(draw, x2, y2)
#
#   TODO : doc
#
def draw_heatmap_triple(draw, triple):
    x, y = scale_point(triple[0], triple[1])
    mark = '%.0f' % triple[2]
    draw_square(draw, x, y, outline=HM_INTERS_COLOR)
    draw_text(draw, x, y, mark)

#
#   TODO : doc
#
def draw_line(draw, x1, y1, x2, y2):
    #print('drawing (%s,%s,%s,%s)' % (x1,y1,x2,y2)) # debug do not uncomment !
    draw.line((x1,y1,x2,y2), fill=STREET_COLOR)
#
#   TODO : doc
#
def draw_point(draw, x, y, px_radius=1): 
    draw.ellipse([(x-px_radius, y-px_radius),
                  (x+px_radius, y+px_radius)], 
                  fill=None , outline=INTERSECT_COLOR)
#
#   TODO : doc
#
def draw_square(draw, x, y, px_half_side=1, fill=None, outline=None):
    draw.rectangle([(x-px_half_side, y-px_half_side),
                    (x+px_half_side, y+px_half_side)],
                    fill=fill, outline=outline)

def draw_text(draw, x, y, text):
    font = ImageFont.load_default()
    draw.text((x,y), text, (0,0,0), font=font)
#
#   TODO : doc
#
def img_init():
    im = Image.new('RGBA', (IMG_WIDTH, IMG_HEIGHT), BG_COLOR) 
    draw = ImageDraw.Draw(im)
    return im, draw
#
#   TODO : doc
#
def draw_map_part(grid_basename):
    print('[drawer.py]> computing map_part for %s...' % grid_basename)
    # init image
    im , draw = img_init()
    # draw image part for given basename
    draw_grid_data(draw, grid_basename)
    # show image
    im.show()
    print('[drawer.py]> done !')
#
#   TODO : doc
#
def draw_map():
    print('[drawer.py]> computing full map...')
    # init image
    im , draw = img_init()
    # for each basename draw image part
    basenames = list_heatmap_psd()
    for basename in basenames:
        draw_grid_data(draw, basename)
    # show image
    im.show()
    print('[drawer.py]> done !')

def draw_heatmap_part(grid_basename, heatmap_basename, criteria_name):
    print('[drawer.py]> computing %s heatmap for %s...' % (grid_basename, criteria_name))
    # init image
    im , draw = img_init()
    # draw grid
    draw_grid_data(draw, grid_basename)
    # draw heatmap on previously drawn grid
    draw_heatmap_data(draw, heatmap_basename, criteria_name)
    # draw criteria data
    draw_criteria_data(draw, criteria_name)
    # show image
    im.show()
    print('[drawer.py]> done !')