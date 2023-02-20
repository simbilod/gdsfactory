import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_heater_meander(length=300.0, spacing=2.0, cross_section='strip', heater_width=2.5, extension_length=15.0, layer_heater='HEATER', radius=5.0, via_stack='via_stack_heater_mtop', port_orientation1=180, port_orientation2=0, heater_taper_length=10.0, straight_widths=[0.8, 0.9, 0.8], taper_length=10)
c.plot_matplotlib()