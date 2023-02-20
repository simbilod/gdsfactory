import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ring_single_dut(gap=0.2, length_x=4, length_y=0, radius=5.0, with_component=True, port_name='o1')
c.plot_matplotlib()