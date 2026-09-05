# Data sources

## Validated forecast source

The provisional forecast source is the NOAA High-Resolution Rapid Refresh (HRRR) public archive. HRRR is an hourly updated, 3-km operational model over the CONUS domain. Archive objects are GRIB2 files organized by initialization date, cycle, product type, and forecast hour.

The surface-file pattern used for Version 1 is:

```text
s3://noaa-hrrr-bdp-pds/hrrr.YYYYMMDD/conus/hrrr.t00z.wrfsfcfFF.grib2
```

Each file has a small companion index file ending in `.grib2.idx`. The index contains byte offsets for individual GRIB2 messages. The validated temperature selector is `TMP:2 m above ground`; it is temperature in Kelvin, encoded as GRIB2 category 0, parameter 0. For each selected message, the GRIB2 reference time and forecast time establish forecast issuance and valid time.

Validated archive checks showed the same path structure and the `TMP:2 m above ground` message for 2016 and 2025. The V1 study begins in 2020 because the selected 00Z f12–f36 range must be available consistently; 2016 did not provide the tested f36 object.

Official references:

- NOAA HRRR public archive: https://registry.opendata.aws/noaa-hrrr-pds/
- NOAA HRRR documentation: https://rapidrefresh.noaa.gov/hrrr/
- NCEP HRRR product inventory: https://www.nco.ncep.noaa.gov/pmb/products/hrrr/

## Validated observation source

The provisional observation source is NOAA/NCEI Global Hourly station data. The initial station pool will prioritize ASOS stations in North Carolina and South Carolina. Observed air temperature will be paired with the HRRR forecast valid time in UTC.

Official reference: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database

## Assumptions that require testing before production retrieval

- Which ASOS stations have sufficiently complete 2020–2025 hourly temperature records and usable quality flags.
- The final station-to-HRRR-grid rule: nearest fixed HRRR grid-cell center or a documented interpolation method.
- Whether the selected HRRR product and all f12–f36 leads are complete for every requested 00Z date from 2020–2025.
- Exact handling of missing, duplicate, special, and quality-flagged station observations.
- Whether station elevation and grid-cell elevation differences warrant screening or a sensitivity analysis.

