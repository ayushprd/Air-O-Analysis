- September 28, 2019, Pawan Gupta (pawan.gupta@nasa.gov)
- The data sets are created for Space Challenge App
- The data file names are: 'Country_City_Location.ProductName.csv'
- The Product Name:
	- MYD04 : This represents MODIS-AQUA satellite (Afternoon overpass)
 	- MOD04 : This represents MODIS-TERRA satellite (Morning overpass)
- The data order in each file
	- YYYY, MM, DD, Latitude, Longitude, AOD1, AOD3, STD3
        Where
        AOD1: Aerosol Optical Depth at 550 nm for nearest grid to ground location
 	AOD3: Aerosol Optical Depth at 550 nm, averaged for 3x3 grids around ground location
	STD3: Standard Deviation in AOD3 
- Aerosol Optical Depth is a unitless quantity
- The data are extracted from MODIS deep blue and Dark Target algorithm and combined using best quality flags
- The valid AOD range is -0.05 to 5.0
- The missing data are filled with value of -1.0   

