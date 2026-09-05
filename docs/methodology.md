# Proposed methodology

## Scope

This project investigates meteorological conditions associated with larger short-term HRRR 2-m temperature forecast errors across North Carolina and South Carolina. It evaluates HRRR model forecast error, not official NWS public forecast performance.

Version 1 uses 00Z HRRR initializations for 2020–2025, forecast leads f12 through f36, and the `TMP:2 m above ground` GRIB2 field.

## Forecast-observation pairing

For every selected initialization, lead, and station/grid pairing:

```text
forecast_reference_time = HRRR GRIB2 reference time (UTC)
lead_time_hours         = HRRR GRIB2 forecast time
forecast_valid_time     = reference time + lead time
forecast_error           = HRRR forecast temperature - observed temperature
```

The matching NCEI Global Hourly temperature observation must have the same valid timestamp in UTC. Temperature units will be harmonized before the error is calculated.

## Spatial matching

Each selected station will be matched once to the HRRR Lambert Conformal grid. The initial rule is to transform the station coordinates into the HRRR projection and select the nearest grid-cell center. The stored pairing record will include station identifier, station coordinates/elevation, grid indices, grid-cell coordinates/elevation if available, and matching distance.

The same fixed grid cell will be used for a station throughout a consistent HRRR grid configuration. A sensitivity check using interpolation may be considered later; it is not part of Version 1.

## Planned analysis, not yet implemented

The future workflow will calculate signed bias, mean absolute error, and RMSE by station, season, lead time, and environmental grouping. Associations will be described as associations, not causal effects. Statistical significance will be reported only after an appropriate, pre-specified test.

