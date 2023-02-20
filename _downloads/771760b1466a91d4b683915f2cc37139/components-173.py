import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.spiral_double(min_bend_radius=10.0, separation=2.0, number_of_loops=3, npoints=1000, cross_section='strip')
c.plot_matplotlib()