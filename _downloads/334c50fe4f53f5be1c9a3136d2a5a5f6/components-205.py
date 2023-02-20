import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_cross_section_sine(length=10, npoints=101, linear=False, width_type='sine')
c.plot_matplotlib()