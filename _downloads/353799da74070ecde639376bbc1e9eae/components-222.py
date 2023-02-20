import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.triangle(x=10, xtop=0, y=20, ybot=0, layer='WG')
c.plot_matplotlib()