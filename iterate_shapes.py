import os


def iterate_shapes():
    # TODO: variable names are a little convoluted
    #  make it more clear what is going on here.
    relative_path = os.path.dirname(__file__)
    data_path = os.path.join(relative_path, "data")
    shape_path = os.path.join(data_path, "shapes")
    report_path = os.path.join(data_path, "reports")
    if not os.path.exists(report_path):
        os.makedirs(report_path)
    summary_file = os.path.join(data_path, "summary.txt")

    # Recursively check whole directory?
    # for (dirpath, dirnames, filenames) in os.walk(shape_path):
    #    file_list.extend(filenames)
    #    break
    file_list = []
    for file in os.listdir(shape_path):
        if file.endswith(".shp"):
            shape_file = os.path.join(shape_path, file)
            print(os.path.join(shape_path, file))
            file_list.extend(file)

            # create report file for each shape file
            report_file = os.path.join(report_path, file + '.txt')
            report = open(report_file, 'w+')
            file_size = os.stat(shape_file).st_size # refer to actual shapefile here

            #len(df.index)

            summary_data = "file name: " + file + "\n" + "file size: " + str(file_size) + " bytes" + "\n"
            report.write(summary_data)

            # create shape file entry in master summary file
            summary = open(summary_file, 'a+')
            summary.write("%s\n" % file)

    print(file_list)

    return file_list

# From The Documentation:
# Do not use os.linesep as a line terminator when writing files opened in text mode
# (the default); use a single '\n' instead, on all platforms.
