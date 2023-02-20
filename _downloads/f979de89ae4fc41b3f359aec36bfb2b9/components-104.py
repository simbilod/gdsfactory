import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_tm(polarization='tm', taper_length=16.6, taper_angle=30.0, trenches_extra_angle=9.0, wavelength=1.53, fiber_angle=15.0, grating_line_width=0.6, neff=1.8, ncladding=1.443, layer_trench='SLAB150', p_start=26, n_periods=30, end_straight_length=0.2, cross_section='strip')
c.plot_matplotlib()