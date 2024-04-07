""" 
This script downloads the NSW Geographic Name Register[1_] and
creates a GeoJSON file.

References
----------
.. [1] https://proposals.gnb.nsw.gov.au/public/geonames/search
"""

import geojson
import pandas as pd
import requests


def main():
    # Download CSV file.
    response = requests.get(
        "https://dcok8xuap4.execute-api.ap-southeast-2.amazonaws.com/prod/public/placenames/geonames/download",
        timeout=60,
    )
    with open("data/input.csv", "wb") as f:
        f.write(response.content)

    # Create GeoJSON file.
    df = pd.read_csv(
        "data/input.csv",
        skiprows=4,
        dtype={
            "REFERENCE": str,
            "PLACENAME": str,
            "DESIGNATION": str,
            "STATUS": str,
            "DUAL NAME": str,
            "GAZETTE DATE": str,
            "GEOGRAPHICAL NAME": str,
            "PREVIOUS NAMES": str,
            "GNB FILE": str,
            "LGA": str,
            "LGA AT GAZETTAL": str,
            "1:25,000 MAP NAME": str,
            "1:100,000 MAP": str,
            "PARISH": str,
            "COUNTY": str,
            "DESCRIPTION": str,
            "MEANING": str,
            "ORIGIN": str,
            "HISTORY": str,
            "PRONUNCIATION": str,
            "ABORIGINAL NAME": str,
            "GDA2020 LAT": float,
            "GDA2020 LONG": float,
        },
    )

    features = []
    for index, row in df.iterrows():
        if pd.isna(df.at[index, "GDA2020 LAT"]):
            coordinates = geojson.Point()
        else:
            coordinates = geojson.Point((row["GDA2020 LONG"], row["GDA2020 LAT"]))

    properties = df.loc[
        index,
        [
            "REFERENCE",
            "PLACENAME",
            "DESIGNATION",
            "STATUS",
            "DUAL NAME",
            "GAZETTE DATE",
            "GEOGRAPHICAL NAME",
            "PREVIOUS NAMES",
            "GNB FILE",
            "LGA",
            "LGA AT GAZETTAL",
            "1:25,000 MAP NAME",
            "1:100,000 MAP",
            "PARISH",
            "COUNTY",
            "DESCRIPTION",
            "MEANING",
            "ORIGIN",
            "HISTORY",
            "PRONUNCIATION",
            "ABORIGINAL NAME",
        ],
    ].to_dict()

    new_properties = {}
    for key, value in properties.items():
        if pd.isna(
            df.at[index, key]
        ):  # Nan values will result in error when passed to GeoJSON.
            new_properties[key] = None
        else:
            new_properties[key] = value

    feature = geojson.Feature(geometry=coordinates, properties=new_properties)
    features.append(feature)

    # Write GeoJSON file.
    feature_collection = geojson.FeatureCollection(features)
    with open("data/output.geojson", "w", encoding="utf-8") as f:
        geojson.dump(feature_collection, f)


if __name__ == "__main__":
    main()
