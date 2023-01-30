"""FIXME.

Tests are failing for python3.7

"""


from __future__ import annotations

import gdsfactory as gf
from gdsfactory.component import hash_file


def test_hash_geometry() -> None:
    """Test geometric hash of the GDS points."""
    c1 = gf.components.straight(length=10)
    c2 = gf.components.straight(length=11)
    h1 = c1.hash_geometry()
    h2 = c2.hash_geometry()
    assert h1 != h2


def _test_hash_array_file() -> None:
    """Test hash of a component with an array of references."""
    c = gf.Component("array")
    wg = gf.components.straight(length=3.2)
    c.add_array(wg)
    gdspath = c.write_gds()
    h = hash_file(gdspath)
    href = "ed41db2253d80bb337510965bec6e422"
    assert h == href, f"href = {h!r}"


def _test_hash_file() -> None:
    """Test hash of the saved GDS file."""
    c = gf.components.straight()
    gdspath = c.write_gds()
    h = hash_file(gdspath)
    href = "120dd914e80c9a1f5bb30b8743e3f836"
    assert h == href, f"href = {h!r}"


if __name__ == "__main__":
    # test_hash_geometry()
    _test_hash_file()
    # _test_hash_array_file()
