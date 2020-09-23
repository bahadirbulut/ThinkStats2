import thinkstats2
import thinkplot

hist = thinkstats2.Hist([1, 2, 2, 3, 5])
# print(hist)

thinkplot.Hist(hist)
thinkplot.Show(xlabel='value', ylabel='frequency')
