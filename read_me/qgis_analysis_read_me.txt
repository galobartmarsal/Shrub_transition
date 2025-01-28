QGIS analysis Methodology Summary:

To analyse and evaluate shrubland transitio, we use the 1987 and 2022 Land Use Land Cover Maps (from now on, LULCM) raster layers from Catalunya (30x30m) elaborated by CREAF.

First, we selected the shrubland class from 1987 LULCM (class 14) and we converted to pixel every point, to get a point vector layer.

(Due to the magnitude of data information, more than 8.000.000 pixels, que separated the pixels in differents regions, 9 regions of Catalunya, and then, after corssing the data with pixels, we elaborated a new table gathergin all this 9 regions in a general table of Catalonia, see Python folder to see the code treatment).

Secondly, from 2022 LULCM, we did a reclassification into 9 clases, combingin all the clases with similatirties. The reclassification was as follows: urbanised areas (classes 4,5,6,7), forest areas (classes 15,16,17), shrubland areas (14), agricultural areas (classes 19,20,21,22,23,24,25), meadow areas (classes 11,12,13), wetland vegetation (class 10), areas with few or no vegetation (class 9) and other classes (classes 2,3). We excluded class 1 (marine water) for unlikely transition. After, we obtained one raster layer for every class.

Moreover, we excluded all the burned áreas (class 18) in the years between 1987 and 2022 (both included).

Then, we used the plugin Point Sampling tool from QGIS, to cross the shrubland point vector layer from 1987 with the variables raster layer and every raster class from 2022. In this way, we obtained, for every pixel, its topographic and climatic variables and the land cover change to 2022.