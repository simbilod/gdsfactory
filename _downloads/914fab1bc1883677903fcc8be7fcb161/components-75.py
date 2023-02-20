import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.die_bbox(street_width=100.0, text_size=100.0, text_anchor='sw', layer='M3', padding=10.0)
c.plot_matplotlib()