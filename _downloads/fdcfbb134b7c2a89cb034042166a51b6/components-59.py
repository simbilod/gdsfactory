import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cutback_bend(straight_length=5.0, rows=6, columns=5)
c.plot_matplotlib()