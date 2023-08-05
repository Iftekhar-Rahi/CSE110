#Task  6
total=int(input())
def year_calculate(day):
  year=day//365
  remaining_year=day%365
  month=remaining_year//30
  r_day=remaining_year%30
  print(f"{year} years, {month} months and {r_day} days")
year_calculate(total)