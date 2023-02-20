import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.logo(text='GDSFACTORY')
c.plot_matplotlib()