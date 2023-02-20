import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.ramp(length=10.0, width1=5.0, width2=8.0, layer='WG')
c.plot_matplotlib()