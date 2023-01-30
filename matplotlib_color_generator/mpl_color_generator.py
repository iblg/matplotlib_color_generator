import matplotlib as mpl
import matplotlib.colors as clrs

def get_single_color(cmap_name, val):
    cmap = mpl.cm.get_cmap(cmap_name)
    c = clrs.to_hex(cmap(val), keep_alpha = True)
    return c

