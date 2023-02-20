import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.copy_layers(layers=[[1, 0], [2, 0]])
c.plot_matplotlib()