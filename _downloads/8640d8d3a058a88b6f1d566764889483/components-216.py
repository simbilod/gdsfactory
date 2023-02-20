import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.terminator(length=50, cross_section_input='strip', tapered_width=0.2, doping_layers=['NPP'])
c.plot_matplotlib()