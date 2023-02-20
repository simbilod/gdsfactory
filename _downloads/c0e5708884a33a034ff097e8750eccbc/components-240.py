import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.wire_sbend(dx=20.0, dy=10.0)
c.plot_matplotlib()