import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.C(width=1.0, size=[10.0, 20.0], layer='WG')
c.plot_matplotlib()