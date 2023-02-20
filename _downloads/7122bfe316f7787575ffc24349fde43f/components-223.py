import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.verniers(widths=[0.1, 0.2, 0.3, 0.4, 0.5], gap=0.1, xsize=100, layer_label='LABEL')
c.plot_matplotlib()