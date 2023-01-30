"""In programming, a factory is a function that returns an object.

Functions are easy to understand because they have clear inputs and outputs.
Most gdsfactory functions take some inputs and return a Component object.
Some of these inputs parameters are also functions.

- Component: Object with.
    - name.
    - references: to other components (x, y, rotation).
    - polygons in different layers.
    - ports dict.
- Route: dataclass with 3 attributes.
    - references: list of references (straights, bends and tapers).
    - ports: dict(input=PortIn, output=PortOut).
    - length: how long is this route?

Factories:

- ComponentFactory: function that returns a Component.
- RouteFactory: function that returns a Route.


Specs:

- ComponentSpec: Component, function, string or dict
    (component=mzi, settings=dict(delta_length=20)).
- LayerSpec: (3, 0), 3 (assumes 0 as datatype) or string.

"""
from __future__ import annotations

import json
import pathlib
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

import gdstk
import numpy as np
from gdstk import Label
from omegaconf import OmegaConf
from pydantic import BaseModel, Extra
from typing_extensions import Literal

from gdsfactory.component import Component, ComponentReference
from gdsfactory.cross_section import CrossSection, Section
from gdsfactory.port import Port
from gdsfactory.technology import LayerLevel, LayerStack

Anchor = Literal[
    "ce",
    "cw",
    "nc",
    "ne",
    "nw",
    "sc",
    "se",
    "sw",
    "center",
    "cc",
]
Axis = Literal["x", "y"]
NSEW = Literal["N", "S", "E", "W"]
WidthTypes = Literal["sine", "linear", "parabolic"]


Float2 = Tuple[float, float]
Float3 = Tuple[float, float, float]
Floats = Tuple[float, ...]
Strs = Tuple[str, ...]
Int2 = Tuple[int, int]
Int3 = Tuple[int, int, int]
Ints = Tuple[int, ...]

Layer = Tuple[int, int]  # Tuple of integer (layer, datatype)
Layers = Tuple[Layer, ...]

LayerSpec = Union[
    Layer, int, str, None
]  # tuple of integers (layer, datatype), a integer (layer, 0) or a string (layer_name)

LayerSpecs = Optional[Tuple[LayerSpec, ...]]
ComponentFactory = Callable[..., Component]
ComponentFactoryDict = Dict[str, ComponentFactory]
PathType = Union[str, pathlib.Path]
PathTypes = Tuple[PathType, ...]

ComponentOrPath = Union[PathType, Component]
ComponentOrReference = Union[Component, ComponentReference]
NameToFunctionDict = Dict[str, ComponentFactory]
Number = Union[float, int]
Coordinate = Tuple[float, float]
Coordinates = Tuple[Coordinate, ...]
ComponentOrPath = Union[Component, PathType]
CrossSectionFactory = Callable[..., CrossSection]
CrossSectionOrFactory = Union[CrossSection, Callable[..., CrossSection]]
PortSymmetries = Dict[str, List[str]]
PortsDict = Dict[str, Port]
PortsList = Dict[str, Port]

ComponentSpec = Union[
    str, ComponentFactory, Component, Dict[str, Any]
]  # PCell function, function name, dict or Component

ComponentSpecOrList = Union[ComponentSpec, List[ComponentSpec]]
CellSpec = Union[
    str, ComponentFactory, Dict[str, Any]
]  # PCell function, function name or dict

ComponentSpecDict = Dict[str, ComponentSpec]
CrossSectionSpec = Union[
    str, CrossSectionFactory, CrossSection, Dict[str, Any]
]  # cross_section function, function name or dict

MultiCrossSectionAngleSpec = List[Tuple[CrossSectionSpec, Tuple[int, ...]]]


class Route(BaseModel):
    references: List[ComponentReference]
    labels: Optional[List[gdstk.Label]] = None
    ports: Tuple[Port, Port]
    length: float

    class Config:
        """Config for Route."""

        extra = Extra.forbid
        arbitrary_types_allowed = True


class Routes(BaseModel):
    references: List[ComponentReference]
    lengths: List[float]
    ports: Optional[List[Port]] = None
    bend_radius: Optional[List[float]] = None

    class Config:
        """Config for Routes."""

        extra = Extra.forbid


class ComponentModel(BaseModel):
    component: Union[str, Dict[str, Any]]
    settings: Optional[Dict[str, Any]]

    class Config:
        extra = Extra.forbid


class PlacementModel(BaseModel):
    x: Union[str, float] = 0
    y: Union[str, float] = 0
    xmin: Optional[Union[str, float]] = None
    ymin: Optional[Union[str, float]] = None
    xmax: Optional[Union[str, float]] = None
    ymax: Optional[Union[str, float]] = None
    dx: float = 0
    dy: float = 0
    port: Optional[Union[str, Anchor]] = None
    rotation: int = 0
    mirror: bool = False

    class Config:
        extra = Extra.forbid


class RouteModel(BaseModel):
    links: Dict[str, str]
    settings: Optional[Dict[str, Any]] = None
    routing_strategy: Optional[str] = None

    class Config:
        extra = Extra.forbid


class NetlistModel(BaseModel):
    """Netlist defined component.

    Parameters:
        instances: dict of instances (name, settings, component).
        placements: dict of placements.
        connections: dict of connections.
        routes: dict of routes.
        name: component name.
        info: information (polarization, wavelength ...).
        settings: input variables.
        ports: exposed component ports.

    """

    instances: Optional[Dict[str, ComponentModel]] = None
    placements: Optional[Dict[str, PlacementModel]] = None
    connections: Optional[Dict[str, str]] = None
    routes: Optional[Dict[str, RouteModel]] = None
    name: Optional[str] = None
    info: Optional[Dict[str, Any]] = None
    settings: Optional[Dict[str, Any]] = None
    ports: Optional[Dict[str, str]] = None

    class Config:
        extra = Extra.forbid


RouteFactory = Callable[..., Route]


class TypedArray(np.ndarray):
    """based on https://github.com/samuelcolvin/pydantic/issues/380."""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate_type

    @classmethod
    def validate_type(cls, val):
        return np.array(val, dtype=cls.inner_type)


class ArrayMeta(type):
    def __getitem__(self, t):
        return type("Array", (TypedArray,), {"inner_type": t})


class Array(np.ndarray, metaclass=ArrayMeta):
    pass


__all__ = (
    "ComponentFactory",
    "ComponentFactoryDict",
    "ComponentSpec",
    "ComponentOrPath",
    "ComponentOrReference",
    "Coordinate",
    "Coordinates",
    "CrossSectionFactory",
    "CrossSectionOrFactory",
    "MultiCrossSectionAngleSpec",
    "Float2",
    "Float3",
    "Floats",
    "Int2",
    "Int3",
    "Ints",
    "Layer",
    "Label",
    "Layers",
    "LayerLevel",
    "LayerStack",
    "NameToFunctionDict",
    "Number",
    "PathType",
    "PathTypes",
    "Route",
    "RouteFactory",
    "Routes",
    "Strs",
    "Section",
)


def write_schema(model: BaseModel = NetlistModel) -> None:
    from gdsfactory.config import PATH

    s = model.schema_json()
    d = OmegaConf.create(s)

    schema_path_json = PATH.schema_netlist
    schema_path_yaml = schema_path_json.with_suffix(".yaml")

    schema_path_yaml.write_text(OmegaConf.to_yaml(d))
    schema_path_json.write_text(json.dumps(OmegaConf.to_container(d)))


def _demo():
    write_schema()

    import jsonschema
    import yaml

    from gdsfactory.config import PATH

    schema_path_json = PATH.schema_netlist
    schema_dict = json.loads(schema_path_json.read_text())

    yaml_text = """

name: mzi

pdk: ubcpdk

settings:
   dy: -90

info:
    polarization: te
    wavelength: 1.55
    description: mzi for ubcpdk

instances:
    yr:
      component: y_splitter
    yl:
      component: y_splitter

placements:
    yr:
        rotation: 180
        x: 100
        y: 0

routes:
    route_top:
        links:
            yl,opt2: yr,opt3
        settings:
            cross_section: strip
    route_bot:
        links:
            yl,opt3: yr,opt2
        routing_strategy: get_bundle_from_steps
        settings:
          steps: [dx: 30, dy: '${settings.dy}', dx: 20]
          cross_section: strip

ports:
    o1: yl,opt1
    o2: yr,opt1
"""

    yaml_dict = yaml.safe_load(yaml_text)
    jsonschema.validate(yaml_dict, schema_dict)

    # from gdsfactory.components import factory
    # c = NetlistModel(factory=factory)
    # c.add_instance("mmi1", "mmi1x2", length=13.3)


if __name__ == "__main__":
    _demo()
