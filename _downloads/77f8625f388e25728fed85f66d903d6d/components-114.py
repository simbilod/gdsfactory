import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.loss_deembedding_ch12_34(pitch=127.0, input_port_indexes=[0, 2])
c.plot_matplotlib()