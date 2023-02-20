import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.bend_circular(angle=90.0, with_bbox=True, cross_section='strip')
c.plot_matplotlib()