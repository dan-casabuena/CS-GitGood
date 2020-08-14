# CS:Git_Good: How to Get More Kills in CS:GO?
## Analysing basic professional level CS:GO statistics

**Have you ever wondered how people have such *HIGH* Kill/Death ratios in professional CS:GO matches?**

No? Well don't fret, because I'm still going to show my findings to you anyways.

**Language**: Python

**Libraries Used**: Selenium, BeautifulSoup, pandas, numpy, scikitlearn, statsmodels

## A Little backstory:
One day I decided to hop on CS:GO and play a couple competitive matches with my friends, to eventually lose all 5 games that we've played. I was so distraught as to why things happened this way, and I wanted to figure out a way that I could improve my CS:GO skills. Until this day, I am still pretty trash, but I have found some interesting data that shows some inconsistencies in my mental game.

And so the quest for knowledge began.

I decided to create a small little web scraper using the python libraries selenium and beautifulsoup to grab *professional* CS:GO player statistics on the [ESL ProGaming Website](https://pro.eslgaming.com/csgo/proleague/statistics/). Unfortunately, the only available data of each player listed on the website were *Kill/Death Ratios*, *Headshot Ratios*, *Average **Distance** of each kill*, and *Number of Aces*. As for other websites, webscraping was not allowed, so the ESL ProGaming website had to do for now.

## Sample Info:
Sample scraped from the [ESL ProGaming Website](https://pro.eslgaming.com/csgo/proleague/statistics/), which holds data of **137** Professional CS:GO players during the "ESL Pro League CS:GO Season 11". "Statistics are based on ESL events last 12 months" (As of 2020-08-13).

## Results:

**Plots for each variable recorded:**
![Aces vs KD Ratio](https://photos.app.goo.gl/KAFgs8QDe8qCmNyK7)

###### Regression Results for Headshot vs KD Ratio
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.064
Model:                            OLS   Adj. R-squared:                  0.057
Method:                 Least Squares   F-statistic:                     9.212
Date:                Thu, 13 Aug 2020   Prob (F-statistic):            0.00289
Time:                        22:18:23   Log-Likelihood:                 87.970
No. Observations:                 137   AIC:                            -171.9
Df Residuals:                     135   BIC:                            -166.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          1.2033      0.058     20.781      0.000       1.089       1.318
x1            -0.3725      0.123     -3.035      0.003      -0.615      -0.130
==============================================================================
Omnibus:                        0.929   Durbin-Watson:                   2.312
Prob(Omnibus):                  0.628   Jarque-Bera (JB):                0.668
Skew:                           0.165   Prob(JB):                        0.716
Kurtosis:                       3.091   Cond. No.                         13.6
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
```
###### Regression Results for Average Distance per Kill vs KD Ratio
```
OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.197
Model:                            OLS   Adj. R-squared:                  0.191
Method:                 Least Squares   F-statistic:                     33.10
Date:                Thu, 13 Aug 2020   Prob (F-statistic):           5.61e-08
Time:                        22:23:19   Log-Likelihood:                 98.468
No. Observations:                 137   AIC:                            -192.9
Df Residuals:                     135   BIC:                            -187.1
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.4738      0.097      4.867      0.000       0.281       0.666
x1             0.0008      0.000      5.753      0.000       0.001       0.001
==============================================================================
Omnibus:                        0.295   Durbin-Watson:                   2.304
Prob(Omnibus):                  0.863   Jarque-Bera (JB):                0.269
Skew:                           0.105   Prob(JB):                        0.874
Kurtosis:                       2.945   Cond. No.                     6.79e+03
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 6.79e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
```

###### **PLEASE NOTE: THIS IS A SIDE PROJECT; IT IS NOT 100% COMPLETE AND MAY INCLUDE ERRORS THAT I MAY HAVE NOT FORSEEN. PAY ATTENTION AND READ *AT YOUR OWN RISK*.**