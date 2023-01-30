from __future__ import annotations

from gdsfactory.port import csv2port


def test_csv2port(data_regression) -> None:
    import gdsfactory as gf

    name = "straight"
    csvpath = gf.PATH.gdsdir / f"{name}.ports"

    ports = csv2port(csvpath)
    data_regression.check(ports)
