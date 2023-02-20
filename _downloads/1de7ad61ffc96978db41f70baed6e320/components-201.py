import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_0p5_to_3_l36(cross_section='strip')
c.plot_matplotlib()