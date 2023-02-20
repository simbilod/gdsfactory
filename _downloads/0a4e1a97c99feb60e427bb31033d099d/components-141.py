import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pack_doe(doe='mmi1x2', do_permutations=False)
c.plot_matplotlib()