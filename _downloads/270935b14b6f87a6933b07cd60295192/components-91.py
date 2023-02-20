import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_elliptical_arbitrary(gaps=[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], widths=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], taper_length=16.6, taper_angle=60.0, wavelength=1.554, fiber_angle=15.0, nclad=1.443, layer_slab='SLAB150', taper_to_slab_offset=-3.0, polarization='te', spiked=True, bias_gap=0, cross_section='strip')
c.plot_matplotlib()