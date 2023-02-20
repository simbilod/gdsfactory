import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.loss_deembedding_ch13_24(pitch=127.0, input_port_indexes=[0, 1], cross_section='strip')
c.plot_matplotlib()