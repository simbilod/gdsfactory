import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_loss_fiber_single(cross_section='strip')
c.plot_matplotlib()