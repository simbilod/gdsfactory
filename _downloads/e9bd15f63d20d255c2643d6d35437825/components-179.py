import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.spiral_racetrack_heater_metal(straight_length=30, spacing=2, num=8, waveguide_cross_section='strip', heater_cross_section='heater_metal')
c.plot_matplotlib()