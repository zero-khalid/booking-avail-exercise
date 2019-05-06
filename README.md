# booking-avail-exercise

[HTML preview of the Jupiter notebook](http://htmlpreview.github.com/?https://github.com/zero-khalid/booking-avail-exercise/blob/master/avail-booking.html "HTML preview of the Jupiter Notebook")

Dependencies: 
- Python 3
- Jupyter
- Pandas
- Pandas Schema
- Matplotlib
- GeoBases
- Flask + Restful + Marshmallow
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

## Benchmark webservice with wrk tool

### Without cache
```kz@kz-virtualbox:~/wrk$ wrk -t12 -c50 -d60s http://127.0.0.1:5000/list
Running 1m test @ http://127.0.0.1:5000/list
  12 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     1.29s   452.13ms   1.95s    66.67%
    Req/Sec     0.84      1.88    10.00     89.39%
  366 requests in 1.00m, 48.67MB read
  Socket errors: connect 0, read 0, write 0, timeout 327
Requests/sec:      6.09
Transfer/sec:    829.80KB
```

### With 'simple' cache
```kz@kz-virtualbox:~/wrk$ wrk -t12 -c50 -d60s http://127.0.0.1:5000/list
Running 1m test @ http://127.0.0.1:5000/list
  12 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   106.43ms  111.37ms   1.80s    97.57%
    Req/Sec    43.67      8.74    80.00     86.57%
  30679 requests in 1.00m, 3.98GB read
  Socket errors: connect 0, read 0, write 0, timeout 2
Requests/sec:    510.51
Transfer/sec:     67.89MB
```
