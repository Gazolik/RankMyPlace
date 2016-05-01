from ...fs.fs import load_static
from ...fs.fs import dump_static
from ...fs.fs import list_heatmap_grids


def generate_areas():
    """
        TODO : doc
    """
    heatmap_grids = list_heatmap_grids()
    areas = {}
    for i in heatmap_grids:
        name = i
        name = name[0].upper() + name[1:]
        idx = name.find('_')
        if idx != -1:
            name = name[:idx]
        areas[i] = {'name': name, 'imgPath': i + '.png', 'code': i}
    dump_static('areas', areas, indent=2)
