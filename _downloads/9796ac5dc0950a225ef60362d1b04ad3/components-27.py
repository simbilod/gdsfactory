import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.cavity(coupler='coupler', length=0.1, gap=0.2)
c.plot_matplotlib()