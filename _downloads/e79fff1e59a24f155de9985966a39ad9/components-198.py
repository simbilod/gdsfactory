import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.switch_tree(noutputs=4, spacing=[500, 100], cross_section='strip')
c.plot_matplotlib()