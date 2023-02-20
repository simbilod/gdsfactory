import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ring_double(gap=0.2, radius=10.0, length_x=0.01, length_y=0.01, cross_section='strip')
c.plot_matplotlib()