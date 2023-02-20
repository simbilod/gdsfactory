import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coh_rx_dual_pol(cross_section='strip', lo_splitter='mmi1x2', single_pol_rx_spacing=50.0, splitter_coh_rx_spacing=40.0)
c.plot_matplotlib()