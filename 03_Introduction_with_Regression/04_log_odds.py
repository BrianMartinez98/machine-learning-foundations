import numpy as np

# Calculate odds_of_rain
odds_of_rain = 0.4 / 0.6

# Calculate log_odds_of_rain
log_odds_of_rain = np.log(odds_of_rain)

# Calculate odds_on_time
odds_on_time = 0.9 / 0.1

# Calculate log_odds_on_time
log_odds_on_time = np.log(odds_on_time)

print("Odds of rain:", odds_of_rain)
print("Log-odds of rain:", log_odds_of_rain)

print("Odds of train being on time:", odds_on_time)
print("Log-odds of train being on time:", log_odds_on_time)
