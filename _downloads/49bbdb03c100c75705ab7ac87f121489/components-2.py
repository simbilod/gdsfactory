import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.L(width=1, size=[10, 20], layer='M3', port_type='electrical')
c.plot_matplotlib()