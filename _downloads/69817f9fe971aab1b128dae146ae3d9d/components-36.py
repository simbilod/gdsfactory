import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.compensation_path(direction='top', cross_section='strip')
c.plot_matplotlib()