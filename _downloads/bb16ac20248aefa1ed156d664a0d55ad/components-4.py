import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.add_fiducials_offsets(fiducial='cross', offsets=[[0, 100], [0, -100]])
c.plot_matplotlib()