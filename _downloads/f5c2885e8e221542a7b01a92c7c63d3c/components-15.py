import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.awg(arms=10, outputs=3, fpr_spacing=50.0)
c.plot_matplotlib()