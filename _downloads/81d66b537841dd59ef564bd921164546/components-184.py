import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_array(n=4, spacing=4.0)
c.plot_matplotlib()