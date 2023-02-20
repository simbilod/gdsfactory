import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cutback_component(cols=4, rows=5, port1='o1', port2='o2', mirror=False, cross_section='strip')
c.plot_matplotlib()