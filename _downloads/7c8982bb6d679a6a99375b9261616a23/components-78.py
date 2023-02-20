import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.disk_heater(radius=10.0, gap=0.2, wrap_angle_deg=180.0, parity=1, cross_section='strip', heater_layer='HEATER', via_stack='via_stack_heater_mtop', heater_width=5.0, heater_extent=2.0, via_width=10.0, port_orientation=90)
c.plot_matplotlib()