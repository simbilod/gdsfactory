import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_elliptical_uniform(n_periods=20, period=0.75, fill_factor=0.5)
c.plot_matplotlib()