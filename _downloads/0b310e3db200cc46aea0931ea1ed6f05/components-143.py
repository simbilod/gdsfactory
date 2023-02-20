import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pad(size=[100.0, 100.0], layer='MTOP', port_inclusion=0)
c.plot_matplotlib()