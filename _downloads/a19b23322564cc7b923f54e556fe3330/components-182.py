import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.staircase(length_v=5.0, length_h=5.0, rows=4)
c.plot_matplotlib()