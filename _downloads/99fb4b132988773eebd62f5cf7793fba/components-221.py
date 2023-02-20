import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.text_rectangular_multi_layer(text='abcd', layers=['WG', 'M1', 'M2', 'M3'])
c.plot_matplotlib()