import geopandas as gpd
from shapely.geometry import Polygon, Point
import h3

from settings import INPUTS_DIR

test_cases = [
    {
        # 1 - mean area of the polygons
        "id": "1.1",
        "type": "simple",
        "input": "gdf",
        "framing": "operation",
        "prompt": 'import geopandas as gpd\n\ndef mean_area(polygons: gpd.GeoDataFrame) -> float:\n    """Calculate mean area of the polygons in a geodataframe"""',
        "entrypoint": "mean_area",
        "tests": [
            {
                "inputs": {
                    "polygons": gpd.read_file(INPUTS_DIR / "simple_buildings" / "1.geojson"),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "polygons": gpd.read_file(INPUTS_DIR / "simple_buildings" / "2.geojson"),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "1.2",
        "type": "simple",
        "input": "shp",
        "framing": "operation",
        "prompt": 'def mean_area(filename: str) -> float:\n    """Calculate mean area of the polygons in a shapefile"""',
        "entrypoint": "mean_area",
        "tests": [
            {
                "inputs": {
                    "filename": (INPUTS_DIR / "simple_buildings" / "1.shp").as_posix(),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "filename": (INPUTS_DIR / "simple_buildings" / "2.shp").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "1.3",
        "type": "simple",
        "input": "geojson",
        "framing": "operation",
        "prompt": 'def mean_area(filename: str) -> float:\n    """Calculate mean area of the polygons in a geojson file"""',
        "entrypoint": "mean_area",
        "tests": [
            {
                "inputs": {
                    "filename": (INPUTS_DIR / "simple_buildings" / "1.geojson").as_posix(),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "filename": (INPUTS_DIR / "simple_buildings" / "2.geojson").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "1.4",
        "type": "simple",
        "input": "gdf",
        "framing": "semantic",
        "prompt": 'import geopandas as gpd\n\ndef buildings_area(building_gdf: gpd.GeoDataFrame) -> float:\n    """Calculate mean area of the buildings in a geodataframe"""',
        "entrypoint": "buildings_area",
        "tests": [
            {
                "inputs": {
                    "building_gdf": gpd.read_file(INPUTS_DIR / "simple_buildings" / "1.geojson"),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "building_gdf": gpd.read_file(INPUTS_DIR / "simple_buildings" / "2.geojson"),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "1.5",
        "type": "simple",
        "input": "shp",
        "framing": "semantic",
        "prompt": 'def buildings_area(building_file: str) -> float:\n    """Calculate mean area of the buildings in a shapefile"""',
        "entrypoint": "buildings_area",
        "tests": [
            {
                "inputs": {
                    "building_file": (INPUTS_DIR / "simple_buildings" / "1.shp").as_posix(),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "building_file": (INPUTS_DIR / "simple_buildings" / "2.shp").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "1.6",
        "type": "simple",
        "input": "geojson",
        "framing": "semantic",
        "prompt": 'def buildings_area(building_file: str) -> float:\n    """Calculate mean area of the buildings in a geojson file"""',
        "entrypoint": "buildings_area",
        "tests": [
            {
                "inputs": {
                    "building_file": (INPUTS_DIR / "simple_buildings" / "1.geojson").as_posix(),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "building_file": (INPUTS_DIR / "simple_buildings" / "2.geojson").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    # 2 - mean area of the intersections beetwen two sets of polygons
    {
        "id": "2.1",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "prompt": 'import geopandas as gpd\n\ndef mean_intersection_area(first: gpd.GeoDataFrame, second: gpd.GeoDataFrame) -> float:\n    """Calculate the mean intersection ratio of polygons. Both arguments are geodataframes."""',
        "entrypoint": "mean_intersection_area",
        "tests": [
            {
                "inputs": {
                    "first": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "buildings_1.geojson"),
                    "second": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "parcels_1.geojson"),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "first": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "buildings_2.geojson"),
                    "second": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "parcels_2.geojson"),
                },
                "expected_output": 0.5,
            }
        ],
    },
    {
        "id": "2.2",
        "type": "complex",
        "input": "shp",
        "framing": "operation",
        "prompt": 'def mean_intersection_area(first_filename: str, second_filename: str) -> float:\n    """Calculate the mean intersection ratio of polygons. Both arguments are shapefiles."""',
        "entrypoint": "mean_intersection_area",
        "tests": [
            {
                "inputs": {
                    "first_filename": (INPUTS_DIR / "buildings_parcels" / "buildings_1.shp").as_posix(),
                    "second_filename": (INPUTS_DIR / "buildings_parcels" / "parcels_1.shp").as_posix(),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "first_filename": (INPUTS_DIR / "buildings_parcels" / "buildings_2.shp").as_posix(),
                    "second_filename": (INPUTS_DIR / "buildings_parcels" / "parcels_2.shp").as_posix(),
                },
                "expected_output": 0.5,
            }
        ],
    },
    {
        "id": "2.3",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "prompt": 'def mean_intersection_area(first_filename: str, second_filename: str) -> float:\n    """Calculate the mean intersection ratio of polygons. Both arguments are geojson files."""',
        "entrypoint": "mean_intersection_area",
        "tests": [
            {
                "inputs": {
                    "first_filename": (INPUTS_DIR / "buildings_parcels" / "buildings_1.geojson").as_posix(),
                    "second_filename": (INPUTS_DIR / "buildings_parcels" / "parcels_1.geojson").as_posix(),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "first_filename": (INPUTS_DIR / "buildings_parcels" / "buildings_2.geojson").as_posix(),
                    "second_filename": (INPUTS_DIR / "buildings_parcels" / "parcels_2.geojson").as_posix(),
                },
                "expected_output": 0.5,
            }
        ],
    },
    {
        "id": "2.4",
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "prompt": 'import geopandas as gpd\n\ndef building_to_parcel_ratio(buildings_gdf: gpd.GeoDataFrame, parcels_gdf: gpd.GeoDataFrame) -> float:\n    """Calculate the mean ratio of the buliding area compared to the parcel it stands on. Buildings and parcels are in separate geodataframes."""',
        "entrypoint": "building_to_parcel_ratio",
        "tests": [
            {
                "inputs": {
                    "buildings_gdf": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "buildings_1.geojson"),
                    "parcels_gdf": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "parcels_1.geojson"),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "buildings_gdf": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "buildings_2.geojson"),
                    "parcels_gdf": gpd.read_file(INPUTS_DIR / "buildings_parcels" / "parcels_2.geojson"),
                },
                "expected_output": 0.5,
            }
        ],
    },
    {
        "id": "2.5",
        "type": "complex",
        "input": "shp",
        "framing": "semantic",
        "prompt": 'def building_to_parcel_ratio(buildings_file: str, parcels_file: str) -> float:\n    """Calculate the mean ratio of the buliding area compared to the parcel it stands on. Buildings and parcels are in separate shapefiles."""',
        "entrypoint": "building_to_parcel_ratio",
        "tests": [
            {
                "inputs": {
                    "buildings_file": (INPUTS_DIR / "buildings_parcels" / "buildings_1.shp").as_posix(),
                    "parcels_file": (INPUTS_DIR / "buildings_parcels" / "parcels_1.shp").as_posix(),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "buildings_file": (INPUTS_DIR / "buildings_parcels" / "buildings_2.shp").as_posix(),
                    "parcels_file": (INPUTS_DIR / "buildings_parcels" / "parcels_2.shp").as_posix(),
                },
                "expected_output": 0.5,
            }
        ],
    },
    {
        "id": "2.6",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "prompt": 'def building_to_parcel_ratio(buildings_file: str, parcels_file: str) -> float:\n    """Calculate the mean ratio of the buliding area compared to the parcel it stands on. Buildings and parcels are in separate geojson files."""',
        "entrypoint": "building_to_parcel_ratio",
        "tests": [
            {
                "inputs": {
                    "buildings_file": (INPUTS_DIR / "buildings_parcels" / "buildings_1.geojson").as_posix(),
                    "parcels_file": (INPUTS_DIR / "buildings_parcels" / "parcels_1.geojson").as_posix(),
                },
                "expected_output": 0.25,
            },
            {
                "inputs": {
                    "buildings_file": (INPUTS_DIR / "buildings_parcels" / "buildings_2.geojson").as_posix(),
                    "parcels_file": (INPUTS_DIR / "buildings_parcels" / "parcels_2.geojson").as_posix(),
                },
                "expected_output": 0.5,
            },
        ],
    },
    # 3 - number of points in polygons
    {
        "id": "3.1",
        "type": "simple",
        "input": "gdf",
        "framing": "operation",
        "prompt": 'import geopandas as gpd\n\ndef points_in_polygons(points_gdf: gpd.GeoDataFrame, polygons_gdf: gpd.GeoDataFrame) -> int:\n    """Calculate the number of points that are inside polygons. Points and polygons are stored in GeoDataFrames."""',
        "entrypoint": "points_in_polygons",
        "tests": [
            {
                # Points are on the edges of the polygons, so the withing predicate will fail. Some points are shared betwenn polygons.
                "inputs": {
                    "polygons_gdf": gpd.read_file(INPUTS_DIR / "stations_count" / "polygons_1.geojson"),
                    "points_gdf": gpd.read_file(INPUTS_DIR / "stations_count" / "points_1.geojson"),
                },
                "expected_output": 3,
            },
            {
                # Points are inside the polygons. No points are shared between polygons.
                "inputs": {
                    "polygons_gdf": gpd.read_file(INPUTS_DIR / "stations_count" / "polygons_2.geojson"),
                    "points_gdf": gpd.read_file(INPUTS_DIR / "stations_count" / "points_2.geojson"),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "3.2",
        "type": "simple",
        "input": "shp",
        "framing": "operation",
        "prompt": 'def points_in_polygons(points: str, polygons: str) -> int:\n    """Calculate the number of points that are inside polygons. Points and polygons are stored in shapefiles."""',
        "entrypoint": "points_in_polygons",
        "tests": [
            {
                "inputs": {
                    "polygons": (INPUTS_DIR / "stations_count" / "polygons_1.shp").as_posix(),
                    "points": (INPUTS_DIR / "stations_count" / "points_1.shp").as_posix(),
                },
                "expected_output": 3,
            },
            {
                "inputs": {
                    "polygons": (INPUTS_DIR / "stations_count" / "polygons_2.shp").as_posix(),
                    "points": (INPUTS_DIR / "stations_count" / "points_2.shp").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "3.3",
        "type": "simple",
        "input": "geojson",
        "framing": "operation",
        "prompt": 'def points_in_polygons(points: str, polygons: str) -> int:\n    """Calculate the number of points that are inside polygons. Points and polygons are stored in geojson files."""',
        "entrypoint": "points_in_polygons",
        "tests": [
            {
                "inputs": {
                    "polygons": (INPUTS_DIR / "stations_count" / "polygons_1.geojson").as_posix(),
                    "points": (INPUTS_DIR / "stations_count" / "points_1.geojson").as_posix(),
                },
                "expected_output": 3,
            },
            {
                "inputs": {
                    "polygons": (INPUTS_DIR / "stations_count" / "polygons_2.geojson").as_posix(),
                    "points": (INPUTS_DIR / "stations_count" / "points_2.geojson").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "3.4",
        "type": "simple",
        "input": "gdf",
        "framing": "semantic",
        "prompt": 'import geopandas as gpd\ndef mean_stations_count(bus_stops: gpd.GeoDataFrames, districts: gpd.GeoDataFrames) -> float:\n    """Calculate the mean number of bus stops in a districs. Stations and districts are stored in GeoDataFrames."""',
        "entrypoint": "mean_stations_count",
        "tests": [
            {
                "inputs": {
                    "bus_stops": gpd.read_file(INPUTS_DIR / "stations_count" / "points_1.geojson"),
                    "districts": gpd.read_file(INPUTS_DIR / "stations_count" / "polygons_1.geojson"),
                },
                "expected_output": 3,
            },
            {
                "inputs": {
                    "bus_stops": gpd.read_file(INPUTS_DIR / "stations_count" / "points_2.geojson"),
                    "districts": gpd.read_file(INPUTS_DIR / "stations_count" / "polygons_2.geojson"),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "3.5",
        "type": "simple",
        "input": "shp",
        "framing": "semantic",
        "prompt": 'def mean_stations_count(bus_stops: str, districts: str) -> float:\n    """Calculate the mean number of bus stops in a districs. Stations and districts are stored in shapefiles."""',
        "entrypoint": "mean_stations_count",
        "tests": [
            {
                "inputs": {
                    "bus_stops": (INPUTS_DIR / "stations_count" / "points_1.shp").as_posix(),
                    "districts": (INPUTS_DIR / "stations_count" / "polygons_1.shp").as_posix(),
                },
                "expected_output": 3,
            },
            {
                "inputs": {
                    "bus_stops": (INPUTS_DIR / "stations_count" / "points_2.shp").as_posix(),
                    "districts": (INPUTS_DIR / "stations_count" / "polygons_2.shp").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    {
        "id": "3.6",
        "type": "simple",
        "input": "geojson",
        "framing": "semantic",
        "prompt": 'def mean_stations_count(bus_stops: str, districts: str) -> float:\n    """Calculate the mean number of bus stops in a districs. Stations and districts are stored in geojson files."""',
        "entrypoint": "mean_stations_count",
        "tests": [
            {
                "inputs": {
                    "bus_stops": (INPUTS_DIR / "stations_count" / "points_1.geojson").as_posix(),
                    "districts": (INPUTS_DIR / "stations_count" / "polygons_1.geojson").as_posix(),
                },
                "expected_output": 3,
            },
            {
                "inputs": {
                    "bus_stops": (INPUTS_DIR / "stations_count" / "points_2.geojson").as_posix(),
                    "districts": (INPUTS_DIR / "stations_count" / "polygons_2.geojson").as_posix(),
                },
                "expected_output": 2,
            },
        ],
    },
    # 4 - build point and check if it is present in a list of points
    {
        # Geopandas reading files and converting lat lon to points.
        "id": "4.1",
        "type": "simple",
        "input": "gdf",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_point_present(x: float, y: float, points: gpd.GeoDataFrame) -> bool:\n    """Check if a point is present in a list of points stored in a geojson file."""',
        "entrypoint": "is_point_present",
        "tests": [
            {
                "inputs": {
                    "x": 0,
                    "y": 0,
                    "points": gpd.read_file(INPUTS_DIR / "points.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "x": 0,
                    "y": 1,
                    "points": gpd.read_file(INPUTS_DIR / "points.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "4.2",
        "type": "simple",
        "input": "shp",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_point_present(x: float, y: float, filename: str) -> bool:\n    """Check if a point is present in a list of points stored in a shapefile."""',
        "entrypoint": "is_point_present",
        "tests": [
            {
                "inputs": {
                    "x": 0,
                    "y": 0,
                    "filename": (INPUTS_DIR / "points.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "x": 0,
                    "y": 1,
                    "filename": (INPUTS_DIR / "points.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "4.3",
        "type": "simple",
        "input": "geojson",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_point_present(x: float, y: float, filename: str) -> bool:\n    """Check if a point is present in a list of points stored in a geojson file."""',
        "entrypoint": "is_point_present",
        "tests": [
            {
                "inputs": {
                    "x": 0,
                    "y": 0,
                    "filename": (INPUTS_DIR / "points.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "x": 0,
                    "y": 1,
                    "filename": (INPUTS_DIR / "points.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "4.4",
        "type": "simple",
        "input": "gdf",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_station(lat: float, lon: float, stations: gpd.GeoDataFrame) -> bool:\n    """Check if given coordinates represent a bus station stored in a geodataframe."""',
        "entrypoint": "is_station",
        "tests": [
            {
                "inputs": {
                    "lat": 0,
                    "lon": 0,
                    "stations": gpd.read_file(INPUTS_DIR / "points.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 0,
                    "lon": 1,
                    "stations": gpd.read_file(INPUTS_DIR / "points.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "4.5",
        "type": "simple",
        "input": "shp",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_station(lat: float, lon: float, stations: str) -> bool:\n    """Check if given coordinates represent a bus station stored in a shapefile."""',
        "entrypoint": "is_station",
        "tests": [
            {
                "inputs": {
                    "lat": 0,
                    "lon": 0,
                    "stations": (INPUTS_DIR / "points.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 0,
                    "lon": 1,
                    "stations": (INPUTS_DIR / "points.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "4.6",
        "type": "simple",
        "input": "geojson",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef is_station(lat: float, lon: float, stations: str) -> bool:\n    """Check if given coordinates represent a bus station stored in a geojson file."""',
        "entrypoint": "is_station",
        "tests": [
            {
                "inputs": {
                    "lat": 0,
                    "lon": 0,
                    "stations": (INPUTS_DIR / "points.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 0,
                    "lon": 1,
                    "stations": (INPUTS_DIR / "points.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        # Shapely point construction.
        "id": "5",
        "type": "simple",
        "tool": "shapely",
        "prompt": 'import shapely\n\ndef construct_point(x: float, y: float) -> shapely.geometry.Point:\n    """Construct a point from x and y coordinates."""',
        "entrypoint": "construct_point",
        "tests": [
            {
                "inputs": {"x": 0, "y": 1},
                "expected_output": Point(0, 1),
            },
            {
                "inputs": {"x": 1, "y": 0},
                "expected_output": Point(1, 0),
            },
        ],
    },
    {
        # 6 - shapely within operation
        "id": "6.1",
        "type": "simple",
        "tool": "shapely",
        "framing": "operation",
        "prompt": 'import shapely\n\ndef is_point_within_polygon(point: shapely.geometry.Point, polygon: shapely.geometry.Polygon) -> bool:\n    """Check if a given point lies within a polygon."""',
        "entrypoint": "is_point_within_polygon",
        "tests": [
            {
                "inputs": {
                    "point": Point(0.5, 0.5),
                    "polygon": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(2, 2),
                    "polygon": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "6.2",
        "type": "simple",
        "tool": "shapely",
        "framing": "semantic",
        "prompt": 'import shapely\n\ndef is_in_the_city(place: shapely.geometry.Point, city: shapely.geometry.Polygon) -> bool:\n    """Check if a given place lies inside the city boundaries."""',
        "entrypoint": "is_in_the_city",
        "tests": [
            {
                "inputs": {
                    "place": Point(0.5, 0.5),
                    "city": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "place": Point(2, 2),
                    "city": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            },
        ],
    },
    {
        # 7 - shapely touches opeartion
        "id": "7.1",
        "type": "simple",
        "tool": "shapely",
        "framing": "operation",
        "prompt": 'import shapely\n\ndef are_polygons_adjacent(polygon1: shapely.geometry.Polygon, polygon2: shapely.geometry.Polygon) -> bool:\n    """Check if two polygons are adjacent."""',
        "entrypoint": "are_polygons_adjacent",
        "tests": [
            {
                "inputs": {
                    "polygon1": Polygon([(1, 1), (2, 1), (2, 2), (1, 2)]),
                    "polygon2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "polygon1": Polygon([(2, 2), (3, 2), (3, 3), (2, 3)]),
                    "polygon2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            },
            {
                "inputs": {
                    "polygon1": Polygon([(0, 0), (0.5, 0), (0.5, 0.5), (0, 0.5)]),
                    "polygon2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            }
        ],
    },
    {
        "id": "7.2",
        "type": "simple",
        "tool": "shapely",
        "framing": "semantic",
        "prompt": 'import shapely\n\ndef are_countries_neighbours(country1: shapely.geometry.Polygon, country2: shapely.geometry.Polygon) -> bool:\n    """Check if two polygons are adjacent."""',
        "entrypoint": "are_countries_neighbours",
        "tests": [
            {
                "inputs": {
                    "country1": Polygon([(1, 1), (2, 1), (2, 2), (1, 2)]),
                    "country2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "country1": Polygon([(2, 2), (3, 2), (3, 3), (2, 3)]),
                    "country2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            },
            {
                "inputs": {
                    "country1": Polygon([(0, 0), (0.5, 0), (0.5, 0.5), (0, 0.5)]),
                    "country2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": False,
            }
        ],
    },
    {
        # 8 - shapely intersection area
        "id": "8.1",
        "type": "simple",
        "tool": "shapely",
        "framing": "operation",
        "prompt": 'import shapely\n\ndef polygons_intersection(polygon1: shapely.geometry.Polygon, polygon2: shapely.geometry.Polygon) -> float:\n    """Calculate the area of two polygons intersection."""',
        "entrypoint": "polygons_intersection",
        "tests": [
            {
                "inputs": {
                    "polygon1": Polygon([(1, 1), (2, 1), (2, 2), (1, 2)]),
                    "polygon2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": 0,
            },
            {
                "inputs": {
                    "polygon1": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
                    "polygon2": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "polygon1": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
                    "polygon2": Polygon([(1, 1), (3, 1), (3, 3), (1, 3)]),
                },
                "expected_output": 1,
            }
        ],
    },
    {
        "id": "8.2",
        "type": "simple",
        "tool": "shapely",
        "framing": "semantic",
        "prompt": 'import shapely\n\ndef forest_area(city: shapely.geometry.Polygon, forset: shapely.geometry.Polygon) -> float:\n    """Calculate how much of the forest is inside the city."""',
        "entrypoint": "forest_area",
        "tests": [
            {
                "inputs": {
                    "forset": Polygon([(1, 1), (2, 1), (2, 2), (1, 2)]),
                    "city": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": 0,
            },
            {
                "inputs": {
                    "forset": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
                    "city": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]),
                },
                "expected_output": 1,
            },
            {
                "inputs": {
                    "forset": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]),
                    "city": Polygon([(1, 1), (3, 1), (3, 3), (1, 3)]),
                },
                "expected_output": 1,
            }
        ],
    },
    {
        # H3 Convert point to a corresponding h3 cell.
        "id": "9.1",
        "type": "simple",
        "tool": "h3",
        "point": "lat_lon",
        "prompt": 'import h3\n\ndef lat_lon_to_h3(lat: float, lon: float, resolution: int) -> str:\n    """Convert a lat lon pair to an h3 cell."""',
        "entrypoint": "lat_lon_to_h3",
        "tests": [
            {
                "inputs": {"lat": 0, "lon": 0, "resolution": 1},
                "expected_output": "81757ffffffffff",
            },
            {
                "inputs": {"lat": 0, "lon": 0, "resolution": 2},
                "expected_output": "82754ffffffffff",
            },
            {
                "inputs": {"lat": 0, "lon": 0, "resolution": 3},
                "expected_output": "83754efffffffff",
            },
        ],
    },
    {
        "id": "9.2",
        "type": "simple",
        "tool": "h3",
        "point": "shapely",
        "prompt": 'import h3\nimport shapely\n\ndef point_to_h3(point: shapely.geometry.Point, resolution: int) -> str:\n    """Convert a point to an h3 cell."""',
        "entrypoint": "point_to_h3",
        "tests": [
            {
                "inputs": {"point": Point(0, 0), "resolution": 1},
                "expected_output": "81757ffffffffff",
            },
            {
                "inputs": {"point": Point(0, 0), "resolution": 2},
                "expected_output": "82754ffffffffff",
            },
            {
                "inputs": {"point": Point(0, 0), "resolution": 3},
                "expected_output": "83754efffffffff",
            },
        ],
    },
    {
        # H3 convert h3 cell to a Polygon
        "id": "10",
        "type": "simple",
        "tool": "h3",
        "prompt": 'import h3\nimport shapely\n\ndef h3_to_polygon(h3_cell: str) -> shapely.geometry.Polygon:\n    """Convert an h3 cell to a polygon."""',
        "entrypoint": "h3_to_polygon",
        "tests": [
            {
                "inputs": {"h3_cell": "82754ffffffffff"},
                "expected_output": Polygon(h3.h3_to_geo_boundary("82754ffffffffff", geo_json=True)),

            },
            {
                "inputs": {"h3_cell": "83754efffffffff"},
                "expected_output": Polygon(h3.h3_to_geo_boundary("83754efffffffff", geo_json=True)),
            },
        ],
    },
    {
        # 11 - count H3 cells that are within a polygon
        "id": "11",
        "type": "complex",
        "tool": "h3",
        "prompt": 'import h3\n\ndef count_h3_cells_within_polygon(polygon: shapely.geometry.Polygon, resolution: int) -> int:\n    """Count the number of h3 cells that are within a polygon."""',
        "entrypoint": "count_h3_cells_within_polygon",
        "tests": [
            {
                "inputs": {"polygon": Polygon([(0, 0), (1, 0), (1, 1), (0, 1)]), "resolution": 6},
                "expected_output": 396,
            },
            {
                "inputs": {"polygon": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]), "resolution": 6},
                "expected_output": 1707,
            },
            {
                "inputs": {"polygon": Polygon([(0, 0), (2, 0), (2, 2), (0, 2)]), "resolution": 3},
                "expected_output": 1,
            }
        ],
    },
    {
        # 12 - search for point in a correct polygon
        "id": "12.1.1",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef check_point(lat: float, lon: float, name: str, polygons: gpd.GeoDataFrame) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons GeoDataFrame contains the polygons boundaries and names in the `name` column."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Lisbon",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "name": "Berlin",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Berlin",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.1.2",
        "type": "complex",
        "input": "shp",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'def check_point(lat: float, lon: float, name: str, polygons: str) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons is the path to the shapefile with polygons boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Lisbon",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.1.3",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'def check_point(lat: float, lon: float, name: str, polygons: str) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons is the path to the geojson with polygons boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Lisbon",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.1.4",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import geopandas as gpd\nimport shapely\n\ndef check_point(point: shapely.geometry.Point, name: str, polygons: gpd.GeoDataFrame) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons GeoDataFrame contains the polygon boundaries and names in the `name` column."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Lisbon",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Berlin",
                    "polygons": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.1.5",
        "type": "complex",
        "input": "shp",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_point(point: shapely.geometry.Point, name: str, polygons: str) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons is the path to the shapefile with polygons boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Lisbon",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.1.6",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_point(point: shapely.geometry.Point, name: str, polygons: str) -> bool:\n    """Check if a point is in the polygon with the given name. The polygons is the path to the geojson with polygons boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Lisbon",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "name": "Berlin",
                    "polygons": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.1",
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef check_point(lat: float, lon: float, city: str, cities: gpd.GeoDataFrame) -> bool:\n    """Check if a point is in the given city. The cities GeoDataFrame contains the cities boundaries and names in the `name` column."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Lisbon",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "city": "Berlin",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Berlin",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.2",
        "type": "complex",
        "input": "shp",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'def check_point(lat: float, lon: float, city: str, cities: str) -> bool:\n    """Check if a point is in the given city. The cities is the path to the shapefile with cities boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Lisbon",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.3",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'def check_point(lat: float, lon: float, city: str, cities: str) -> bool:\n    """Check if a point is in the given city. The cities is the path to the geojson with cities boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Lisbon",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.4",
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import geopandas as gpd\nimport shapely\n\ndef check_point(point: shapely.geometry.Point, city: str, cities: gpd.GeoDataFrame) -> bool:\n    """Check if a point is in the given city. The cities GeoDataFrame contains the cities boundaries and names in the `name` column."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Lisbon",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Berlin",
                    "cities": gpd.read_file(INPUTS_DIR / "cities" / "all.geojson"),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.5",
        "type": "complex",
        "input": "shp",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_point(point: shapely.geometry.Point, city: str, cities: str) -> bool:\n    """Check if a point is in the given city. The cities is the path to the shapefile with cities boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Lisbon",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.shp").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "12.2.6",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_point(point: shapely.geometry.Point, city: str, cities: str) -> bool:\n    """Check if a point is in the given city. The cities is the path to the geojson with cities boundaries with `name` feature."""',
        "entrypoint": "check_point",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Lisbon",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "name": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "city": "Berlin",
                    "cities": (INPUTS_DIR / "cities" / "all.geojson").as_posix(),
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "13.1.1",
        "type": "simple",
        "input": "gdf",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef get_polygon_name(lat: float, lon: float, polygons: gpd.GeoDataFrame) -> str:\n    """Get the name of a polygon in which a point is. The polygons GeoDataFrame contains the polygons boundaries and names in the `name` column."""',
        "entrypoint": "get_polygon_name",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "polygons": gpd.read_file(INPUTS_DIR / "countries" / "all.geojson"),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "polygons": gpd.read_file(INPUTS_DIR / "countries"  / "all.geojson"),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.1.2",
        "type": "simple",
        "input": "shp",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'def check_country(lat: float, lon: float, polygons: str) -> str:\n    """Get the name of a polygon in which a point is. The polygons is the path to the shapefile with polygons boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "polygons": (INPUTS_DIR / "countries" / "all.shp").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "polygons": (INPUTS_DIR / "countries"  / "all.shp").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.1.3",
        "type": "simple",
        "input": "geojson",
        "framing": "operation",
        "point": "lat_lon",
        "prompt": 'def check_country(lat: float, lon: float, polygons: str) -> str:\n    """Get the name of a polygon in which a point is. The polygons is the path to the geojson with polygons boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "polygons": (INPUTS_DIR / "countries" / "all.geojson").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "polygons": (INPUTS_DIR / "countries"  / "all.geojson").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.1.4",
        "type": "simple",
        "input": "gdf",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import geopandas as gpd\nimport shapely\n\ndef check_country(point: shapely.geometry.Point, polygons: gpd.GeoDataFrame) -> str:\n    """Get the name of a polygon in which a point is. The polygons GeoDataFrame contains the polygons boundaries and names in the `name` column."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "polygons": gpd.read_file(INPUTS_DIR / "countries" / "all.geojson"),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "polygons": gpd.read_file(INPUTS_DIR / "countries"  / "all.geojson"),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.1.5",
        "type": "simple",
        "input": "shp",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point, polygons: str) -> str:\n    """Get the name of a polygon in which a point is. The polygons is the path to the shapefile with polygons boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "polygons": (INPUTS_DIR / "countries" / "all.shp").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "polygons": (INPUTS_DIR / "countries"  / "all.shp").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.1.6",
        "type": "simple",
        "input": "geojson",
        "framing": "operation",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point, polygons: str) -> str:\n    """Get the name of a polygon in which a point is. The polygons is the path to the geojson with polygons boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "polygons": (INPUTS_DIR / "countries" / "all.geojson").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "polygons": (INPUTS_DIR / "countries"  / "all.geojson").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.1",
        "type": "simple",
        "input": "gdf",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'import geopandas as gpd\n\ndef check_country(lat: float, lon: float, countries: gpd.GeoDataFrame) -> str:\n    """Check in which country a point is. The countries GeoDataFrame contains the countries boundaries and names in the `name` column."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "countries": gpd.read_file(INPUTS_DIR / "countries" / "all.geojson"),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "countries": gpd.read_file(INPUTS_DIR / "countries"  / "all.geojson"),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.2",
        "type": "simple",
        "input": "shp",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'def check_country(lat: float, lon: float, countries: str) -> str:\n    """Check in which country a point is. The countries is the path to the shapefile with countries boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "countries": (INPUTS_DIR / "countries" / "all.shp").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "countries": (INPUTS_DIR / "countries"  / "all.shp").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.3",
        "type": "simple",
        "input": "geojson",
        "framing": "semantic",
        "point": "lat_lon",
        "prompt": 'def check_country(lat: float, lon: float, countries: str) -> str:\n    """Check in which country a point is. The countries is the path to the geojson with countries boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "countries": (INPUTS_DIR / "countries" / "all.geojson").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "countries": (INPUTS_DIR / "countries"  / "all.geojson").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.4",
        "type": "simple",
        "input": "gdf",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import geopandas as gpd\nimport shapely\n\ndef check_country(point: shapely.geometry.Point, countries: gpd.GeoDataFrame) -> str:\n    """Check in which country a point is. The countries GeoDataFrame contains the countries boundaries and names in the `name` column."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                "point": Point(-9.13, 38.71),  # Lisbon
                    "countries": gpd.read_file(INPUTS_DIR / "countries" / "all.geojson"),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "countries": gpd.read_file(INPUTS_DIR / "countries"  / "all.geojson"),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.5",
        "type": "simple",
        "input": "shp",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point, countries: str) -> str:\n    """Check in which country a point is. The countries is the path to the shapefile with countries boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "countries": (INPUTS_DIR / "countries" / "all.shp").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "countries": (INPUTS_DIR / "countries"  / "all.shp").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "13.2.6",
        "type": "simple",
        "input": "geojson",
        "framing": "semantic",
        "point": "shapely",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point, countries: str) -> str:\n    """Check in which country a point is. The countries is the path to the geojson with countries boundaries with `name` feature."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "countries": (INPUTS_DIR / "countries" / "all.geojson").as_posix(),
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "countries": (INPUTS_DIR / "countries"  / "all.geojson").as_posix(),
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        # 14 - reverse geocoding with osmnx
        "id": "14.1",
        "type": "simple",
        "point": "lat_lon",
        "tool": "osmnx",
        "prompt": 'def check_country(lat: float, lon: float) -> str:\n    """Check in which country a point is. Use the osmnx to perform geocoding to find country name."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "14.2",
        "type": "simple",
        "point": "shapely",
        "tool": "osmnx",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point) -> str:\n    """Check in which country a point is. Use the osmnx to perform geocoding to find country name."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                },
                "expected_output": "Portugal",
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                },
                "expected_output": "Germany",
            },
        ],
    },
    {
        "id": "15.1",
        "type": "complex",
        "point": "lat_lon",
        "tool": "osmnx",
        "prompt": 'def check_country(lat: float, lon: float, country: str) -> bool:\n    """Check if a point lies within the given country. Use the osmnx to perform geocoding."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "lat": 38.71,  # Lisbon
                    "lon": -9.13,
                    "country": "Portugal",
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "country": "Germany",
                },
                "expected_output": True,
            },
                        {
                "inputs": {
                    "lat": 52.43,  # Berlin
                    "lon": 13.59,
                    "country": "Portugal",
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "15.2",
        "type": "complex",
        "point": "shapely",
        "tool": "osmnx",
        "prompt": 'import shapely\n\ndef check_country(point: shapely.geometry.Point, country: str) -> bool:\n    """Check if a point lies within the given country. Use the osmnx to perform geocoding."""',
        "entrypoint": "check_country",
        "tests": [
            {
                "inputs": {
                    "point": Point(-9.13, 38.71),  # Lisbon
                    "country": "Portugal",
                },
                "expected_output": True,
            },
            {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "country": "Germany",
                },
                "expected_output": True,
            },
                        {
                "inputs": {
                    "point": Point(13.59, 52.43),  # Berlin
                    "country": "Portugal",
                },
                "expected_output": False,
            },
        ],
    },
    {
        "id": "16.1",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef trajectory_length(trajectory: gpd.GeoDataFrame) -> float:\n    """Calculate the length of a trajectory. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "trajectory_length",
        "tests": [
            {
                "inputs": {
                    "trajectory": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 16.24264,
            }
        ]
    },
    {
        "id": "16.3",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'def trajectory_length(trajectory: str) -> float:\n    """Calculate the length of a trajectory. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "trajectory_length",
        "tests": [
            {
                "inputs": {
                    "trajectory": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 16.24264,
            }
        ]
    },
    {
        "id": "16.4",
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef walk_length(trip: gpd.GeoDataFrame) -> float:\n    """Calculate the length of a walk. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "walk_length",
        "tests": [
            {
                "inputs": {
                    "trip": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 16.24264,
            }
        ]
    },
    {
        "id": "16.6",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'def walk_length(trip: str) -> float:\n    """Calculate the length of a walk. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "walk_length",
        "tests": [
            {
                "inputs": {
                    "trip": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 16.24264,
            }
        ]
    },
    {
        "id": "17.1",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef trajectory_duration(trajectory: gpd.GeoDataFrame) -> float:\n    """Calculate the duration of a trajectory in seconds. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "trajectory_duration",
        "tests": [
            {
                "inputs": {
                    "trajectory": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 900.0,
            }
        ]
    },
    {
        "id": "17.3",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'def trajectory_duration(trajectory: str) -> float:\n    """Calculate the duration of a trajectory in seconds. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "trajectory_duration",
        "tests": [
            {
                "inputs": {
                    "trajectory": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 900.0,
            }
        ]
    },
    {
        "id": "17.4",
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef walk_duration(trip: gpd.GeoDataFrame) -> float:\n    """Calculate the duration of a walk in seconds. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "walk_duration",
        "tests": [
            {
                "inputs": {
                    "trip": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 900.0,
            }
        ]
    },
    {
        "id": "17.6",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'def walk_duration(trip: str) -> float:\n    """Calculate the duration of a walk in seconds. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "walk_duration",
        "tests": [
            {
                "inputs": {
                    "trip": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 900.0,
            }
        ]
    },
    {
        "id": "18.1",
        "type": "complex",
        "input": "gdf",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef average_speed(trajectory: gpd.GeoDataFrame) -> float:\n    """Calculate the average speed of a trajectory in meters per second. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "average_speed",
        "tests": [
            {
                "inputs": {
                    "trajectory": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 0.018047,
            }
        ]
    },
    {
        "id": "18.3",
        "type": "complex",
        "input": "geojson",
        "framing": "operation",
        "tool": "movingpandas",
        "prompt": 'def average_speed(trajectory: str) -> float:\n    """Calculate the average speed of a trajectory in meters per second. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "average_speed",
        "tests": [
            {
                "inputs": {
                    "trajectory": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 0.018047,
            }
        ]
    },
    {
        "id": '18.4',
        "type": "complex",
        "input": "gdf",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'import geopandas as gpd\n\ndef average_walk_speed(trip: gpd.GeoDataFrame) -> float:\n    """Calculate the average speed of a walk in meters per second. It is saved in a geodataframe as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "average_walk_speed",
        "tests": [
            {
                "inputs": {
                    "trip": gpd.read_file(INPUTS_DIR / "trajectories" / "traj.geojson"),
                },
                "expected_output": 0.018047,
            }
        ]
    },
    {
        "id": "18.6",
        "type": "complex",
        "input": "geojson",
        "framing": "semantic",
        "tool": "movingpandas",
        "prompt": 'def average_walk_speed(trip: str) -> float:\n    """Calculate the average speed of a walk in meters per second. It is saved in a geojson as a collection of points and timestamps in the `geometry` and `t` columns. Use the `movingpandas` library."""',
        "entrypoint": "average_walk_speed",
        "tests": [
            {
                "inputs": {
                    "trip": (INPUTS_DIR / "trajectories" / "traj.geojson").as_posix(),
                },
                "expected_output": 0.018047,
            }
        ]
    },
    {
        # 19 - geocoding with osmnx - polygon
        "id": "19.1",
        "type": "simple",
        "tool": "osmnx",
        "prompt": 'def geocode_city(city: str) -> Polygon:\n    """Geocode a city to get its boundaries. Use the osmnx to perform geocoding."""',
        "entrypoint": "geocode_city",
        "tests": [
            {
                "inputs": {
                    "city": city.query,
                },
                "expected_output": city.geometry
            } for city in gpd.read_file(INPUTS_DIR / "geocoding" / "cities.geojson").itertuples()
        ]
    },
    {
        # 20 - geocoding with osmnx - point
        "id": "20.1",
        "type": "simple",
        "tool": "osmnx",
        "prompt": 'def geocode_city(city: str) -> Point:\n    """Geocode a city ant get its center point. Use the osmnx to perform geocoding."""',
        "entrypoint": "geocode_city",
        "tests": [
            {
                "inputs": {
                    "city": city.query,
                },
                "expected_output": (city.point_lat, city.point_lon)
            } for city in gpd.read_file(INPUTS_DIR / "geocoding" / "cities.geojson").itertuples()
        ]
    }
]
