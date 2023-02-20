import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.add_fiducials(gap=50, left='cross', right='cross', offset=[0, 0])
c.plot_matplotlib()