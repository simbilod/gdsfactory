import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.compass(size=[4.0, 2.0], layer='WG', port_type='placement', port_inclusion=0.0, port_orientations=[180, 90, 0, -90])
c.plot_matplotlib()