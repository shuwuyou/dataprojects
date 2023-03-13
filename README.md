# Spreadsheet Analysis
A little assignment to practice finding data, munging it, and analyzing it in a spreadsheet program.

Replace the contents of this file with a report, as described in the [instructions](./instructions.md).

## Basic Information
The original source of data set from NYC OpenData. Its title is [NYC Wi-Fi Hotspot Locations](https://data.cityofnewyork.us/City-Government/NYC-Wi-Fi-Hotspot-Locations/yjub-udmw). This data set displays the details of NYC Wi-Fi hotspot locations along with other details. There are 29 columns: "OBJECTID,Borough,Type,Provider,Name,Location,Latitude,Longitude,X,Y,Location_T,Remarks,City,SSID,SourceID,Activated,BoroCode,Borough Name,Neighborhood Tabulation Area Code (NTACODE),Neighborhood Tabulation Area (NTA),Council Distrcit,Postcode,BoroCD,Census Tract,BCTCB2010,BIN,BBL,DOITT_ID,"Location (Lat, Long)"
The original format of this file is in CSV.

The First 20 rows:
| OBJECTID      | Borough        | Type          | Provider                | Name                                                               | Location                                                                          | Latitude      | Longitude                                          | X             | Y                  | Location_T                                   | Remarks                                            | City             | SSID                     | SourceID               | Activated                                | BoroCode | Borough Name  | Neighborhood Tabulation Area Code (NTACODE) | Neighborhood Tabulation Area (NTA)                       | Council Distrcit | Postcode | BoroCD     | Census Tract | BCTCB2010                         | BIN     | BBL        | DOITT_ID | "Location (Lat, Long)"            |
|---------------|----------------|---------------|-------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------|---------------|----------------------------------------------------|---------------|--------------------|----------------------------------------------|----------------------------------------------------|------------------|--------------------------|------------------------|------------------------------------------|----------|---------------|---------------------------------------------|----------------------------------------------------------|------------------|----------|------------|--------------|-----------------------------------|---------|------------|----------|-----------------------------------|
| 10604         | 4              | Limited Free  | SPECTRUM                | Baisley Pond Park                                                  | Park Perimeter                                                                    | 40.6748599999 | -73.7841200005                                     | 1044131.89696 | 185219.892077      | Outdoor TWC Aerial                           | 3 free 10 min sessions                             | Queens           | GuestWiFi                | 0                      | 09/09/9999                               | 4        | Queens        | QN02                                        | Springfield Gardens North                                | 28               | 11434    | 412        | 294          | 294                               | 0       | 0          | 1408     | "(40.6748599999, -73.7841200005)" |
| 10555         | 4              | Limited Free  | SPECTRUM                | Kissena Park                                                       | Park Perimeter                                                                    | 40.7475599996 | -73.8181499997                                     | 1034637.51076 | 211685.217755      | Outdoor TWC Aerial                           | 3 free 10 min sessions                             | Queens           | GuestWiFi                | 0                      | 09/09/9999                               | 4        | Queens        | QN22                                        | Flushing                                                 | 20               | 11355    | 407        | 845          | 845                               | 0       | 0          | 1359     | "(40.7475599996, -73.8181499997)" |
| 12370         | 3              | Free          | Transit Wireless        | Grand St (L)                                                       | Grand St (L)                                                                      | 40.7119259997 | -73.9406699994                                     | 1000698.12752 | 198655.90884       | Subway Station                               | SN 123                                             | Brooklyn         | TransitWirelessWiFi      |                        | 09/09/9999                               | 3        | Brooklyn      | BK90                                        | East Williamsburg                                        | 34               | 11206    | 301        | 495          | 495                               | 0       | 0          | 1699     | "(40.7119259997, -73.9406699994)" |
| 9893          | 3              | Free          | Downtown Brooklyn       |                                                                    | 125 Court St.                                                                     | 40.6899850001 | -73.9919950004                                     | 986469.966349 | 190656.680416      | Outdoor                                      |                                                    | Brooklyn         | Downtown Brooklyn WiFi   |                        | 09/09/9999                               | 3        | Brooklyn      | BK09                                        | Brooklyn Heights-Cobble Hill                             | 33               | 11201    | 302        | 9            | 9                                 | 3388736 | 3002777501 | 298      | "(40.6899850001, -73.9919950004)" |
| 10169         | 1              | Free          | Transit Wireless        | Lexington Av-63 St (F)                                             | Lexington Av-63 St (F)                                                            | 40.7646300002 | -73.9661150001                                     | 993636.552081 | 217853.888161      | Subway Station                               | SN 223                                             | New York         | TransitWirelessWiFi      |                        | 09/09/9999                               | 1        | Manhattan     | MN40                                        | Upper East Side-Carnegie Hill                            | 4                | 10065    | 108        | 120          | 120                               | 0       | 0          | 599      | "(40.7646300002, -73.9661150001)" |
| 10880         | 4              | Limited Free  | SPECTRUM                | Kissena Park                                                       | Park Perimeter                                                                    | 40.7424300003 | -73.8115100003                                     | 1036481.35944 | 209820.088612      | Outdoor TWC Aerial                           | 3 free 10 min sessions                             | Queens           | GuestWiFi                | 0                      | 09/09/9999                               | 4        | Queens        | QN62                                        | Queensboro Hill                                          | 20               | 11355    | 407        | 1215         | 1215                              | 0       | 0          | 1347     | "(40.7424300003, -73.8115100003)" |
| 10953         | 1              | Free          | Harlem                  |                                                                    | Pole 94 - LenWS1N133                                                              | 40.812944     | -73.9416929996                                     | 1000390.02217 | 235459.893303      | Outdoor                                      |                                                    | New York         | Harlem Wi-Fi             |                        | 09/09/9999                               | 1        | Manhattan     | MN03                                        | Central Harlem North-Polo Grounds                        | 9                | 10037    | 110        | 212          | 212                               | 0       | 0          | 787      | "(40.812944, -73.9416929996)"     |
| 11018         | 3              | Free          | BPL                     | Clinton Hill - Brooklyn Public Library                             | 380 WASHINGTON AVENUE                                                             | 40.6873790941 | -73.966030666                                      | 993670.827931 | 189708.997928      | Library                                      |                                                    | Brooklyn         | BPLUNWIRED               |                        | 09/09/9999                               | 3        | Brooklyn      | BK69                                        | Clinton Hill                                             | 35               | 11238    | 302        | 197          | 197                               | 3055495 | 3019450036 | 53       | "(40.6873790941, -73.966030666)"  |
| 12375         | 4              | Free          | Transit Wireless        | Halsey St (L)                                                      | Halsey St (L)                                                                     | 40.6956020001 | -73.9040840004                                     | 1010847.41694 | 192717.578854      | Subway Station                               | SN 129                                             | Brooklyn         | TransitWirelessWiFi      |                        | 09/09/9999                               | 4        | Queens        | QN20                                        | Ridgewood                                                | 34               | 11385    | 405        | 555          | 555                               | 0       | 0          | 1704     | "(40.6956020001, -73.9040840004)" |
| 12607         | 3              | Free          | Transit Wireless        | "Broadway Junction (A,C,J,L,Z)"                                    | "Broadway Junction (A,C,J,L,Z)"                                                   | 40.6783340002 | -73.9053160001                                     | 1010512.58493 | 186425.975295      | Subway Station                               | SN 184                                             | Brooklyn         | TransitWirelessWiFi      |                        | 09/09/9999                               | 3        | Brooklyn      | BK79                                        | Ocean Hill                                               | 37               | 11233    | 316        | 367          | 367                               | 0       | 3015460001 | 1718     | "(40.6783340002, -73.9053160001)" |
| 11726         | 2              | Limited Free  | ALTICEUSA               | Crotona Park                                                       | CROTONA PARK C/O EAST 173RD ST AND FULTON AVE                                     | 40.8406639999 | -73.8983720002                                     | 1012370.03233 | 245570.243161      | Outdoor                                      | 3 free 10 min sessions                             | Bronx            | GuestWiFi                |                        | 09/09/9999                               | 2        | Bronx         | BX01                                        | Claremont-Bathgate                                       | 16               | 10457    | 203        | 167          | 167                               | 0       | 0          | 1285     | "(40.8406639999, -73.8983720002)" |
| 9823          | 1              | Free          | Fiberless               | Governors Island                                                   | Liggett B Food Court                                                              | 40.6903899996 | -74.0199599995                                     | 978714.677069 | 190804.762797      | Outdoor                                      | Free - up to 5 mbs                                 | New York         | Governors Island         | Governors Island Trust | 09/09/9999                               | 1        | Manhattan     | MN99                                        | Governors Island                                         | 1                | 10004    | 101        | 5            | 5                                 | 1086341 | 1000010010 | 4920     | "(40.6903899996, -74.0199599995)" |
| 10915         | 1              | Free          | Harlem                  |                                                                    | pole 51n - 131NWC5th                                                              | 40.81026      | -73.9395100003                                     | 1000994.97568 | 234482.426426      | Outdoor                                      |                                                    | New York         | Harlem Wi-Fi             |                        | 09/09/9999                               | 1        | Manhattan     | MN03                                        | Central Harlem North-Polo Grounds                        | 9                | 10037    | 110        | 208          | 208                               | 0       | 0          | 748      | "(40.81026, -73.9395100003)"      |
| 12084         | 3              | Free          | LinkNYC - Citybridge    | bk-02-126166                                                       | 181 Court Street                                                                  | 40.6879008003 | -73.9931469103                                     | 986150.575255 | 189897.318418      | Outdoor Kiosk                                | "Tablet Internet -phone , Free 1 GB Wi-FI Service" | Brooklyn         | LinkNYC Free Wi-Fi       | LINK-000049            | 01/05/2018                               | 3        | Brooklyn      | BK38                                        | DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum Hill         | 33               | 11201    | 302        | 43           | 43                                | 3002846 | 3002800020 | 3039     | "(40.6879008003, -73.9931469103)" |
| 12080         | 3              | Free          | LinkNYC - Citybridge    | bk-02-126505                                                       | 620 ATLANTIC AVENUE                                                               | 40.6836250004 | -73.9770060002                                     | 990627.361249 | 188340.282818      | Outdoor Kiosk                                | "Tablet Internet -phone , Free 1 GB Wi-FI Service" | Brooklyn         | LinkNYC Free Wi-Fi       | LINK-000044            | 07/25/2017                               | 3        | Brooklyn      | BK37                                        | Park Slope-Gowanus                                       | 35               | 11217    | 302        | 129          | 129                               | 3348849 | 3020017500 | 3035     | "(40.6836250004, -73.9770060002)" |
| 12500         | 5              | Free          | LinkNYC - Citybridge    | si-02-125476                                                       | 19 SEAVIEW AVENUE                                                                 | 40.5909830002 | -74.1007320003                                     | 956273.280351 | 154603.543533      | Outdoor Kiosk                                | "Tablet Internet -phone , Free 1 GB Wi-FI Service" | Staten Island    | LinkNYC Free Wi-Fi       | LINK-001752            | 02/28/2017                               | 5        | Staten Island | SI36                                        | Old Town-Dongan Hills-South Beach                        | 50               | 10304    | 502        | 96           | 96                                | 5048677 | 5033050090 | 3585     | "(40.5909830002, -74.1007320003)" |
| 9932          | 3              | Free          | BPL                     | Saratoga - Brooklyn Public Library                                 | 8 THOMAS S BOYLAND STREET                                                         | 40.6848100477 | -73.915132416                                      | 1007787.51197 | 188782.594926      | Library                                      |                                                    | Brooklyn         | BPLUNWIRED               |                        | 09/09/9999                               | 3        | Brooklyn      | BK79                                        | Ocean Hill                                               | 41               | 11233    | 316        | 373          | 373                               | 3040218 | 3014980035 | 345      | "(40.6848100477, -73.915132416)"  |
| 10191         | 4              | Free          | LinkNYC - Citybridge    | qu-01-145954                                                       | 43-40 NORTHERN BOULEVARD                                                          | 40.7536406401 | -73.9184016594                                     | 1006857.44756 | 213858.819051      | Outdoor Kiosk                                | "Tablet Internet -phone , Free 1 GB Wi-FI Service" | Queens           | LinkNYC Free Wi-Fi       | LINK-020932            | 11/07/2017                               | 4        | Queens        | QN31                                        | Hunters Point-Sunnyside-West Maspeth                     | 26               | 11101    | 401        | 171          | 171                               | 4441943 | 4001430500 | 4639     | "(40.7536406401, -73.9184016594)" |
| 10390         | 3              | Limited Free  | ALTICEUSA               | MARIA HERNANDEZ                                                    | IN PARK BELOW PLAYGROUND AREA SOUTH SIDE                                          | 40.7025399998 | -73.9238159997                                     | 1005373.55518 | 195239.922234      | Outdoor                                      | 3 free 10 min sessions                             | Brooklyn         | GuestWiFi                |                        | 09/09/9999                               | 3        | Brooklyn      | BK77                                        | Bushwick North                                           | 34               | 11237    | 304        | 429          | 429                               | 0       | 3032030001 | 245      | "(40.7025399998, -73.9238159997)" |

This data set has 29 columns, for which many columns are very unnecessary. There are missing values.
So I delete many columns using the code to avoid repetition:
```Python
df = df.drop(df.columns[[1, 8, 9, 12, 13, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28]], axis=1)
```
The column 1 is the Brough, which uses 1-5 to represent Manhattan, Queens, etc. This column is repetitive with column 16--BoroCode. Hence, I delete it to avoid repetition.

The column 8 and 9 are X, Y coordinates of the hotspots. Given the fact that column 6 and 7 are describing the position using latitude and longitude, deleting them can avoid repetition,

Column 12 is the City. However, It is just another version of Borough for which "Manhattan" is replaced by "New York". To avoid repetition, delete it.

Column 13 and 14 are SSID and SourceID, which are also something that are irrelevant to analysis.

Column 15 is Activated, showing the day of activating devices. However, only a small number of devices are correctly labelled. Many of them are labelled as 09/09/9999, which is not meaningful. Since very little information can be drawn from it, I delete it.

Column 18 is Neigborhood Code. Since I have had the Neigborhood Name in column 19. I delete this column to avoid repetition.

Column 20, 22, 23, 25, 26, 27 are IDs that are generated from Borough or Device ID. Since I have already had the Borough and device details, I delete them.

For column 28, it is just the combinition of latitude and longitude. To avoid repetition, I delete.

In order to deal with missing values, I use code to replace the missing value as NaN. 
```Python
df.fillna("NaN", inplace=True)
```

Links to files:
raw_date: https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/data/nyc_hotspot.csv
clean_data: https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/data/clean_data.csv
munge.py: https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/munge.py
spreadsheet: https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/data/clean_data_Shu_Tony.xlsx

## Analysis
### Raw data analysis
I first do the aggregate statistics for the raw data. 
| Aggregate Statistics for Column F--Latitude (2 decimal place) |       |
|---------------------------------------------------------------|-------|
| Maximum Latitude                                              | 40.90 |
| Minimum Latitude                                              | 40.51 |
| Mean Latitude                                                 | 40.74 |
| Median Latitude                                               | 40.75 |
| The range of Latitude                                         | 0.39  |
| The range of Latitude in kilometer                            | 43.76 |

| Aggregate Statistics for Column G--Longitude (2 decimal place) |        |
|----------------------------------------------------------------|--------|
| Maximum Longitude                                              | -73.71 |
| Minimum Longitude                                              | -74.24 |
| Mean Longitude                                                 | -73.95 |
| Median Longitude                                               | -73.96 |
| The range of Longitude                                         | 0.53   |
| The range of Longitude in kilometer                            | 58.75  |


I calculate the maximum latitude and longitude that the hotspot is located using MAX() function.
I calculate the minimum latitude and longitude that the hotspot is located using MIN() function.
I calculate the mean latitude and longitude that the hotspot is located using AVERAGE() function.
I calculate the median using MEDIAN() function.
I calculate the range by minus MAX with MIN.
I convert the range into kilometer by multiplying the value with 111.
The insight here is that, the latitude and longitude between max and min values can be very small from the value they present. However, since latitude and longitude are on the scale of the earth, when they turn to kilometer, the range is 43.76 km and 58.75 km, which is huge on km basis. So it can be sure that the hotspots are allocated 43.78 km vertically and 58.75 horizontally.

### Conditional aggregate statistics analysis
I then do aggregate statistics by conditions
| Aggregate Statistics by conditions of Borough Name |                |
|----------------------------------------------------|----------------|
| Borough Name                                       | No. of hotspot |
| Manhattan                                          | 1672           |
| Queens                                             | 531            |
| Brooklyn                                           | 700            |
| Bronx                                              | 316            |
| Staten Island                                      | 100            |
| Total number of Hotspots                           | 3319           |
| Borough with maximum numbers of hotspot            | Manhattan      |
| Borough with minimum numbers of hotspot            | Staten Island  |

This describes Number hotspots by the borough name.
I use the function COUNTIF() to given condition of borough name to count how many hotspots are in one area.
From the table, I also use SUM() to calculate the total numbers of hotspots in NYC.
To generate more insights, I use the function INDEX() and MATCH():
```
=INDEX(O20:O24, MATCH(MAX(P20:P24), P20:P24, 0))
```
I use MATCH() and INDEX to find the MAX numbers of hotspot is belong to which borough. Hence, in this case, it is Manhattan. Similarly, I find the MIN number belongs to which, too. Therefore, I can say that for all hotspots in NYC, most of them concentrated in Manhattan. Least of them contained in Staten Island. 

This is the result that I add condition to describe hotspots that are free in different boroughs.
| Aggregate Statistics by conditions--Type |                   |
|------------------------------------------|-------------------|
| Borough                                  | Number of Hotspot |
| In Manhattan given its free              | 1573              |
| In Queens given its free                 | 379               |
| In Brooklyn given its free               | 540               |
| In Bronx given its free                  | 196               |
| In Staten Island given its free          | 48                |
| Total free hotspots                      | 2736              |
I use COUNTIFS() function to convey the numbers. For example,
```
=COUNTIFS(K2:K3320, "Manhattan", B2:B3320,"Free")
```
I add multiple arguments to restrict my answer. Compared with the previous table I create. It shows that the free WiFi hotspot distribution in different boroughs are similar to all hotspots distribution. It also follows the pattern that Manhattan has the most free hotspots while Staten Island has the least. Yet, compared with the total number of hotspots, freespots have 2736, which is 82.4% of all hotspots.

I also do some further analysis on these data.
| General Aggregate Statistics by conditions                             |                                     |
|------------------------------------------------------------------------|-------------------------------------|
| Max latitude of hotspot given its free and in Manhattan                | 40.868072                           |
| Its location                                                           | Inwood-207 St (A)                   |
| Its Neigborhood                                                        | Marble Hill-Inwood                  |
| Max longitude of hotspot given its free and in Manhattan               | -73.919899                          |
| Its location                                                           | Inwood-207 St (A)                   |
| Its Neigborhood                                                        | Marble Hill-Inwood                  |
| Min latitude of hotspot given its free and in Manhattan                | 40.68517                            |
| Its location                                                           | Motor Pool Building 925 Rooftop     |
| Its Neigborhood                                                        | Governors Island                    |
| Min longitude of hotspot given its free and in Manhattan               | -73.919899                          |
| Its location                                                           | Motor Pool Building 925 Rooftop     |
| Its Neigborhood                                                        | Governors Island                    |
| Max latitude of hotspot given its free                                 | 40.90372278                         |
| Its Borough                                                            | Bronx                               |
| Its Neigborhood                                                        | North Riverdale-Fieldston-Riverdale |
| Max longitude of hotspot given its free                                | -73.71483776                        |
| Its Borough                                                            | Queens                              |
| Its Neigborhood                                                        | Glen Oaks-Floral Park-New Hyde Park |
| Mean Latitude of hotspot distribution given its free and in Manhattan  | 40.76817464                         |
| Mean Longitude of hotspot distribution given its free and in Manhattan | -73.97421153                        |

I give condition to find the hotspot that is free and in Manhattan with the maximum latitude and longitude. I use MAXIFS() functions to accomplish. 
```
=MAXIFS(F2:F3320, B2:B3320, "Free", K2:K3320, "Manhattan")
```
I then display their location and neigborhood respectivly using MAXIFS within MATCH() within INDEX()
```
=index(E2:E3320, MATCH(MAXIFS(F2:F3320, B2:B3320, "Free", K2:K3320, "Manhattan"),F2:F3320, 0))
```
Surprisingly, I found that the location of hotspot with maximum latitude & longitude is the same. It is in Marble Hill-Inwood. Hence, hotspot in Marble Hill-Inwood is Manhattan's  farthest free hotspot location with maximum latitude and longitude.

Similarly, I do the free hotspot place in Manhattan with minimum latitude and longitude using the similar functions. Surprisingly, the location of hotspot with minimum latitude & longitude is also the same, which is in Governor's Island. Hence, hotspot in Motor Pool Building is Manhattan's free hotspot location with minimum latitude and longitude.

I then calculate the free hotspot with maximum latitude. The result shows that it is in Bronx, which is also legit because Bronx is NYC's northest borough. In terms of maximum longitude, the result is in Queens, which is also legit because Queens is in eastest of NYC.

I then calculate the mean latitude and longitude of free hotspot in Manhattan to see does the hotspots spread evenly.
```
=averageifs(F2:F3320, B2:B3320, "Free", K2:K3320, "Manhattan")
```
The average lat. and longi. of hotspot distribution given its free & in manhattan is located in Wollman Rink in Central Park, which is the middle of Manhattan. So it appears to be relativly even-spreading.

### Pivot Table
(Sometimes the "Total" column will turn to Chinese "总计". I try to change the setting, but it sometimes might not work. So it will sometimes appear Chinese characters on "Total" column.)

I use the pivot table to show how providers distribute among 5 boroughs in NYC

| COUNTA for "Provider"   | Borough Name |          |           |        |               |      |
|-------------------------|--------------|----------|-----------|--------|---------------|------|
| Provider                | Bronx        | Brooklyn | Manhattan | Queens | Staten Island | Total|
| ALTICEUSA               | 120          | 117      | 237       |        |               |237   |
| AT&T                    | 3            | 6        | 13        | 3      | 2             |27    |
| BPL                     |              | 59       |           |        |               |59    |
| Chelsea                 |              |          |  30       |        |               |30    |
| City Tech               |              | 11       |           |        |               |11    |
| Downtown Brooklyn       |              | 100      |           |        |               |100   |
| Fiberless               |              |          |   30      |        |               |30    |
| Harlem                  |              |          |101        |        |               |101   |
| LinkNYC - Citybridge    | 137          | 257      | 1175      | 265    |34             |1868  |
| Manhattan Down Alliance |              |          |     36    |        |               |36    |
| NYCHA                   |              | 28       |           |        |               |28    |
| NYPL                    | 35           |          |  43       |        |12             |90    |
| Partner                 |              |          |  2        |        |               |2     |
| QPL                     |              |          |           | 65     |               |65    |
| SPECTRUM                |              | 43       | 97        | 151    |52             |343   |
| Spot On Networks        |              |          |           |  16    |               |16    |
| Transit Wireless        | 21           | 79       | 145       | 31     |               |276   |
| Total                   | 316          | 700      | 1672      | 531    | 100           | 3319 |

The results show that there are 17 providers of hotspot. Every provider has its own distribution of hotspots. 
The most dominated providers is the LinkNYC - Citybridge. Its main focus is on Manhattan, yet it also covers other 4 areas. 
ALTICEUSA sets its hotspots in Bronx, Brooklyn, and Manhattan. 
AT&T covers all boroughs but has small numbers of devices. So it covers big but density is low.
BPL, City Tech, Downtown Brooklyn, and NYCHA are only focus on Brooklyn. Chelsea, Fiberless, Harlem, Manhattan Down Alliance, and Partner only focus on Manhattan. QPL and Spot On Networks only focus on hotspots in Queens. 
NYPL has its service only not in Brooklyn and Queens. So it develops its services vertically.
SPECTRUM expands its services in all boroughs except Bronx so it concentrates its services on lower NYC.
Transit Wireless has hotspots on all boroughs except Staten Island so it focuses more service on continent.

This is the second pivot table. It shows the borough names and their respective type if hotspot.
| COUNTA For Type | Type |              |              |       |
|-----------------|------|--------------|--------------|-------|
| Borough Name    | Free | Limited Free | Partner Site | Total |
| Bronx           | 196  | 120          |              | 316   |
| Brooklyn        | 540  | 160          |              | 700   |
| Manhattan       | 1573 | 97           | 2            | 1672  |
| Queens          | 379  | 152          |              | 531   |
| Staten Island   | 48   | 52           |              | 100   |
| Total           | 2736 | 581          | 2            | 3319  |

The result shows that there are 3 types of WiFi hotspot, free, limited free, and partner site. The majority of them are free and limited free. The only partner Site are in Manhattan. In general, the number of free hotspot will outweight the limited free hotspot. However, it is not true in Staten Island where limited free hotspots are more than free hotspots. The most extreme ratio between free hotspot and unlimited free hotspot is in Manhattan, for which the ratio is roughly 16:1. For which among 17 hotspots, 16 of them are free.

### Charts
I also generate two charts.
The first image shows the number of hotspots in different boroughs. It is similar to what I describe on aggregate statistcis by condition. Manhattan has the most hotspots. Staten Island has the least number of hotspot. Brooklyn is 2nd most, Queens is 3rd most, and Bronx is 4th most.
![Number of hotspots by borough](https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/images/numboro1.png)

The second chart shows the number of free hotspots in different boroughs.
![Number of free hotspots by borough](https://github.com/dbdesign-assignments-spring2023/spreadsheet-analysis-shuwuyou/blob/main/images/numborofree.png)
The free hotspots follow the same pattern as all hotspots. Manhattan did not change much becuase it has more free hotspots. Yet, Staten Island's histogram's column shrinks the most, showing that Staten Island has a lot of limited free hotspots yet less free hotspots.

## Extra Credit
I think my work fits option2: Extra Credit is available for examples which tackle large and/or complex data tables. A large data set, for our purposes, being defined as thousands of rows.
In my raw data file, it contains more than 3000 rows of data, specifically 3319 rows and 29 columns. Hence, I believe I can receive an extra credit.