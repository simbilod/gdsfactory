import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_straight(length=10.0, gap=0.27)
c.plot_matplotlib()