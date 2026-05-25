from knn_utils import min_max_normalize

release_dates = [
    1897.0, 1998.0, 2000.0, 1948.0, 1962.0,
    1950.0, 1975.0, 1960.0, 2017.0, 1937.0,
    1968.0, 1996.0, 1944.0, 1891.0, 1995.0,
    1948.0, 2011.0, 1965.0, 1891.0, 1978.0,
]

normalized_dates = min_max_normalize(release_dates)

print("Normalized release dates:")
print(normalized_dates)
