import pandas as pd
import numpy as np
data = pd.read_csv('medallero_Panamericanos_Lima2019.csv')


def cal_sum():
    print("Sum of gold medals: ", data['Oro'].sum())


def cal_num_elements():
    print("Number of elements: ", data['Oro'].count())


def cal_mean():
    print("Average of gold medals: ", data.Oro.mean())


def cal_mean_round():
    print("Average of gold medals: ", round(data.Oro.mean(), 2))


def cal_median():
    pos_median = round(np.size(data.Oro) / 2)
    print("Data median: ", data.Oro[pos_median - 1])


def cal_mode():
    print("Mode: ", data.Oro.mode())


def cal_percentile(per):
    num = np.percentile(data.Oro, per)
    print("Per(", per, "%): ", num)


def cal_var():
    print("Variance: ", data.Oro.var())


if __name__ == '__main__':
    print(data.Oro)
    for i in range(0, 110, 10):
        cal_percentile(i)

