import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_ring(gap=0.2, radius=5.0, length_x=4.0, cross_section='strip')
c.plot_matplotlib()