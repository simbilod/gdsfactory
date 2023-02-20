import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.straight_pin_slot(length=500.0, via_stack_width=10.0, via_stack_spacing=3.0, via_stack_slab_spacing=2.0)
c.plot_matplotlib()