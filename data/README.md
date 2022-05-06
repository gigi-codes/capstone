# ![](images/barti.png) Model Transit Ridership as Fuel Prices Fluctuate

![](images/barti.png) ![](images/bart.png)

---
DATA
---
I will look at ridership on 

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


### <b>Data:</b> <a href = 'https://data.ca.gov/dataset/california-gasoline-data-facts-and-statistics' > CA Gas Data, Facts, and Statistics </a>
* 


https://data.ca.gov/dataset/time-walk-bike-to-work
https://data.ca.gov/dataset/annual-miles-traveled
https://data.ca.gov/dataset/california-air-resources-board-gis-datasets
https://data.ca.gov/dataset/transportation-to-work
https://data.ca.gov/dataset/driver-licenses-outstanding-by-county/resource/0abef7f0-285f-4887-9b4e-69e86d89ceb1
https://data.ca.gov/dataset/vehicle-fuel-type-count-by-zip-code




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