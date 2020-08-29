# mortgage.py
#
# Exercise 1.7
rate_years = 30
mortage_value = 500000.00
interest_rate = 0.05
monthly_payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while mortage_value > 0:
    monthly = monthly_payment + extra_payment if extra_payment_start_month <= months <= extra_payment_end_month else monthly_payment

    mortage_value = mortage_value * (1 + interest_rate / 12) - monthly

    total_paid = total_paid + monthly
    months = months + 1

    print(round(months, 2), round(total_paid, 2), round(mortage_value, 2))

print('Total paid', round(total_paid, 2))
print('Months', 310)