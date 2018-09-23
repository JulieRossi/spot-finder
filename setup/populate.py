import json

from spot_finder.model import Spot


def create_spots_from_file(file_path):
    with open(file_path, encoding='utf_8') as f:
        for line in f:
            line = json.loads(line)
            spot = Spot(**line)
            spot.save()
