import pandas

datums = pandas.date_range("20220101", periods=6)

for datum in datums:
     print(datum.date())