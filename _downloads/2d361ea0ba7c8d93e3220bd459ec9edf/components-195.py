import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_pn(length=2000, via_stack_width=10.0, via_stack_spacing=2)
c.plot_matplotlib()