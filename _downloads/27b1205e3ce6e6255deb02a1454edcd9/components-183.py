import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight(length=10.0, npoints=2, with_bbox=True, cross_section='strip')
c.plot_matplotlib()