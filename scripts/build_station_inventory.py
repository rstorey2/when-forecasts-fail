from pathlib import Path

import pandas as pd
import requests


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "data" / "processed"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# NCEI ISD station-history file
STATION_HISTORY_URL = (
    "https://www.ncei.noaa.gov/pub/data/noaa/isd-history.csv"
)

# Our candidate ASOS stations
ASOS_STATIONS = {
    # North Carolina
    "KAKH", "KAVL", "KBUY", "KCLT", "KECG", "KEQY",
    "KEWN", "KFAY", "KGSO", "KHKY", "KHSE", "KILM",
    "KINT", "KLBT", "KMEB", "KMRH", "KRDU", "KRWI",

    # South Carolina
    "KAND", "KCAE", "KCEU", "KCHS", "KCRE", "KCUB",
    "KFLO", "KGMU", "KGRD", "KGSP", "KOGB", "KUZA",
}


def download_station_history() -> pd.DataFrame:
    """Download and return the NCEI ISD station-history table."""

    print("Downloading NCEI station metadata...")

    response = requests.get(STATION_HISTORY_URL, timeout=60)
    response.raise_for_status()

    raw_file = RAW_DATA_DIR / "isd-history.csv"
    raw_file.write_bytes(response.content)

    print(f"Saved raw metadata to: {raw_file}")

    return pd.read_csv(raw_file)


def main() -> None:
    stations = download_station_history()

    # NCEI stores ICAO identifiers in the ICAO column.
    stations["ICAO"] = stations["ICAO"].astype(str).str.strip()

        # Keep only our candidate ASOS stations in North Carolina
    # and South Carolina that were active at the beginning
    # of our study period.
    selected = stations[
        stations["ICAO"].isin(ASOS_STATIONS)
        & stations["STATE"].isin(["NC", "SC"])
    ].copy()

    # Convert station history dates to datetime.
    selected["BEGIN"] = pd.to_datetime(
        selected["BEGIN"].astype(str),
        format="%Y%m%d",
        errors="coerce",
    )

    selected["END"] = pd.to_datetime(
        selected["END"].astype(str),
        format="%Y%m%d",
        errors="coerce",
    )

    # Keep station records that cover the beginning of our study period.
    study_start = pd.Timestamp("2020-01-01")

    selected = selected[
        (selected["BEGIN"] <= study_start)
        & (selected["END"] >= study_start)
    ].copy()

    # Display the important metadata.
    columns = [
        "USAF",
        "WBAN",
        "STATION NAME",
        "CTRY",
        "STATE",
        "ICAO",
        "LAT",
        "LON",
        "ELEV(M)",
        "BEGIN",
        "END",
    ]

    selected = selected[columns].sort_values(["STATE", "ICAO"])

    selected["BEGIN"] = selected["BEGIN"].dt.strftime("%Y%m%d")
    selected["END"] = selected["END"].dt.strftime("%Y%m%d")

    output_file = OUTPUT_DIR / "candidate_asos_stations.csv"
    selected.to_csv(output_file, index=False)

    print()
    print(f"Found {len(selected)} matching station records.")
    print(f"Saved inventory to: {output_file}")
    print()
    print(selected.to_string(index=False))


if __name__ == "__main__":
    main()