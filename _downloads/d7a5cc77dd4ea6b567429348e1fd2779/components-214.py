import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_w11_l200(cross_section='strip')
c.plot_matplotlib()