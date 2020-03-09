def feast(beast, dish):
    begining = beast.startswith(dish[:1])
    end = beast.endswith(dish[-1:])
    return begining and end
