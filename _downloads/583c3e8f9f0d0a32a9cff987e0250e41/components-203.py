import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.taper_cross_section_linear(length=10, npoints=2, linear=True, width_type='sine')
c.plot_matplotlib()