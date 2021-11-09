
## autoClim: Modern Climate Events - Automated Tropospheric Global Profiles

*autoClim is currently under development, and many features that have been mentioned here may not be available. They've been marked with an asterisk(\*) under the Output Categories section for your convenience.*

<p align="center"><img src=https://user-images.githubusercontent.com/47943744/123750937-c550b800-d8d4-11eb-80f9-58d768010fd0.jpeg alt=autoClim_logo width="300" height="300" align="middle"></p>

### Authors:
- Mihir Dasgupta <<dasguptamihir10@gmail.com>>
- Abhijith Pradeep <<abhijithp20@gmail.com>>

It's exceedingly common to require reliable data when studying a specific climate event, like a tornado, for example. Significant local deviations from climatological normals, (a 30-year average of a weather variable for a given time of year, eg. JJA) can help us improve our understanding of these events. Faster, more accurate, and stronger forecasting is only attainable through an improved understanding of the mean climate system from which weather stems.

That being said, it's still unjustifiably cumbersome to be able to use this data to draw meaningful conclusions. It's an unruly process that involves identifying relevant datasets (from hundreds of options), downloading dozens of gigabytes of data, parsing through data structures, matrix manipulation, and endless graphing parameterization to finally come to a basic understanding of the climate system's state at the time of the event. It's a fairly routine ordeal, but remains an ordeal nonethelesss. 

*autoClim's trying to change that.*

Essentially, we're looking to create a framework that allows a user to develop a set (see 'Output Categories') of useful atmospheric profiles automatically, when given a date. We wanted to create a system that's automated end-to-end, that gives you the full picture you need, when you need it. Used effectively, the sheer number of variables autoClim brings should be able to give you a high-level idea of what's going on in the system, so that you can figure out how and where to dig a little deeper. 

We try to provide greater context by supplying profiles for the week of the date input to the system (&#177; 3 days). Therefore, output filenames with the "day4" suffix are profiles for the specific date the user requests. We use <a href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html" target="_blank">NOAA</a>'s <a href="http://www.atmos.albany.edu/daes/atmclasses/atm305/Kistler_2001.pdf" target="_blank"> NCEP/NCAR 1 reanalysis </a> for all our data requirements. We're completely open-source, having published under the <a href="https://github.com/Mihir-DG/autoClim/blob/main/LICENSE" target="_blank">MIT license</a>. 

To help  give you a better idea of what we're looking to create, we've attached samples to *finalOutput_plots/* for all currently-available output categories. The samples are currently centered on **November 7, 2020** (so, profiles are generated for the 4th to the 10th, inclusive!). Datasets (used for sample output) handled by the *downloadData()* function in **pullData.py** have not been added to the repository. For the sake of maintaining a clean directory structure, an empty stand-in text file has been added to their target folder.

**Execute *runMain.py* to create your own profiles! (Python 3.7)**

## Output Categories:

We strongly believe that autoClim's strength will lie in the diversity of the profiles it'll offer. Here's our list!
<ol>
													<br/>
													<li><b>Wind Quiver Plot (overlaying Air Temperature (K) contours): </b></li>
													<ul>
														<li> Uses zonal and meridional wind values as x- and y- vector components to generate a global dynamics profile. </li>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;; Air temperature sampling rate of 2.0, wind vector sampling rate of 3.0.</li>
														<li>Coverage: (Surface, 850 mbar pressure level, 250 mbar pressure level), Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Delta Profiles for Wind Quivers</b> - changes across the chosen week</li>
													<ul>
														<li>Identical resolution and spatial coverage as Wind Quivers.</li>
													</ul>
  <br/>
													<li><b>Air Temperature (K)</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: (Surface, 850 mbar pressure level, 250 mbar pressure level), Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Precipitation Rate (Kg/m<sup>2</sup>/s) </b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Relative Humidity (%)</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0; for 250 mbar and 850 mbar pressure levels; T62 Gaussian grid with 194x92 grid points for surface profiles </li>
														<li>Coverage: (Surface, 850 mbar pressure level, 250 mbar pressure level), Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Specific Humidity (kg/kg)</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0; for 250 mbar and 850 mbar pressure levels; T62 Gaussian grid with 194x92 grid points for surface profiles </li>
														<li>Coverage: (Surface, 850 mbar pressure level, 250 mbar pressure level), Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Cloud Cover (%)</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: EATM - Entire Atmosphere, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Skin Temperature (K) *</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Potential Temperature (K)*</b></li>
													<ul>
														<li>Provided to help identify vertical regions of convective instability (and thus, action).
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: Full vertical profiles for key latitudes (0&#xb0;, 30&#xb0;, 60&#xb0;, 90&#xb0; for each hemisphere), Global, 7 days
													</ul>
  <br/>
                          <li><b>Precipitable Water (Kg/m<sup>2</sup>)*</b></li>
												 	<ul>
												 		<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: EATM - Entire Atmosphere, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Latent Heat Net Flux (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Sensible Heat Net Flux (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Ground Heat Net Flux (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Potential Evapotranspiration Rate (mm/s)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Outgoing Longwave Radiation - OLR (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: NTAT (Nominal Top of Atmosphere) / Aggregate Radiating Pressure, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Emitted Upwelling Longwave Radiation (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Net Longwave Radiation (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Net Shortwave Radiation (W/m<sup>2</sup>)*</b></li>
													<ul>
														<li>Resolution: T62 Gaussian grid with 194x92 grid points</li>
														<li>Coverage: Surface, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Tropopause Air Temperature i.e. Local minimum (K)*</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: Tropopause, Global, 7 days</li>
													</ul>
  <br/>
													<li><b>Tropopause Air Pressure (mbar)*</b></li>
													<ul>
														<li>Resolution: 2.5&#xb0; x 2.5&#xb0;</li>
														<li>Coverage: Tropopause, Global, 7 days</li>
													</ul>
												</ol>
<em>*: Currently under development</em>
 

### Dependencies:
- **numpy v1.19.5**: Primary module used for data handling throughout the project.
- **Matplotlib v3.3.4**: Used to present results graphically.
- **netCDF4 v1.5.2**: Used as a handler for .nc file input.
- **Cartopy v0.19.2**: Provides a global basemap.
- **wget v3.2.0**: Web interfacing to automate dataset downloads.
- **os**: Handles internal directory structure.
- **PIL v1.1.6**: Setting up the basemap usage in plots.


