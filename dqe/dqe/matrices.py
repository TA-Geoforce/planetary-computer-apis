from typing import List

from morecantile.defaults import tms as defaultTileMatrices

from .models import TileMatrixRef


def tileMatrixRefs(data_root_url: str) -> List[TileMatrixRef]:
    return [
        TileMatrixRef(
            tileMatrixSet=matrixID,
            tileMatrixSetURI="{}/tileMatrixSets/{}".format(data_root_url, matrixID),
        )
        for matrixID in defaultTileMatrices.list()
    ]