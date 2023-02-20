import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ellipse(radii=[10.0, 5.0], angle_resolution=2.5, layer='WG')
c.plot_matplotlib()