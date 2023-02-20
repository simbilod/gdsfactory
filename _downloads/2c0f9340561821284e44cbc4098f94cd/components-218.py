import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.text_freetype(text='abcd', size=10, justify='left', layer='WG', font='DEPLOF')
c.plot_matplotlib()