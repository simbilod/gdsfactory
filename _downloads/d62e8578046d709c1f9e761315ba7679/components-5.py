import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.add_frame(width=10.0, spacing=10.0, layer='WG')
c.plot_matplotlib()