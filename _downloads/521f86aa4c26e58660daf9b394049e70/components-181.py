import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.splitter_tree(noutputs=4, spacing=[90.0, 50.0], cross_section='strip')
c.plot_matplotlib()