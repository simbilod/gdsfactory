import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.mmi1x2_with_sbend(with_sbend=True, cross_section='strip')
c.plot_matplotlib()