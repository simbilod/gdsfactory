import gdsfactory as gf
c = gf.Component("demo")

mmi = gf.components.mmi2x2(width_mmi=10, gap_mmi=3)
mmi1 = c << mmi
mmi2 = c << mmi

mmi2.move((100, 30))
mmi2.rotate(30)

routes = gf.routing.get_bundle_all_angle(
    mmi1.get_ports_list(orientation=0),
    [mmi2.ports["o2"], mmi2.ports["o1"]],
    connector=None,
)
for route in routes:
    c.add(route.references)
c.plot()