from matplotlib import pyplot
from matplotlib.patches import Rectangle

from worldmaparea import Map


map = Map()
map.parse_worldmaparea()


def on_mouse_move(event):
    print('COORDS:',event.xdata, event.ydata)
    map.coords_to_zone(event.ydata,event.xdata, 0)


# Specify hardcoded map ID to process
target_map_id = 1
target_map_name = "Kalimdor"
# target_map_id = 0
# target_map_name = "Azeroth"

# Rectangles dict for each zone
rectangles = dict()

# Create dictionary of limits for figure
limits = {
    "x_lim_positive": 0,
    "x_lim_negative": 0,
    "y_lim_positive": 0,
    "y_lim_negative": 0,
}

for i, zone in enumerate(map):
    # Skip header
    if i == 0:
        continue

    # Set zone properties
    area_name = zone.area_name
    x1 = zone.x1
    x2 = zone.x2
    y1 = zone.y1
    y2 = zone.y2

    # Skip where map ID doesn't equal the target
    if int(zone.map_id) != target_map_id:
        continue

    # Grab target map and set axis limits
    if area_name == target_map_name:
        limits["x_lim_positive"] = x1 + 1000
        limits["x_lim_negative"] = x2 - 1000
        limits["y_lim_positive"] = y1 + 1000
        limits["y_lim_negative"] = y2 - 1000

    # Make the zone rectangle
    rectangle = Rectangle((x1, y1),
                          zone.width,
                          zone.height,
                          linewidth=1,
                          edgecolor='r',
                          facecolor='none')

    rectangles[area_name] = rectangle

# Initialize matplotlib figure
fig = pyplot.figure()
ax = fig.add_subplot()

# Add generated rectangles and area name to figure
for area_name, rectangle in rectangles.items():
    ax.add_patch(rectangle)
    ax.add_artist(rectangle)
    rx, ry = rectangle.get_xy()
    cx = rx + rectangle.get_width()/2.0
    cy = ry + rectangle.get_height()/2.0
    ax.annotate(area_name, (cx, cy), color='red', weight='bold', 
                fontsize=6, ha='center', va='center')

# Set figure axis limits
pyplot.xlim(limits["x_lim_negative"], limits["x_lim_positive"])
pyplot.ylim(limits["y_lim_negative"], limits["y_lim_positive"])

pyplot.connect('button_press_event',on_mouse_move)
pyplot.show()
