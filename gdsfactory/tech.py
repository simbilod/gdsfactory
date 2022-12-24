"""Technology settings."""
from __future__ import annotations

import pathlib
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from pydantic import BaseModel

from gdsfactory.materials import MaterialSpec

module_path = pathlib.Path(__file__).parent.absolute()
Layer = Tuple[int, int]
LayerSpec = Union[int, Layer, str, None]
nm = 1e-3


class LayerMap(BaseModel):
    """Generic layermap based on book.

    Lukas Chrostowski, Michael Hochberg, "Silicon Photonics Design",
    Cambridge University Press 2015, page 353
    You will need to create a new LayerMap with your specific foundry layers.
    """

    WAFER: Layer = (0, 0)

    WG: Layer = (1, 0)
    WGCLAD: Layer = (111, 0)
    SLAB150: Layer = (2, 0)
    SLAB90: Layer = (3, 0)
    DEEPTRENCH: Layer = (4, 0)
    GE: Layer = (5, 0)
    UNDERCUT: Layer = (6, 0)
    WGN: Layer = (34, 0)
    WGN_CLAD: Layer = (36, 0)

    N: Layer = (20, 0)
    NP: Layer = (22, 0)
    NPP: Layer = (24, 0)
    P: Layer = (21, 0)
    PP: Layer = (23, 0)
    PPP: Layer = (25, 0)
    GEN: Layer = (26, 0)
    GEP: Layer = (27, 0)

    HEATER: Layer = (47, 0)
    M1: Layer = (41, 0)
    M2: Layer = (45, 0)
    M3: Layer = (49, 0)
    VIAC: Layer = (40, 0)
    VIA1: Layer = (44, 0)
    VIA2: Layer = (43, 0)
    PADOPEN: Layer = (46, 0)

    DICING: Layer = (100, 0)
    NO_TILE_SI: Layer = (71, 0)
    PADDING: Layer = (67, 0)
    DEVREC: Layer = (68, 0)
    FLOORPLAN: Layer = (64, 0)
    TEXT: Layer = (66, 0)
    PORT: Layer = (1, 10)
    PORTE: Layer = (1, 11)
    PORTH: Layer = (70, 0)
    SHOW_PORTS: Layer = (1, 12)
    LABEL: Layer = (201, 0)
    LABEL_SETTINGS: Layer = (202, 0)
    TE: Layer = (203, 0)
    TM: Layer = (204, 0)
    DRC_MARKER: Layer = (205, 0)
    LABEL_INSTANCE: Layer = (206, 0)
    ERROR_MARKER: Layer = (207, 0)
    ERROR_PATH: Layer = (208, 0)

    SOURCE: Layer = (110, 0)
    MONITOR: Layer = (101, 0)

    class Config:
        """pydantic config."""

        frozen = True
        extra = "forbid"


LAYER = LayerMap()
PORT_MARKER_LAYER_TO_TYPE = {
    LAYER.PORT: "optical",
    LAYER.PORTE: "dc",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_LAYER_TO_TYPE = {
    LAYER.WG: "optical",
    LAYER.WGN: "optical",
    LAYER.SLAB150: "optical",
    LAYER.M1: "dc",
    LAYER.M2: "dc",
    LAYER.M3: "dc",
    LAYER.TE: "vertical_te",
    LAYER.TM: "vertical_tm",
}

PORT_TYPE_TO_MARKER_LAYER = {v: k for k, v in PORT_MARKER_LAYER_TO_TYPE.items()}


class LayerLevel(BaseModel):
    """Level for 3D LayerStack.

    Parameters:
        layer: (GDSII Layer number, GDSII datatype).
        thickness: layer thickness in um.
        thickness_tolerance: layer thickness tolerance in um.
        zmin: height position where material starts in um.
        material: material name.
        sidewall_angle: in degrees with respect to normal.
        width_to_z: if sidewall_angle, relative z-position
            (0 --> zmin, 1 --> zmin + thickness).
        z_to_bias: parametrizes shrinking/expansion of the design GDS layer
            when extruding from zmin (0) to zmin + thickness (1).
            Defaults no buffering [[0, 1], [0, 0]].
        info: simulation_info and other types of metadata.
            mesh_order: lower mesh order (1) will have priority over higher
                mesh order (2) in the regions where materials overlap.
            refractive_index: refractive_index
                can be int, complex or function that depends on wavelength (um).
            type: grow, etch, implant, or background.
            mode: octagon, taper, round.
                https://gdsfactory.github.io/klayout_pyxs/DocGrow.html
            into: etch into another layer.
                https://gdsfactory.github.io/klayout_pyxs/DocGrow.html
            doping_concentration: for implants.
            resistivity: for metals.
            bias: in um for the etch.
    """

    layer: Optional[Tuple[int, int]]
    thickness: float
    thickness_tolerance: Optional[float] = None
    zmin: float
    material: Optional[str] = None
    sidewall_angle: float = 0.0
    width_to_z: float = 0.0
    z_to_bias: Optional[Tuple[List[float], List[float]]] = None
    info: Dict[str, Any] = {}


class LayerStack(BaseModel):
    """For simulation and 3D rendering.

    Parameters:
        layers: dict of layer_levels.
    """

    layers: Dict[str, LayerLevel]

    def get_layer_to_thickness(self) -> Dict[Tuple[int, int], float]:
        """Returns layer tuple to thickness (um)."""
        return {
            level.layer: level.thickness
            for level in self.layers.values()
            if level.thickness
        }

    def get_layer_to_zmin(self) -> Dict[Tuple[int, int], float]:
        """Returns layer tuple to z min position (um)."""
        return {
            level.layer: level.zmin for level in self.layers.values() if level.thickness
        }

    def get_layer_to_material(self) -> Dict[Tuple[int, int], str]:
        """Returns layer tuple to material name."""
        return {
            level.layer: level.material
            for level in self.layers.values()
            if level.thickness
        }

    def get_layer_to_sidewall_angle(self) -> Dict[Tuple[int, int], str]:
        """Returns layer tuple to material name."""
        return {
            level.layer: level.sidewall_angle
            for level in self.layers.values()
            if level.thickness
        }

    def get_layer_to_info(self) -> Dict[Tuple[int, int], Dict]:
        """Returns layer tuple to info dict."""
        return {level.layer: level.info for level in self.layers.values()}

    def to_dict(self) -> Dict[str, Dict[str, Any]]:
        return {level_name: dict(level) for level_name, level in self.layers.items()}

    def get_klayout_3d_script(
        self,
        klayout28: bool = True,
        print_to_console: bool = True,
        layer_display_properties=None,
        dbu: Optional[float] = 0.001,
    ) -> str:
        """Prints script for 2.5 view KLayout information.

        You can add this information in your tech.lyt take a look at
        gdsfactory/klayout/tech/tech.lyt
        """
        out = ""
        for layer_name, level in self.layers.items():
            layer = level.layer
            zmin = level.zmin
            zmax = zmin + level.thickness

            if layer is None:
                continue

            if dbu:
                rnd_pl = len(str(dbu).split(".")[-1])
                zmin = round(zmin, rnd_pl)
                zmax = round(zmax, rnd_pl)

            if klayout28:
                txt = (
                    f"z("
                    f"input({layer[0]}, {layer[1]}), "
                    f"zstart: {zmin}, "
                    f"zstop: {zmax}, "
                    f"name: '{layer_name}: {level.material} {layer[0]}/{layer[1]}'"
                )
                if layer_display_properties:
                    txt += ", "
                    props = layer_display_properties.get_from_tuple(layer)
                    if props.fill_color == props.frame_color:
                        txt += f"color: {props.frame_color}"
                    else:
                        txt += (
                            f"fill: {props.fill_color}, " f"frame: {props.frame_color}"
                        )

                txt += ")"

            else:
                txt = f"{layer[0]}/{layer[1]}: {zmin} {zmax}"
            out += f"{txt}\n"

            if print_to_console:
                print(txt)
        if klayout28:
            out += "\nend\n"
        return out


def get_layer_stack_generic(
    thickness_wg: float = 220 * nm,
    thickness_slab_deep_etch: float = 90 * nm,
    thickness_clad: float = 3.0,
    thickness_nitride: float = 350 * nm,
    thickness_ge: float = 500 * nm,
    gap_silicon_to_nitride: float = 100 * nm,
    zmin_heater: float = 1.1,
    zmin_metal1: float = 1.1,
    thickness_metal1: float = 700 * nm,
    zmin_metal2: float = 2.3,
    thickness_metal2: float = 700 * nm,
    zmin_metal3: float = 3.2,
    thickness_metal3: float = 2000 * nm,
    substrate_thickness: float = 10.0,
    box_thickness: float = 3.0,
    undercut_thickness: float = 5.0,
) -> LayerStack:
    """Returns generic LayerStack.

    based on paper https://www.degruyter.com/document/doi/10.1515/nanoph-2013-0034/html

    Args:
        thickness_wg: waveguide thickness in um.
        thickness_slab_deep_etch: for deep etched slab.
        thickness_clad: cladding thickness in um.
        thickness_nitride: nitride thickness in um.
        thickness_ge: germanium thickness.
        gap_silicon_to_nitride: distance from silicon to nitride in um.
        zmin_heater: TiN heater.
        zmin_metal1: metal1.
        thickness_metal1: metal1 thickness.
        zmin_metal2: metal2.
        thickness_metal2: metal2 thickness.
        zmin_metal3: metal3.
        thickness_metal3: metal3 thickness.
        substrate_thickness: substrate thickness in um.
        box_thickness: bottom oxide thickness in um.
        undercut_thickness: thickness of the silicon undercut.
    """
    return LayerStack(
        layers=dict(
            substrate=LayerLevel(
                layer=LAYER.WAFER,
                thickness=substrate_thickness,
                zmin=-substrate_thickness - box_thickness,
                material="si",
                info={"mesh_order": 99},
            ),
            box=LayerLevel(
                layer=LAYER.WAFER,
                thickness=box_thickness,
                zmin=-box_thickness,
                material="sio2",
                info={"mesh_order": 99},
            ),
            core=LayerLevel(
                layer=LAYER.WG,
                thickness=thickness_wg,
                zmin=0.0,
                material="si",
                info={"mesh_order": 1},
                sidewall_angle=10,
                width_to_z=0.5,
            ),
            clad=LayerLevel(
                # layer=LAYER.WGCLAD,
                layer=LAYER.WAFER,
                zmin=0.0,
                material="sio2",
                thickness=thickness_clad,
                info={"mesh_order": 10},
            ),
            slab150=LayerLevel(
                layer=LAYER.SLAB150,
                thickness=150e-3,
                zmin=0,
                material="si",
                info={"mesh_order": 3},
            ),
            slab90=LayerLevel(
                layer=LAYER.SLAB90,
                thickness=thickness_slab_deep_etch,
                zmin=0.0,
                material="si",
                info={"mesh_order": 2},
            ),
            nitride=LayerLevel(
                layer=LAYER.WGN,
                thickness=thickness_nitride,
                zmin=thickness_wg + gap_silicon_to_nitride,
                material="sin",
                info={"mesh_order": 2},
            ),
            ge=LayerLevel(
                layer=LAYER.GE,
                thickness=thickness_ge,
                zmin=thickness_wg,
                material="ge",
                info={"mesh_order": 1},
            ),
            undercut=LayerLevel(
                layer=LAYER.UNDERCUT,
                thickness=-undercut_thickness,
                zmin=-box_thickness,
                material="air",
                z_to_bias=[
                    [0, 0.3, 0.6, 0.8, 0.9, 1],
                    [-0, -0.5, -1, -1.5, -2, -2.5],
                ],
                info={"mesh_order": 1},
            ),
            via_contact=LayerLevel(
                layer=LAYER.VIAC,
                thickness=zmin_metal1 - thickness_slab_deep_etch,
                zmin=thickness_slab_deep_etch,
                material="Aluminum",
                info={"mesh_order": 1},
                sidewall_angle=-10,
                width_to_z=0,
            ),
            metal1=LayerLevel(
                layer=LAYER.M1,
                thickness=thickness_metal1,
                zmin=zmin_metal1,
                material="Aluminum",
                info={"mesh_order": 2},
            ),
            heater=LayerLevel(
                layer=LAYER.HEATER,
                thickness=750e-3,
                zmin=zmin_heater,
                material="TiN",
                info={"mesh_order": 1},
            ),
            via1=LayerLevel(
                layer=LAYER.VIA1,
                thickness=zmin_metal2 - (zmin_metal1 + thickness_metal1),
                zmin=zmin_metal1 + thickness_metal1,
                material="Aluminum",
                info={"mesh_order": 2},
            ),
            metal2=LayerLevel(
                layer=LAYER.M2,
                thickness=thickness_metal2,
                zmin=zmin_metal2,
                material="Aluminum",
                info={"mesh_order": 2},
            ),
            via2=LayerLevel(
                layer=LAYER.VIA2,
                thickness=zmin_metal3 - (zmin_metal2 + thickness_metal2),
                zmin=zmin_metal2 + thickness_metal2,
                material="Aluminum",
                info={"mesh_order": 1},
            ),
            metal3=LayerLevel(
                layer=LAYER.M3,
                thickness=thickness_metal3,
                zmin=zmin_metal3,
                material="Aluminum",
                info={"mesh_order": 2},
            ),
        )
    )


LAYER_STACK = get_layer_stack_generic()


class Section(BaseModel):
    """CrossSection to extrude a path with a waveguide.

    Parameters:
        width: of the section (um) or parameterized function from 0 to 1.
             the width at t==0 is the width at the beginning of the Path.
             the width at t==1 is the width at the end.
        offset: center offset (um) or function parameterized function from 0 to 1.
             the offset at t==0 is the offset at the beginning of the Path.
             the offset at t==1 is the offset at the end.
        layer: layer spec.
        port_names: Optional port names.
        port_types: optical, electrical, ...
        name: Optional Section name.
        hidden: hide layer.
    .. code::
          0   offset
          |<-------------->|
          |              _____
          |             |     |
          |             |layer|
          |             |_____|
          |              <---->
                         width
    """

    width: Union[float, Callable]
    offset: Union[float, Callable] = 0
    layer: Union[LayerSpec, Tuple[LayerSpec, LayerSpec]]
    port_names: Tuple[Optional[str], Optional[str]] = (None, None)
    port_types: Tuple[str, str] = ("optical", "optical")
    name: Optional[str] = None
    hidden: bool = False

    class Config:
        """pydantic basemodel config."""

        extra = "forbid"


material_name_to_lumerical: Dict[str, MaterialSpec] = {
    "si": "Si (Silicon) - Palik",
    "sio2": "SiO2 (Glass) - Palik",
    "sin": "Si3N4 (Silicon Nitride) - Phillip",
}


class SimulationSettingsLumericalFdtd(BaseModel):
    """Lumerical FDTD simulation_settings.

    Parameters:
        background_material: for the background.
        port_margin: on both sides of the port width (um).
        port_height: port height (um).
        port_extension: port extension (um).
        mesh_accuracy: 2 (1: coarse, 2: fine, 3: superfine).
        zmargin: for the FDTD region (um).
        ymargin: for the FDTD region (um).
        xmargin: for the FDTD region (um).
        wavelength_start: 1.2 (um).
        wavelength_stop: 1.6 (um).
        wavelength_points: 500.
        simulation_time: (s) related to max path length
            3e8/2.4*10e-12*1e6 = 1.25mm.
        simulation_temperature: in kelvin (default = 300).
        frequency_dependent_profile: compute mode profiles for each wavelength.
        field_profile_samples: number of wavelengths to compute field profile.
    """

    background_material: str = "sio2"
    port_margin: float = 1.5
    port_extension: float = 5.0
    mesh_accuracy: int = 2
    zmargin: float = 1.0
    ymargin: float = 3.0
    xmargin: float = 3.0
    wavelength_start: float = 1.2
    wavelength_stop: float = 1.6
    wavelength_points: int = 500
    simulation_time: float = 10e-12
    simulation_temperature: float = 300
    frequency_dependent_profile: bool = True
    field_profile_samples: int = 15
    distance_source_to_monitors: float = 0.2
    material_name_to_lumerical: Dict[str, MaterialSpec] = material_name_to_lumerical

    class Config:
        """pydantic basemodel config."""

        arbitrary_types_allowed = True


SIMULATION_SETTINGS_LUMERICAL_FDTD = SimulationSettingsLumericalFdtd()


def assert_callable(function):
    if not callable(function):
        raise ValueError(
            f"Error: function = {function} with type {type(function)} is not callable"
        )


if __name__ == "__main__":
    # import gdsfactory as gf
    # from gdsfactory.serialization import clean_value_json

    # d = clean_value_json(SIMULATION_SETTINGS_LUMERICAL_FDTD)

    # def mmi1x2_longer(length_mmi: float = 25.0, **kwargs):
    #     return gf.components.mmi1x2(length_mmi=length_mmi, **kwargs)

    # def mzi_longer(**kwargs):
    #     return gf.components.mzi(splitter=mmi1x2_longer, **kwargs)

    ls = LAYER_STACK
    ls.get_klayout_3d_script()
    # print(ls.get_layer_to_material())
    # print(ls.get_layer_to_thickness())

    # s = Section(width=1, layer=(1, 0))
    # print(s)
