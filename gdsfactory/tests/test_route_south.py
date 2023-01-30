from __future__ import annotations

from pytest_regressions.data_regression import DataRegressionFixture

import gdsfactory as gf
from gdsfactory.component import Component


def test_route_south(
    data_regression: DataRegressionFixture, check: bool = True
) -> Component:
    c = gf.Component("test_route_south")
    cr = c << gf.components.mmi2x2()
    route = gf.routing.route_south(component=cr)
    references = route.references

    lengths = {}
    for i, reference in enumerate(references):
        c.add(reference)
        route_length = reference.parent.info["length"]
        lengths[i] = float(route_length)
    if check:
        data_regression.check(lengths)
    return c


if __name__ == "__main__":
    c = test_route_south(None, check=False)
    c.show(show_ports=True)
