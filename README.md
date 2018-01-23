# RF-random-generator
Random generator based on dump via rtl-sdr

## Usage
You can create number or string different size. With argument: NUMBER + `s` - string with digits, `d` - only digits.
### Example
```
$ python rand.py 2d
83
$ python rand.py 5s
ksLC2
```

----
# For collecting statistic:
```
for i in {1..1000}; do python rand.py 2d; done
```
After this use `$ python check_stat.py`.
