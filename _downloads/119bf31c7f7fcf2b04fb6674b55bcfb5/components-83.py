import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.extend_ports(length=5.0, port_type='optical', centered=False)
c.plot_matplotlib()