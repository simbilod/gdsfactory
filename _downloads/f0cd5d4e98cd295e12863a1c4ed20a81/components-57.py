import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.crossing_from_taper()
c.plot_matplotlib()