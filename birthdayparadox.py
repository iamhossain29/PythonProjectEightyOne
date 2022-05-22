import datetime, random


def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


print('''Birthday Paradox''')

MONTHS = ('Jan', 'Feb', 'Mar', 'APR', 'MAY', 'Jun', 'Jul', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

print('Here are', numBDays, 'birthdays: ')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()

match = getMatch(birthdays)
print('In this simulation,', end='')
if match is not None:
    monthName = MONTHS[match.month - 1]
    dateText = "{} {}".format(monthName, match.day)
    print('Multiple people have a birthday on', dateText)
else:
    print('There are no matching birthdays.')
print()

print('Generating', numBDays, 'Random birthdays 100,000 times ...')
input('Press ENTER to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 10_00 == 0:
        print(i, 'simulations run....')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) is not None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

#########################################################################################

# 1. How are birthdays represented in this program? YYYY/MM/DD
# 2. How could you remove the maximum limit of 100 birthdays the program generates? By changing this  if response.isdecimal() and (0 < int(response) <= 100): to  if response.isdecimal() and (0 < int(response) <= 101):
# 3. What error message do you get if you delete or comment out numBDays = int(response) on line 57? NameError: name 'numBDays' is not defined
# 4. How can you make the program display full month names, such as 'January' instead of 'Jan'? It can be change here MONTHS = ('Jan', 'Feb', 'Mar', 'APR', 'MAY', 'Jun', 'Jul', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')
# 5. How could you make 'X simulations run...' appear every 1,000 simulations instead of every 10,000?  if i % 10_00 == 0: