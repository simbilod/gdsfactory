import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.resistance_meander(pad_size=[50.0, 50.0], num_squares=1000, width=1.0, res_layer='MTOP', pad_layer='MTOP', gnd_layer='MTOP')
c.plot_matplotlib()