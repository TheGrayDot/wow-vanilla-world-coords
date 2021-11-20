from typing import Generator


class Zone:
    def __init__(self):
        self.db_id = None
        self.map_id = None
        self.area_id = None
        self.area_name = None
        self.loc_left = None
        self.loc_right = None
        self.loc_top = None
        self.loc_bottom = None
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.width = None
        self.height = None

    def populate(self, data: list) -> None:
        """Load WorldMapArea data for the specific zone."""
        self.x1 = float(data[6])
        self.x2 = float(data[7])
        self.y1 = float(data[4])
        self.y2 = float(data[5])
        self.width = self.x2 - self.x1
        self.height = self.y2 - self.y1

        properties = [
            "db_id",
            "map_id",
            "area_id",
            "area_name",
            "loc_left",
            "loc_right",
            "loc_top",
            "loc_bottom"
        ]

        for prop, value in zip(properties, data):
            if "id" in prop:
                # Convert any ID-based property to int
                value = int(value)
                setattr(self, prop, value)
            elif "loc" in prop:
                # Convert any location property to float
                value = float(value)
                setattr(self, prop, value)
            else:
                setattr(self, prop, value)
    
    def coord_in_zone(self, x: float, y: float, map_id: int):
        """Check if a world coord is in a zone."""
        # print(x, y)
        # print(x <= self.loc_left)
        # print(x >= self.loc_right)
        # print(y <= self.loc_top)
        # print(y >= self.loc_bottom)
        if self.map_id != map_id:
            return False
        if x < self.x1 and x > self.x2:
            if y < self.y1 and y > self.y2:
                return True


class Map:
    def __init__(self):
        self.world_map_area_file = "worldmaparea.csv"
        self.all_zones = list()
        self.all_zones_dict = dict()

    def __iter__(self) -> Generator[Zone, None, None]:
        """Iterate (loop) over each Zone object in map."""
        for zone in self.all_zones:
            yield zone

    def __getitem__(self, zone_name: str) -> Zone:
        """Return the zone object based on zone name.
        :param zone_name: The zone name.
        :return: The zone object linked to a specific named.
        """
        return self.all_zones_dict[zone_name]

    def __len__(self) -> int:
        """Return the count of the total number of zones.
        :return: The total number of items.
        """
        return len(self.all_zones)

    def parse_worldmaparea(self):
        """Read the WorldMapArea CSV file."""
        with open(self.world_map_area_file) as f:
            for i, line in enumerate(f):
                if i == 0:
                    continue
                line = line.strip()
                line = line.split(",")
                zone = Zone()
                zone.populate(line)
                self.all_zones.append(zone)
                self.all_zones_dict[zone.area_name] = zone

    def coords_to_zone(self, x: float, y: float, map_id: int) -> str:
        predicted_zone_name = None
        predicted_zone_id = 0

        for zone in self.all_zones:
            # if "elwynn" not in zone.area_name.lower():
            #     continue
            is_in_zone = zone.coord_in_zone(x, y, map_id)
            if is_in_zone:
                print("   ", zone.area_name, zone.area_id, zone.db_id)
                if zone.area_id > predicted_zone_id:
                    predicted_zone_id = zone.area_id
                    predicted_zone_name = zone.area_name
            
        print("    GUESSING:", predicted_zone_name)
