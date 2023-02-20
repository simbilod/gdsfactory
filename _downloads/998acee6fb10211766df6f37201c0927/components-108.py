import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.interdigital_capacitor(fingers=4, finger_length=20.0, finger_gap=2.0, thickness=5.0, layer='WG')
c.plot_matplotlib()