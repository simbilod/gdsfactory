import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coupler_full(coupling_length=40.0, dx=10.0, dy=5.0, gap=0.5, dw=0.1, cross_section='strip')
c.plot_matplotlib()