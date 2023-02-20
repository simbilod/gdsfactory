import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pad_array270(pad='pad', spacing=[150.0, 150.0], columns=6, rows=1, orientation=270)
c.plot_matplotlib()