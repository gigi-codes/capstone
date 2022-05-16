# Model Transit Ridership as Fuel Prices Fluctuate

![](images/barti.png)

---
SUMMARY
---
I sought to model ridership in general, and with a few additional regressors. Various models using Facebook's _Prophet_ and Linkedin's _Greykite_ frameworks produced good results for modelling data prior to early-COVID-pandemic-shutdowns, but they and _ARIMA_ models failed to capture the percipitous monthly riderhip drop, and exceedingly low rise.

I included average _fuel price_, increased number of _registere cars_ as well as _consumer debt_ as additional regressors in both _Prophet_ and _Greykite_, but there was no significant effect at that resolution. 

Sourcing local data - at the ZIP-code or even county level, would likely yiedl better results. 

--- 
## DATA
---

Data was sourced via various sources, through API requests and extracting from spreadsheets obtained directly from state sources. Details can be found in the [data](/data/) directory README. 

---

## Background 
* How elastic/inelastic is mass transit ridership as a function of fuel price? 
* Can fuel prices be a tool use to increase ridership? 
---

## _Exploratory Data Analyses_ 

<img src =images/barrt.png>
<br>
<img src =images/fuel.png>

### MODELS: 
Model performance visualized below

<img src =images/arima.png>

_ARIMA model over gridsearch yielded (4,1,4) model._

<img src=images/greykite.png>

_Greykite model with extra regressors performed best on data prior to COVID_

<img src=images/prophet.png>

_PROPHET model poorly predicted downward trend even prior to COVID decrease_

--- 
## Conclusion: 
Although _Prophet_ and _Greykite_ are extremely powerful and flexible, tried-and-true _ARIMA_ produced the best model for forecasting rideship, both for data inclusive of COVID shutdowns and without. As a true time-series model, the changes were better captured. _Prophet_ and _Greykite_ are built as standard linear regerssors parameters and coefficients to model holidays, seasons, weekends, etc. - the limitations of monthly data also negate the power and flexibility of frameworks designed to model just that. 
> <b>Further Work:</b> source data elsewhere, as non-official venues may have finer granularity. With finer temporal and spatial granularity, a robust and powerful model is possible. .