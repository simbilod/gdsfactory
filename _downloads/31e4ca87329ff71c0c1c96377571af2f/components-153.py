import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.qrcode(data='mask01', psize=1, layer='WG')
c.plot_matplotlib()