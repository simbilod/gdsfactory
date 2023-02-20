import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.loss_deembedding_ch14_23(pitch=127.0, input_port_indexes=[0, 1])
c.plot_matplotlib()