import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_symmetric(gap=0.234, dy=5.0, dx=10.0, cross_section='strip')
c.plot_matplotlib()