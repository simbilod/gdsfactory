import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_rib_tapered(length=5.0, port1='o2', port2='o1', port_type='optical', centered=False)
c.plot_matplotlib()