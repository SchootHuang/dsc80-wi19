## Midterm Concepts list

### Messy Data
* What is 'data generating process'
* Know how to evaluate the EDA topics: Granularity, Scope, Temporality, Faithfulness

### Null Values
* Understand Missingness Types (MCAR, MAR, MNAR, MD)
* Know how to determine missingness types
* Know null values effect on computing processing

### Granularity
* Split-apply-combine (what can be passed into 'apply')?
* How are groupby/pivot used to compute conditional distributions?
* Simpson's Paradox: computing it from aggregate stats; interpreting it.

### Combining Data
* inner/outer/left/right -- when to use each?
* many-to-many (or one) joins -- how to deal?
* Joining different granularities: look at SSA 'names' examples

### Smoothing
* Computing empirical distributions
* Binning and percentiles
* Additive smoothing -- interpolate between distributions
* Rolling windows: how do you compute with them? what do they do to statistics? outliers?

### Imputation
* For each of the following: when are they (in)appropriate to use? Why
  are they good/bad? How to compute them? How are they connected to
  MCAR/MAR/NMAR?
  
1. Dropping Nulls, 
2. Single value imputations, 
3. imputing with a distribution (like HW, lecture), 
4. multiple imputation (just know sketch of implementation)

### Geographical Data
* Basic ingredients to geo data (lat/longs, lines, polygons, multi-geometries)
* Noisy geo data techniques: rolling window on a sequence, 2D histogram, aggregate by a geographical region.
* Understanding how geographic-specific measurements are used: distance, point in region. (You *don't* have to memorize haversine distance formula!)
