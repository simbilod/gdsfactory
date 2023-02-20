import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_loss_fiber_array(pitch=127.0, input_port_indexes=[0, 1])
c.plot_matplotlib()