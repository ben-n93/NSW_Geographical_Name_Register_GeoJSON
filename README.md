![](https://github.com/ben-n93/NSW_Geographical_Name_Register_GeoJSON/actions/workflows/csv_to_geojson.yml/badge.svg)

# NSW Geographical Name Register - GeoJSON file

The [NSW Geographical Names Board](https://www.gnb.nsw.gov.au/) is a government body responsible for the management and administration of geographic place names within the state of New South Wales, Australia.

They very helpfully offer a [CSV file](https://proposals.gnb.nsw.gov.au/public/geonames/search) with all record information from their Geographical Name Register. 

I thought it would be of use to data analysts/scientists/journalists/developers to have a GeoJSON file from this data so I've created this repo. Every day my script downloads the CSV file and outputs it to a GeoJSON file (which you can find in the data directory).

## Data integrity 

It's worth noting that some of the coordinates might not be accurate as some were recorded at various times last century and so due to tectonic plate movement and other factors it's possible some of the coordinates aren't as accurate as they were when orginally recorded. I'm no geographer though!

### Acknowledgements

I have to shout out the brilliant [GeoJSON package](https://github.com/jazzband/geojson)!

### Contact

If you have any questions or feedback please reach out to at <hello@ben-nour.com>.
