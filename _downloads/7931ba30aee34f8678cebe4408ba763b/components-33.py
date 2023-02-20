import gdsfactory as gf

PDK = gf.get_generic_pdk()
PDK.activate()
c = gf.components.coh_tx_dual_pol(splitter='mmi1x2', spol_coh_tx='coh_tx_single_pol', yspacing=10.0, xspacing=40.0, cross_section='strip')
c.plot_matplotlib()