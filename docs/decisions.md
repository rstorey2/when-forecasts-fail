# Project decisions

## Forecast archive selection

- NDFD was considered because it represents operational NWS digital forecasts. It was not selected for Version 1 because historical 2016 access required the NCEI AIRS/HAS delivery workflow, which is impractical for the one-week project timeline.
- HRRR was selected provisionally because NOAA provides a practical public historical archive with programmatic object and GRIB2-message access.
- The project evaluates HRRR model forecast error. It does not evaluate, rank, or criticize NWS public forecast performance.

## Version 1 scope

- Study period: 2020–2025.
- Initialization: 00 UTC.
- Forecast lead range: f12–f36.
- Forecast variable: HRRR 2-m temperature (`TMP:2 m above ground`).
- Observations: NOAA/NCEI Global Hourly, prioritizing ASOS stations.
- Error convention: forecast minus observation.

The 2020–2025 period and f12–f36 lead range were selected for Version 1 to provide a consistent lead-time range and a feasible public-data workflow. Availability must still be checked systematically before full retrieval.

## Locked observation-network methodology

- The station network is limited to ASOS stations in North Carolina and South Carolina, identified by crosswalking the NWS ASOS equipment roster with NCEI ISD identifiers.
- The primary spatial match is a fixed nearest HRRR 3-km grid-cell center for each station. Interpolation is not part of the primary analysis.
- For each forecast valid UTC hour, qualifying observations are searched from 10 minutes before the hour through the hour. The closest acceptable observation is selected; remaining ties prefer a routine hourly observation.
- Missing temperatures are not imputed. A forecast-observation pair without a qualifying observation is excluded.
- Final station completeness requires every study year and at least 90% of expected qualifying forecast-observation pairs. This result will be calculated only after the actual availability screen.
- The currently accessible Global Hourly listing ends on 2025-08-28. September–December 2025 availability is therefore an unresolved blocker for the locked full-year study period.
