import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_straight_asymmetric(length=10.0, gap=0.27, width_top=0.5, width_bot=1)
c.plot_matplotlib()