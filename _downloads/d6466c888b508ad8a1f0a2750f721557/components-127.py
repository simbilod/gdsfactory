import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.mzi_arm(length_y_left=0.8, length_y_right=0.8, length_x=0.1)
c.plot_matplotlib()