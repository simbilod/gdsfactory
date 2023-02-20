import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_bend(radius=10.0, coupler_gap=0.2, coupling_angle_coverage=120.0, cross_section_inner='strip', cross_section_outer='strip')
c.plot_matplotlib()