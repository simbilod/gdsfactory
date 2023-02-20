import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.text_rectangular(text='abcd', size=10.0, position=[0.0, 0.0], justify='left', layer='WG')
c.plot_matplotlib()