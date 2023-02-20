import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.fiber(core_diameter=10, cladding_diameter=125, layer_core='WG', layer_cladding='WGCLAD')
c.plot_matplotlib()