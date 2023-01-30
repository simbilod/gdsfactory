from __future__ import annotations

import gdsfactory as gf
from gdsfactory import CrossSection
from gdsfactory import path as pa


def test_no_ports() -> gf.Component:
    c = gf.Component()
    w = h = 1
    layer = (1, 0)
    points = [
        [-w / 2.0, -h / 2.0],
        [-w / 2.0, h / 2],
        [w / 2, h / 2],
        [w / 2, -h / 2.0],
    ]
    c.add_polygon(points, layer=layer)
    return c


def test_path() -> gf.Component:
    s1 = gf.Section(width=2.2, offset=0, layer=(3, 0), name="etch")
    s2 = gf.Section(width=1.1, offset=3, layer=(1, 0), name="wg2")
    X1 = CrossSection(
        width=1.2,
        offset=0,
        layer=(2, 0),
        name="wg",
        port_names=("in1", "out1"),
        sections=(s1, s2),
    )

    # Create the second CrossSection that we want to transition to
    s1 = gf.Section(width=3.5, offset=0, layer=(3, 0), name="etch")
    s2 = gf.Section(width=3, offset=5, layer=(1, 0), name="wg2")
    X2 = CrossSection(
        width=1,
        offset=0,
        layer=(2, 0),
        name="wg",
        port_names=("in2", "out2"),
        sections=[s1, s2],
    )

    Xtrans = pa.transition(cross_section1=X1, cross_section2=X2, width_type="sine")

    P1 = pa.straight(length=5)
    P2 = pa.straight(length=5)
    WG1 = gf.path.extrude(P1, X1)
    WG2 = gf.path.extrude(P2, X2)

    P4 = pa.euler(radius=25, angle=45, p=0.5, use_eff=False)
    WG_trans = gf.path.extrude(P4, Xtrans)

    c = gf.Component("test_path")
    wg1 = c << WG1
    wg2 = c << WG2
    wgt = c << WG_trans

    wgt.connect("in2", wg1.ports["out1"])
    wg2.connect("in2", wgt.ports["out1"])
    assert len(c.references) == 3
    return c


if __name__ == "__main__":
    # c = test_no_ports()
    c = test_path()
    c.show(show_ports=True)
