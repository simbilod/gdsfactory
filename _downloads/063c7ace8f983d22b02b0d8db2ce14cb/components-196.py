import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_rib(length=10.0, npoints=2, with_bbox=True)
c.plot_matplotlib()