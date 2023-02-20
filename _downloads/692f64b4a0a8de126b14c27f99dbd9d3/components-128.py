import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.mzi_arms(delta_length=10.0, length_y=0.8, length_x=0.1, with_splitter=True, delta_yright=0)
c.plot_matplotlib()