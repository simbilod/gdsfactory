import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.edge_coupler_array(n=5, pitch=127.0, x_reflection=False, text_offset=[10, 20])
c.plot_matplotlib()