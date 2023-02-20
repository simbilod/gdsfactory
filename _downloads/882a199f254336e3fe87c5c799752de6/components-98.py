import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_loss_fiber_array4(pitch=127.0)
c.plot_matplotlib()