import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.align_wafer(width=10.0, spacing=10.0, cross_length=80.0, layer='WG', square_corner='bottom_left')
c.plot_matplotlib()