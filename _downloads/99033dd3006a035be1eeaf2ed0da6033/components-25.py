import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.bend_straight_bend(straight_length=10.0, angle=90, p=0.5, with_arc_floorplan=True, npoints=720, direction='ccw')
c.plot_matplotlib()