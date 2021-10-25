def oracle_difference(current_price, oracle_price, a):
    return a * (1 + abs(current_price - oracle_price))
