import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_w10_l100(cross_section='strip')
c.plot_matplotlib()