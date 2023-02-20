import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.dicing_lane(size=[50, 300], layer_dicing='DICING')
c.plot_matplotlib()