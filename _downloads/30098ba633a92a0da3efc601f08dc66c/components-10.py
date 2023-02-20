import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.array(spacing=[150.0, 150.0], columns=6, rows=1, add_ports=True)
c.plot_matplotlib()