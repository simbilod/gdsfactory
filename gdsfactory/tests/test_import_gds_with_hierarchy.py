# from pprint import pprint

from __future__ import annotations

import jsondiff
from pytest_regressions.data_regression import DataRegressionFixture

import gdsfactory as gf
from gdsfactory.cross_section import cross_section

gdspath = gf.PATH.gdsdir / "mzi2x2.gds"


def test_read_gds_hash2() -> gf.Component:
    c = gf.import_gds(gdspath)

    h = "bfc84eea02b07fa0e167223e0fdedc8e8b085026"
    assert c.hash_geometry() == h, f"h = {c.hash_geometry()!r}"
    return c


def test_read_gds_with_settings2(data_regression: DataRegressionFixture) -> None:
    c = gf.import_gds(gdspath, read_metadata=True)
    data_regression.check(c.to_dict())


def test_read_gds_equivalent2() -> None:
    """Ensures we can load it from GDS + YAML and get the same component
    settings."""
    splitter = gf.components.mmi1x2(cross_section=cross_section)
    c1 = gf.components.mzi(splitter=splitter, cross_section=cross_section)
    c2 = gf.import_gds(gdspath, read_metadata=True)

    d1 = c1.to_dict()
    d2 = c2.to_dict()

    # we change the name, so there is no cache conflicts
    # d1.pop("name")
    # d2.pop("name")
    # d1.pop("ports")
    # d2.pop("ports")
    # c1.pprint()
    # c2.pprint()

    d = jsondiff.diff(d1, d2)

    # from pprint import pprint
    # pprint(d1)
    # pprint(d2)
    # pprint(d)
    assert len(d) == 0, d


def test_mix_cells_from_gds_and_from_function2() -> None:
    """Ensures not duplicated cell names.

    when cells loaded from GDS and have the same name as a function with
    @cell decorator

    """
    c = gf.Component("test_mix_cells_from_gds_and_from_function")
    c << gf.components.mzi()
    c << gf.import_gds(gdspath)
    c.write_gds()
    c.show(show_ports=True)


def _write() -> None:
    splitter = gf.components.mmi1x2(cross_section=cross_section)
    c1 = gf.components.mzi(splitter=splitter, cross_section=cross_section)
    c1.write_gds_with_metadata(gdspath=gdspath)
    c1.show()


if __name__ == "__main__":
    _write()
    # test_read_gds_equivalent2()

    c = test_read_gds_hash2()
    # c.show(show_ports=True)
    # test_mix_cells_from_gds_and_from_function2()

    # test_read_gds_with_settings2()
    c1 = gf.components.mzi()
    c2 = gf.import_gds(gdspath)
    d1 = c1.to_dict()
    d2 = c2.to_dict()

    d = jsondiff.diff(d1, d2)
    print(d)
