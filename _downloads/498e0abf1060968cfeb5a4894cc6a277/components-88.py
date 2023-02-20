import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.grating_coupler_array(pitch=127.0, n=6, port_name='o1', rotation=0)
c.plot_matplotlib()