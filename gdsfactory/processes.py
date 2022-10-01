from dataclasses import dataclass
from xmlrpc.client import Boolean

@dataclass
class Deposit:
    """Add material.

    Args:
        material (str): material tag
        thickness (float): thickness to add
        positive_tone (bool): whether to operate at the layer location (positive tone resist), or not at the layer location (negative tone resist)
    """
    material: str
    thickness: float
    positive_tone: Boolean = True

@dataclass
class Etch:
    """Remove material at mask location.

    Args:
        material (str): material tag
        depth (float): thickness to remove
        
    TODO: add profile
    """
    material: str
    thickness: float

@dataclass
class Implant:
    """Implant ions.

    Args:
        element (str): element tag
        simulate (bool): whether to use a provided profile (False), or calculate a profile from parameters (True)
        depth (float): 
        energy (float): thickness to remove
            """
    element: str
    depth: float
    vertical_straggle: float
    lateral_straggle: float
    simulate: Boolean = False
    profile: str = "Gaussian"

@dataclass
class Diffuse:
    """Simulates diffusion of impurities and healing of defects. Assumes very sharp rampup and rampdown.

    Args:
        time (float)
        temperature (float): temperature
            """
    time: float
    temperature: float
