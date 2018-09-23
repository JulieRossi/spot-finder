from spot_finder.model import Spot


def delete_all_spots():
    Spot().search().delete()
