import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.version_stamp(labels=['demo_label'], with_qr_code=False, layer='WG', pixel_size=1, text_size=10)
c.plot_matplotlib()