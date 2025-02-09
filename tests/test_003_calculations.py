import test_001_to_from as ttf


def test_within_extent():
    dino_gw = ttf.test_obscollection_dinozip_gw()
    extent = [210350, 213300, 473300, 474000]
    dino_gw.geo.within_extent(extent, inplace=True)
    assert dino_gw.shape[0] == 4
    return dino_gw


# %% stats


def test_obscollection_consecutive_obs_years():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    coy = gw.stats.consecutive_obs_years()
    return coy


def test_obscollection_get_number_of_obs():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    coy = gw.stats.get_no_of_observations()
    return coy


def test_obscollection_get_first_last_obs_date():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    fl_obs_date = gw.stats.get_first_last_obs_date()
    return fl_obs_date


def test_obscollection_get_seasonal_stats():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    st = gw.stats.get_seasonal_stat(stat="mean")
    return st


def test_obscollection_get_min():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    omin = gw.stats.get_min()
    return omin


def test_obscollection_get_max():
    gw = ttf.test_obscollection_dinozip_gw_keep_all_obs()
    omax = gw.stats.get_max()
    return omax


# %% geo


def test_get_nearest_point():
    # check two of the same observation collections
    # every point must find itself as the nearest point
    dino_gw = ttf.test_obscollection_dinozip_gw()
    fl = ttf.test_obscollection_dinozip_wl()
    dino_gw[
        ["nearest point", "distance nearest point"]
    ] = dino_gw.geo.get_nearest_point(fl)
    return dino_gw


def test_get_nearest_polygon():
    import geopandas as gpd
    from shapely.geometry import Polygon

    # check two of the same observation collections
    # every point must find itself as the nearest point
    dino_gw = ttf.test_obscollection_dinozip_gw()
    extent = dino_gw.geo.get_extent()
    polygon1 = Polygon(
        (
            (extent[0], extent[2]),
            (extent[0], extent[3]),
            (extent[1], extent[3]),
            (extent[1], extent[2]),
            (extent[0], extent[2]),
        )
    )
    polygon2 = Polygon(
        (
            (-extent[0], -extent[2]),
            (-extent[0], -extent[3]),
            (-extent[1], -extent[3]),
            (-extent[1], -extent[2]),
            (-extent[0], -extent[2]),
        )
    )
    gdf = gpd.GeoDataFrame({"name": [1, 2], "geometry": [polygon1, polygon2]})

    dino_gw[
        ["nearest polygon", "distance nearest polygon"]
    ] = dino_gw.geo.get_nearest_polygon(gdf)
    assert (dino_gw["nearest polygon"] == 0.0).all()
    assert (dino_gw["distance nearest polygon"] == 0.0).all()

    return dino_gw[["nearest polygon", "distance nearest polygon"]]


def test_get_ground_level_oc():
    try:
        from art_tools import hpd_extension

        gw = ttf.test_obscollection_fews_lowmemory()
        zp = gw.art.geo_get_ground_level()
        return zp
    except ModuleNotFoundError as e:
        print(e)
    return


def test_get_ground_level_gwobs():
    try:
        from art_tools import hpd_extension

        gw = ttf.test_observation_gw()
        mv = gw.art.geo_get_ground_level()
        return mv
    except ModuleNotFoundError as e:
        print(e)
        return
