import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_from_csv(cross_section='strip')
c.plot_matplotlib()