# booking-avail-exercise

[HTML preview of the Jupiter playbook](http://htmlpreview.github.com/?https://github.com/zero-khalid/booking-avail-exercise/blob/master/avail-booking.html "HTML preview of the Jupiter playbook")

HTML preview of the Jupyter playbook: 

Dependencies: 
- Python 3
- Jupyter
- Pandas
- Pandas Schema
- Matplotlib
- GeoBases
- Flask + Restful
- Flask Restful Swagger

Using data provided by email

```
# Data quick look w/ CLI
head -n200 searches.csv  > subset_200_searches.csv
column -s^ -t < subset_200_searches.csv| less -#2 -N -S

head -n200 bookings.csv  > subset_200_bookings.csv
column -s^ -t < subset_200_bookings.csv| less -#2 -N -S

csvtool readable bookings_sorted_subset.csv -t '^'| view -
```


To run the webservice:
```
python3 webservice/airport.py
```

Swagger & API available at 
```
http://localhost:5000/api/v1/spec.html#!/spec
http://localhost:5000/
```

![alt text](https://github.com/zero-khalid/booking-avail-exercise/blob/master/swagger.png "Swagger API screenshot")
