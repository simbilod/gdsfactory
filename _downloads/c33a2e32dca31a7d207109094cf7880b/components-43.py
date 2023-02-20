import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler90circular(gap=0.2, radius=10.0, cross_section='strip')
c.plot_matplotlib()