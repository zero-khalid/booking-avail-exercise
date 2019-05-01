# booking-avail-exercise

Dependencies: 
- Python 3
- Jupyter
- Pandas
- Pandas Schema
- Matplotlib
- GeoBases

Using data provided by email

```
# Data quick look w/ CLI
head -n200 searches.csv  > subset_200_searches.csv
column -s^ -t < subset_200_searches.csv| less -#2 -N -S

head -n200 bookings.csv  > subset_200_bookings.csv
column -s^ -t < subset_200_bookings.csv| less -#2 -N -S
```
