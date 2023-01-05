def manday_calculator(organization_size, complexity, additional_requirements):
  man_days = 0
  if organization_size == "small":
    man_days += 2
  elif organization_size == "medium":
    man_days += 4
  elif organization_size == "large":
    man_days += 6
  else:
    man_days += 1
    
  if complexity == "low":
    man_days += 1
  elif complexity == "medium":
    man_days += 2
  elif complexity == "high":
    man_days += 3
  else:
    man_days += 1
    
  if additional_requirements == "design and development":
    man_days += 3
  elif additional_requirements == "higher risk activities":
    man_days += 5
  else:
    man_days += 0
    
  return man_days