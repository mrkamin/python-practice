price = 1000000

has_good_credet = False
has_bad_credet  = False

if has_good_credet:
    down_pyment = 0.1 * price
    print(down_pyment)
elif has_bad_credet:
    down_pyment = 0.2 *price
    print(down_pyment)
else:
    down_pyment = 0.15 *price
    print(down_pyment)