import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.bend_euler180(angle=180, p=0.5, with_arc_floorplan=True, direction='ccw', with_bbox=True, cross_section='strip')
c.plot_matplotlib()