import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_rectangular_arbitrary(gaps=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2], widths=[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], width_grating=11.0, length_taper=150.0, polarization='te', wavelength=1.55, layer_slab='SLAB150', slab_xmin=-1.0, slab_offset=1.0, fiber_angle=15, cross_section='strip')
c.plot_matplotlib()