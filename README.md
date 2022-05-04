# ![](images/barti.png) Model Transit Ridership as Fuel Prices Fluctuate

![](images/barti.png) ![](images/bart.png)

---
SUMMARY
---
I will look at ridership on 

* bart
* ~~caltrain~~ upon further exploration, Caltrain's ridership metric is a strictly yearly-counted number, with no sampling on daily, weekly or even monthly. Project will only consider BART data. 


to model increase or decrease as a function of fuel prices. If given time, I will look at 
* other systems: LIRR
* model 

I want to focus on the information of on and off boarding to look at commuter vs intra-city/ 'urban' rides

---

## Background 
* How elastic/inelastic is mass transit ridership as a function of fuel price? 
* Can fuel prices be a tool use to increase ridership? 
* What subsidies does mass transit receive vs. car-travel infrastructure? 

---
## Data Acquisition & Cleaning 
---
### <b>Data:</b> Ridership data 
**Description:** Ridership reports from the BART reporting agency website daing to 2009. 


 Source  | File  | Report Date  | Shape | 
 ---     | ---   |  ---         |  ---  |
 <a href = link > BART </a> |  <a href =  link > Data (xlsx) </a> | April 2013 | (1500,49) |
 <a href = link > Caltrain </a> |  <a href =  link > Data (xlsx) </a> | April 2013 | (1500,49) |

<br>

### <b>Data:</b> <a href = '' > Fuel from EIA </a>
**Description:** The fuel stats is collected by federal fuel agency

<!-- 
year(s) | name/link     | description                  | size 
---     | ---           | ---                          | ---
2012    |   xxx         |  business by type in county  | row x col 
2012    |   xxx         |  business counts by zip      | row x col  -->


name        | description 
---         | --- 
avg         | zip

### Data: _Model Features_

<br >

variable name   | type      | description 
---             | ---       | ---   
riders         | numeric   | count, modelled
riders         | numeric   | count, faregate info
fuel price      | weekly average    | city
fuel price      | monthly average    | zip 

---

## _Target_

I trained multiple estimators to model the outcomes reported in the _CalEnviroScreen_ reports to build upon that work: 

variable name   | type      | description 
---             | ---       | ---   
ridership         | fuelprice   | increase/decrease

---

## _Exploratory Data Analyses_ 

* a summary

<!-- <img src = filepathnoquotes ><br>
_a caption._ -->
