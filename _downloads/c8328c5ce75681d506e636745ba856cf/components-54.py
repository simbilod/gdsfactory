import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.crossing45(port_spacing=40.0, alpha=0.08, npoints=101, cross_section='strip')
c.plot_matplotlib()