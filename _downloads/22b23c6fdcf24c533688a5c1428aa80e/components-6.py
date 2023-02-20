import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.add_grating_couplers(layer_label=[200, 0], gc_port_name='o1')
c.plot_matplotlib()