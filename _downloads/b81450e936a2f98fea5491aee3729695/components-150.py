import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.pad_gsg_short(size=[22, 7], layer_metal='M3', metal_spacing=5.0, short=True, pad_spacing=150)
c.plot_matplotlib()