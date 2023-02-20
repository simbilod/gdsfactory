import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ring_single_array(spacing=5.0, cross_section='strip')
c.plot_matplotlib()