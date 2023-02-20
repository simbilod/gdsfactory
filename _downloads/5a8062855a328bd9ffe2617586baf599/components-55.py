import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.crossing_arm(r1=3.0, r2=1.1, w=1.2, L=3.4, layer_slab='SLAB150', cross_section='strip')
c.plot_matplotlib()