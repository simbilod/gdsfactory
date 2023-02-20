import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cutback_bend180(straight_length=5.0, rows=6, columns=6, spacing=3)
c.plot_matplotlib()