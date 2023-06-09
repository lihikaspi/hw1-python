import sys
import data
import statistics


def print_stats(dt, subtitle, features, is_all, which_feature):
    """
    prints for first question
    :param dt: database
    :param subtitle: type of data
    :param features: array of relevant keys
    :param is_all: not only one category
    :param which_feature: which key
    :return: none
    """
    print(subtitle + ":")
    statistic_functions = [statistics.calc_mean, statistics.calc_stdv]  # one value statistic functions
    statistic_functions_joint = [statistics.calc_covariance]  # two value statistic function
    database = dt
    if is_all == 0:
        filtered = data.filter_by_feature(dt, features[which_feature], {1})
        database = filtered[0]
    data.print_details(database, features[2:], statistic_functions)
    data.print_joint_details(database, features[3:], statistic_functions_joint, "Cov(t1, cnt)")


def main(argv):
    path = argv[1]
    features = ["season", "is_holiday", "hum", "t1", "cnt"]  # relevant features
    dt = data.load_data(path, features)
    print("Question 1:")
    print_stats(dt, "Summer", features, path, 0, 0)
    print_stats(dt, "Holiday", features, path, 0, 1)
    print_stats(dt, "All", features, path, 1, -1)

    print()
    print("Question 2:")
    winter_only = data.filter_by_feature(dt, "season", {3})
    holiday = data.filter_by_feature(winter_only[0], "is_holiday", {0})
    func = [statistics.calc_mean, statistics.calc_stdv]
    label = ["Winter Holiday records:", "Winter Weekday records:"]
    print("If t1<=13.0, then:")
    statistics.population_statistics(label[0], holiday[1], "t1", "cnt", 13.0, 0, func)
    statistics.population_statistics(label[1], holiday[0], "t1", "cnt", 13.0, 0, func)
    print("If t1>13.0, then:")
    statistics.population_statistics(label[0], holiday[1], "t1", "cnt", 13.0, 1, func)
    statistics.population_statistics(label[1], holiday[0], "t1", "cnt", 13.0, 1, func)
    # double code --> fix


if __name__ == '__main__':
    main(sys.argv)


