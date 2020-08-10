import os


class PathClass:
    # -Folders-
    relative_path = os.path.dirname(__file__)
    debug_path = os.path.join(relative_path, "debug")
    data_path = os.path.join(relative_path, "data")
    shape_path = os.path.join(data_path, "shapes")
    covid_path = os.path.join(data_path, "covid")
    merge_path = os.path.join(data_path, "merge")

    # -Files-
    # TODO: don't like this at all. How to declare a blank path?
    no_file = os.path.join(data_path, "blank.csv")
    election_results = no_file
    glue_file = no_file
    political_file = no_file
    covid_political_file = no_file
    debug_file = no_file

    state_shapefile = no_file
    county_shapefile = no_file
    state_covid_cases_file = no_file
    state_covid_deaths_file = no_file
    county_covid_cases_file = no_file
    county_covid_deaths_file = no_file

    def __init__(self, detail_level):
        #nonlocal relative_path, merge_path, data_path, debug_path, shape_path, covid_path
        #nonlocal election_results, glue_file, political_file, covid_political_file, debug_file, state_shapefile, county_shapefile, state_covid_cases_file, state_covid_deaths_file, county_covid_cases_file, county_covid_deaths_file
        PathClass.election_results = os.path.join(PathClass.merge_path, detail_level + "_results.csv")
        PathClass.glue_file = os.path.join(PathClass.merge_path, detail_level + "_glue.csv")
        PathClass.political_file = os.path.join(PathClass.data_path, detail_level + "_political.csv")
        PathClass.covid_political_file = os.path.join(PathClass.data_path, detail_level + "_covid_political.csv")
        PathClass.debug_file = os.path.join(PathClass.debug_path, detail_level + "_merge_debug_data.csv")

        PathClass.state_shapefile = os.path.join(PathClass.shape_path, "s_11au16.shp")
        PathClass.county_shapefile = os.path.join(PathClass.shape_path, "tl_2019_us_county.shp")
        PathClass.state_covid_cases_file = os.path.join(PathClass.covid_path, "COVID-19-Cases-USA-By-State.csv")
        PathClass.state_covid_deaths_file = os.path.join(PathClass.covid_path, "COVID-19-Deaths-USA-By-State.csv")
        PathClass.county_covid_cases_file = os.path.join(PathClass.covid_path, "COVID-19-Cases-USA-By-County.csv")
        PathClass.county_covid_deaths_file = os.path.join(PathClass.covid_path, "COVID-19-Deaths-USA-By-County.csv")
        return
