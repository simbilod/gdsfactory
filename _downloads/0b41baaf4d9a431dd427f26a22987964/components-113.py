import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.loop_mirror(bend90='bend_euler')
c.plot_matplotlib()