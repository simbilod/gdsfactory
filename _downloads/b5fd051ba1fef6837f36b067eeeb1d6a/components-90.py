import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_elliptical(polarization='te', taper_length=16.6, taper_angle=40.0, wavelength=1.554, fiber_angle=15.0, grating_line_width=0.343, neff=2.638, nclad=1.443, n_periods=30, big_last_tooth=False, layer_slab='SLAB150', slab_xmin=-1.0, slab_offset=2.0, spiked=True, cross_section='strip')
c.plot_matplotlib()