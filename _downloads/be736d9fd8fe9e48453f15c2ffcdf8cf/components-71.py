import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.delay_snake3(length=1600.0, length0=0.0, n=2, cross_section='strip')
c.plot_matplotlib()