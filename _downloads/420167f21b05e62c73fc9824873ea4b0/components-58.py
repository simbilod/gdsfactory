import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cutback_2x2(cols=4, port1='o1', port2='o2', port3='o3', port4='o4')
c.plot_matplotlib()