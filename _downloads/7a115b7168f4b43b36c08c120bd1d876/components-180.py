import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.splitter_chain(columns=3)
c.plot_matplotlib()