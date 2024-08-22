from pathlib import Path
import click
import json

from utils import remove_additional_functions, test_code
from test_cases import test_cases

extra_imports = """
import geopandas as gpd
from shapely.geometry import Point
import shapely.geometry
import os
import json
import osmnx
import pandas as pd
import osmnx as ox
import fiona
import shapefile
import geojson
"""


@click.command()
@click.option(
    "-f",
    "--file",
    type=click.Path(exists=True, dir_okay=False, file_okay=True, path_type=Path),
)
def main(file: Path):
    with open(file, "r") as f:
        stats = json.load(f)

    models = [m for m in stats.keys() if "time" not in m]

    for model in models:
        print(f"Testing model: {model}")

        sanitized_code = [
            remove_additional_functions(stats[model][f"{case['id']}_generated"]) for case in test_cases
        ]

        for idx, code in enumerate(sanitized_code):
            stats[model][f"{test_cases[idx]['id']}_sanitized"] = code
            test_cases[idx]["code"] = code

        results = test_code(test_cases, extra_imports=extra_imports)

        for idx, res in enumerate(results):
            stats[model][f"{test_cases[idx]['id']}_results"] = res
        print(results)

    # print(stats)
    with open(file.parent / "tests.json", "w") as f:
        json.dump(stats, f, indent=2)


if __name__ == "__main__":
    main()
