import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ring_double_pn(add_gap=0.3, drop_gap=0.3, radius=5.0, doping_angle=85, doped_heater=True, doped_heater_angle_buffer=10, doped_heater_layer='NPP', doped_heater_width=0.5, doped_heater_waveguide_offset=2.175)
c.plot_matplotlib()