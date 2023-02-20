import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.text_lines(text=['Chip', '01'], size=0.4, layer='WG')
c.plot_matplotlib()