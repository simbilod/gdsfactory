import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.via_stack_with_offset(layers=['PPP', 'M1'], sizes=[[10, 10], [10, 10]], port_orientation=180)
c.plot_matplotlib()