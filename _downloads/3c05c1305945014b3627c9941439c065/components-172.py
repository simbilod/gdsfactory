import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.snspd(wire_width=0.2, wire_pitch=0.6, size=[10, 8], turn_ratio=4, terminals_same_side=False, layer=[1, 0])
c.plot_matplotlib()