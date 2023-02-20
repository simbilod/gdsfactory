import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.marker_te(layer='TE', centered=True, port_type='placement', port_orientations=[180, 90, 0, -90])
c.plot_matplotlib()