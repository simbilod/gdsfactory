import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.via1(size=[0.7, 0.7], spacing=[2.0, 2.0], enclosure=2, layer='VIA1', bbox_offset=0)
c.plot_matplotlib()