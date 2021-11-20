# wow-vanilla-world-coords

An attempt to understand the WoW Vanilla coordinate system.

## Problem

How does one determine the target zone from XYZ world coordinates? Or convert XYZ world coordinates to XY coordinates in a specific zone? For example, in CMaNGOS there are game objects with XYZ coordinates in the database. How can you figure out what zone those world XYZ coordinates are in? There are also teleport spells avilable GM commands with XYZ coordinates, such as `.go -14406.6 419.353 22.3907 0` which teleports the player to Booty Bay. How do you know this is in Stanglethorn Vale?

Short answer... I do not think this is possible. But you can convert from XY zone coordinates to world coordinates. This repo documents some of my research, notes, links, and code to try share some of the information I learned along the way.

## Quick Setup

```none
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you get the following error message when using one of the `generate_zone_map*` files:

> UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.

Install a GUI such as QT5.

```none
pip install PyQt5
```

## File Summary

There are a bunch of files included in the repo. Here are a summary of the files:

- `coords_test.py`: A Python test script with a bunch of known world coordinates to known zones and areas.
- `generate_zone_map_*`: Two Python scripts to visually map the `WorldMapArea.dbc` file.
- `worldmaparea.py`: A Python module with a couple classes to handle loading `WorldMapArea` DBC data.
- `worldmaparea.csv`: Data extracted from 1.12.1.5875 WoW Vanilla client. The extracted `WorldMapArea` DBC data is easily downloaded from [WoW.tools](https://wow.tools/dbc/?dbc=worldmaparea&build=1.12.1.5875#page=1).

## Definitions

- XYZ coordinates: Also known as world coordinates, global coordinates, or `.gps` coordinates. These are the type of coordinates you will see in WoW private server databases, or when running the `.gps` command (if you have GM command capability of a private server)

- XY coordinates: Also known as normal coordinates, map coordinates, or zone coordinates. These are the coordinates you will see on the zone map (area map) in-game. Basically, these are the coordinates you are used to seeing in-game.

## Example Gameobject Coordinates

World coordinates from a CMaNGOS database

1. Finding the game object ID of Sungrass

```
mysql> select entry,name from gameobject_template where name = "Sungrass";;
+--------+----------+
| entry  | name     |
+--------+----------+
| 142142 | Sungrass |
| 176636 | Sungrass |
| 180164 | Sungrass |
+--------+----------+
```

2. Then get all sungrass on world map

```
select * from gameobject where id = "142142";
```

## Resources

- [[3.0] Yet another core rewrite? #148](https://github.com/Questie/Questie/issues/148) - summary of a method to extract zone from world coordinates which is not effective
- [Zones and coordinates --> World to Zone coordinates](https://www.ownedcore.com/forums/world-of-warcraft/world-of-warcraft-bots-programs/wow-memory-editing/382790-zones-coordinates-world-zone-coordinates.html) - summary of how to convert zone coordinates to world coordinates
- [[WOTLK] Get World Coordinates From Map Coords](https://wrobot.eu/forums/topic/11486-wotlk-get-world-coordinates-from-map-coords/) - summary of how to convert zone coordinates to world coordinates
- [GatherMate2_Data_Wowhead](https://gitlab.com/marhag87/gathermate2_data_wowhead) - Has scraper for wowhead data
- [How to add unseen nodes to GatherMate2](https://www.reddit.com/r/classicwow/comments/gsnijz/how_to_add_unseen_nodes_to_gathermate2/) - Like the title says!
- [Mangosdb_struct](https://github.com/cmangos/issues/wiki/MangosDB_struct) - Information about the mangos db structure
