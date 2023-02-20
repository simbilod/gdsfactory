import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cross(length=10.0, width=3.0, layer='WG')
c.plot_matplotlib()