import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.mzi_phase_shifter(delta_length=10.0, length_y=2.0, length_x=200, straight_x_top='straight_heater_metal', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', nbends=2, cross_section='strip')
c.plot_matplotlib()