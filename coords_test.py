from worldmaparea import Map

map = Map()
map.parse_worldmaparea()

"""
Tirisfal Glades: Brill
left    3033.3333
right   -1485.4166
top     3837.4998
bottom  824.99994
"""
print("[+] Tirisfal Glades: Brill")
tele = ".go 2260.64 289.021 34.1291 0"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)

"""
Elwynn Forest: Goldshire
left    1535.4166
right   -1935.4166
top     -7939.583
bottom  -10254.166
"""
print("[+] Elwynn Forest: Goldshire")
tele = ".go -9443.45 59.8944 56.0704 0"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)

"""
Strangelthorn Vale: Booty Bay
left    2220.8333
right   -4160.4165
top     -11168.75
bottom  -15422.916
"""
print("[+] Strangelthorn Vale: Booty Bay")
tele = ".go -14406.6 419.353 22.3907 0"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)

"""
The Barrens: The Crossroads
left    XXX
right   XXX
top     XXX
bottom  XXX
"""
print("[+] The Barrens: The Crossroads")
tele = ".go -456.263 -2652.7 95.615 1"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)

"""
Hillsbrad Foothills: Tarren Mill
left    XXX
right   XXX
top     XXX
bottom  XXX
"""
print("[+] Hillsbrad Foothills: Tarren Mill")
tele = ".go -28.1484 -899.243 56.0704 0"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)

"""
Felwood: Jaedenar
left    XXX
right   XXX
top     XXX
bottom  XXX
"""
print("[+] Felwood: Jaedenar")
tele = ".go 4878.319336 -614.219360 306.391052 1"
tele = tele.split(" ")
x = float(tele[1])
y = float(tele[2])
map_id = int(tele[4])
zone = map.coords_to_zone(x, y, map_id)
