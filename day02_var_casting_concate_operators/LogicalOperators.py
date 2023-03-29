name = 'Joshua Osin'
age = 48
isUSCitizen = True

# for and operator both should be true
isEligibletoVote = age > 21 and isUSCitizen  # true and true => true

print(f'Is {name} eligible to Vote \n{isEligibletoVote}')

# for or operator one of them should be true

print(10 > 20 or True != False)

#for not operator will make it reverse True => False

print(not True) # means false
