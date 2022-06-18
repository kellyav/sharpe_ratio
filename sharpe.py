{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red7\green19\blue34;
}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c99971\c0;\cssrgb\c2138\c10019\c17854;
}
\margl1440\margr1440\vieww12840\viewh11860\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf2 \cb3 ## 1. Sharpe ratio study\
<p>An investment may make sense if we expect it to return more money than it costs. But returns are only part of the story because they are risky - there may be a range of possible outcomes. How does one compare different investments that may deliver similar results on average, but exhibit different levels of risks?</p>\
\
<p>The <a href="https://web.stanford.edu/~wfsharpe/art/sr/sr.htm"><em>reward-to-variability ratio</em></a> was developed in 1966, and soon came to be called the Sharpe Ratio. It compares the expected returns for two investment opportunities and calculates the additional return per unit of risk an investor could obtain by choosing one over the other. In particular, it looks at the difference in returns for two investments and compares the average difference to the standard deviation (as a measure of risk) of this difference. A higher Sharpe ratio means that the reward will be higher for a given amount of risk. It is common to compare a specific opportunity against a benchmark that represents an entire category of investments.</p>\
<p>The Sharpe ratio has been one of the most popular risk/return measures in finance, not least because it's so simple to use. It also helped that Professor Sharpe won a Nobel Memorial Prize in Economics in 1990 for his work on the capital asset pricing model (CAPM).</p>\
<p>The Sharpe ratio is usually calculated for a portfolio and uses the risk-free interest rate as benchmark. We will simplify our example and use stocks for \cb3 Facebook and Amazon \cb3 instead of a portfolio. We will also use a stock index as benchmark rather than the risk-free interest rate because both are readily available at daily frequencies and we do not have to get into converting interest rates from annual to daily frequency. Just keep in mind that you would run the same calculation with portfolio returns and your risk-free rate of choice, e.g, the <a href="https://fred.stlouisfed.org/series/TB3MS">3-month Treasury Bill Rate</a>. </p>\
<p>As a benchmark, we'll use the S&amp;P 500 that measures the performance of the 500 largest stocks in the US. When we use a stock index instead of the risk-free rate, the result is called the Information Ratio and is used to benchmark the return on active portfolio management because it tells you how much more return for a given unit of risk your portfolio manager earned relative to just putting your money into a low-cost index fund.</p>\
\
\
\
# Importing required modules\
import pandas as pd\
import numpy as np\
import matplotlib.pyplot as plt\
\
# Settings to produce nice plots in a Jupyter notebook\
plt.style.use('fivethirtyeight')\
%matplotlib inline\
\
# Reading in the data\
stock_data= pd.read_csv('datasets/stock_data.csv', \
                        parse_dates=['Date'], index_col=['Date']).dropna()\
benchmark_data= pd.read_csv('datasets/benchmark_data.csv', \
                            parse_dates=['Date'], index_col=['Date']).dropna()\
\
\
#stock_data.dropna()\
#benchmark_data.dropna()\
\
\
\
# Display summary for stock_data\
print('Stocks\\n')\
stock_data.info()\
print(stock_data.head())\
\
# Display summary for benchmark_data\
print('\\nBenchmarks\\n')\
benchmark_data.info()\
benchmark_data.info()\
print(benchmark_data.head())\
\
# summarize daily prices for Amazon and Facebook\
stock_data.plot(subplots=True, title='Stock Data')\
stock_data.describe()\
\
\
#  plot the \cb3 daily values for the S&P 500 \cb3 \
benchmark_data.plot(title='S&P 500')\
\
# summarized:\
benchmark_data.describe()\
\
\
#The inputs for the Sharpe Ratio: Starting with Daily Stock Returns\
<p>The Sharpe Ratio uses the difference in returns between the two investment opportunities under consideration.</p>\
<p>However, our data show the historical value of each investment, not the return. To calculate the return, we need to calculate the percentage change in value from one day to the next. We'll also take a look at the summary statistics because these will become our inputs as we calculate the Sharpe Ratio. \
\
\
# calculate daily stock_data returns\
stock_returns = stock_data.pct_change()\
\
stock_returns.plot() # plot the daily returns\
stock_returns.describe() # summarize the daily returns\
\
#  Daily S&P 500 returns\
sp_returns = benchmark_data['S&P 500'].pct_change()\
sp_returns.plot() # plot the daily returns\
sp_returns.describe() # summarize the daily returns\
\
\
#Calculating Excess Returns for Amazon and Facebook vs. S&P 500\
<p>Next, we need to calculate the relative performance of stocks vs. the S&amp;P 500 benchmark. This is calculated as the difference in returns between <code>stock_returns</code> and <code>sp_returns</code> for each day.</p>\
\
\
## calculate the difference in daily returns\
excess_returns = stock_returns.sub(sp_returns, axis=0)\
excess_returns.plot() # plot the excess_returns\
excess_returns.describe()# summarize the excess_returns\
\
\
# The Sharpe Ratio, Step 1: The Average Difference in Daily Returns Stocks vs S&P 500\
<p>Now we can finally start computing the Sharpe Ratio. First we need to calculate the average of the <code>excess_returns</code>. This tells us how much more or less the investment yields per day compared to the benchmark.</p>\
\
# calculate the mean of excess_returns \
avg_excess_return = excess_returns.mean()\
\
# plot avg_excess_returns\
avg_excess_return.plot.bar(title='mean of the return difference')\
\
\
The Sharpe Ratio, Step 2: Standard Deviation of the Return Difference\
<p>It looks like there was quite a bit of a difference between average daily returns for Amazon and Facebook.</p>\
<p>Next, we calculate the standard deviation of the <code>excess_returns</code>. This shows us the amount of risk an investment in the stocks implies as compared to an investment in the S&amp;P 500.</p>\
\
\
# calculate the standard deviations\
sd_excess_return = excess_returns.std()\
\
# plot the standard deviations\
sd_excess_return.plot.bar(title='Standard Deviation of the Return Difference')\
\
\
\
compute the ratio of <code>avg_excess_returns</code> and <code>sd_excess_returns</code>. The result is now finally the <em>Sharpe ratio</em> and indicates how much more (or less) return the investment opportunity under consideration yields per unit of risk.</p>\
<p>The Sharpe Ratio is often <em>annualized</em> by multiplying it by the square root of the number of periods. We have used daily data as input, so we'll use the square root of the number of trading days (5 days, 52 weeks, minus a few holidays): \uc0\u8730 252</p>\
\
\
# calculate the daily sharpe ratio\
daily_sharpe_ratio = avg_excess_return.div(sd_excess_return)\
\
# annualize the sharpe ratio\
annual_factor = 
\fs28 \cb3 \expnd0\expndtw0\kerning0
np.sqrt(252)
\fs24 \cb3 \kerning1\expnd0\expndtw0 \
annual_sharpe_ratio = 
\fs28 \cb3 \expnd0\expndtw0\kerning0
daily_sharpe_ratio.mul(annual_factor)
\fs24 \cb3 \kerning1\expnd0\expndtw0 \
\
# plot the annualized sharpe ratio\
\pard\pardeftab720\partightenfactor0

\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
annual_sharpe_ratio.plot.bar(title='Annualized Sharpe Ratio: Stocks vs S&P 500\'92)\
\
\
}