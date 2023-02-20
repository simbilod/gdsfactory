import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pad_array0(pad='pad', spacing=[150.0, 150.0], columns=1, rows=3, orientation=0)
c.plot_matplotlib()