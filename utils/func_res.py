def sinuosity(geom):
    assert geom.geom_type == "LineString" or geom.geom_type == "MultiLineString", geom.geom_type
    length = geom.length
    start_pt = geom.interpolate(0)
    end_pt = geom.interpolate(1, normalized=True)
    straight_dist = start_pt.distance(end_pt)
    if straight_dist == 0.0:
        if length == 0.0:
            return 0.0
        return float("inf")
    return length / straight_dist

