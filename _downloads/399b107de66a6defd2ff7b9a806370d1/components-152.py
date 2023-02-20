import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pixel(size=1.0, layer='WG')
c.plot_matplotlib()