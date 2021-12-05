import pandas as pd
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import statistics as stat
import random

main_data = input("please enter the main data on which you need to apply the z test")
column_name = input("please enter the column name of your data")

df = pd.read_csv(main_data)
column_list = df[column_name].tolist()


def randon_set_of_mean(sample_size):
    data_set = []
    for i in range(0, sample_size):
        random_index = random.randint(0, len(column_list)-1)
        value = column_list[random_index]
        data_set.append(value)

    mean = stat.mean(data_set)
    return(mean)


def setup():
    mean_list = []
    for i in range(0, 1000):
        mean = randon_set_of_mean(100)
        mean_list.append(mean)
    
    sampling_mean = stat.mean(mean_list)
    print("mean for the sample data is ", sampling_mean)

    stdev_sampling_data = stat.stdev(mean_list)
    print("stdev for the sample data is ", stdev_sampling_data)

    first_std_start, first_std_end = sampling_mean - stdev_sampling_data, sampling_mean + stdev_sampling_data
    second_std_start, second_std_end = sampling_mean - (stdev_sampling_data*2), sampling_mean + (stdev_sampling_data*2)
    third_std_start, third_std_end = sampling_mean - (stdev_sampling_data*3), sampling_mean + (stdev_sampling_data*3)



    # finding mean of first intervention data (students who got tab with study material)
    intervention1_data = input("please enter the data for intervention1")

    intervention1 = pd.read_csv(intervention1_data)
    intervention1_list = intervention1[column_name].tolist()
    sample1_mean = stat.mean(intervention1_list)
    print("z test score for intervention 1 is ", (sample1_mean - sampling_mean)/ stdev_sampling_data)



    # finding mean of second intervention data (students who got extra classes)
    intervention2_data = input("please enter the data for intervention2")

    intervention2 = pd.read_csv(intervention2_data)
    intervention2_list = intervention2[column_name].tolist()
    sample2_mean = stat.mean(intervention2_list)
    print("z test score for intervention 2 is ", (sample2_mean - sampling_mean)/ stdev_sampling_data)



    # finding mean of third intervention data (students who got fun sheets)
    intervention3_data = input("please enter the data for intervention3")

    intervention3 = pd.read_csv(intervention3_data)
    intervention3_list = intervention3[column_name].tolist()
    sample3_mean = stat.mean(intervention3_list)
    print("z test score for intervention 3 is ", (sample3_mean - sampling_mean)/ stdev_sampling_data)


    graph = pff.create_distplot([mean_list], ["average"], show_hist=False)

    graph.add_trace(pgo.Scatter(x = [sampling_mean, sampling_mean], y = [0, 2], mode="lines", name="mean"))

    graph.add_trace(pgo.Scatter(x = [first_std_start, first_std_start], y = [0, 2], mode="lines", name="sampling_first_start"))
    graph.add_trace(pgo.Scatter(x = [first_std_end, first_std_end], y = [0, 2], mode="lines", name="sampling_first_end"))
    
    graph.add_trace(pgo.Scatter(x = [second_std_start, second_std_start], y = [0, 2], mode="lines", name="sampling_second_start"))
    graph.add_trace(pgo.Scatter(x = [second_std_end, second_std_end], y = [0, 2], mode="lines", name="sampling_second_end"))

    graph.add_trace(pgo.Scatter(x = [third_std_start, third_std_start], y = [0, 2], mode="lines", name="sampling_third_start"))
    graph.add_trace(pgo.Scatter(x = [third_std_end, third_std_end], y = [0, 2], mode="lines", name="sampling_third_end"))

    graph.add_trace(pgo.Scatter(x = [sample1_mean, sample1_mean], y = [0, 2], mode="lines", name="sample1_mean"))

    graph.add_trace(pgo.Scatter(x = [sample2_mean, sample2_mean], y = [0, 2], mode="lines", name="sample2_mean"))

    graph.add_trace(pgo.Scatter(x = [sample3_mean, sample3_mean], y = [0, 2], mode="lines", name="sample3_mean"))

    """ graph.show() """

setup()

""" standard dev = std of population / sqrt(sampling size) """

