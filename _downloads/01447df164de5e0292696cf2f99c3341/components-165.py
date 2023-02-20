import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ring_single(gap=0.2, radius=10.0, length_x=4.0, length_y=0.6, cross_section='strip')
c.plot_matplotlib()