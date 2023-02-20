import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.wafer(reticle='die', cols=[2, 6, 6, 8, 8, 6, 6, 2])
c.plot_matplotlib()