import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.delay_snake2(length=1600.0, length0=0.0, n=2, bend180='bend_euler180', cross_section='strip')
c.plot_matplotlib()