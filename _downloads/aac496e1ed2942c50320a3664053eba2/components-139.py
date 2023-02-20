import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.optimal_hairpin(width=0.2, pitch=0.6, length=10, turn_ratio=4, num_pts=50, layer=[1, 0])
c.plot_matplotlib()