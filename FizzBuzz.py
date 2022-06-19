def FizzBuzz(number: int):
    if not number % 15:
        return 'FizzBuzz'
    elif not number % 5:
        return 'Buzz'
    elif not number % 3:
        return 'Fizz'
    else:
        return None

def LeanFizzBuzz(number: int):
    result = ''
    if not number % 3:
        result = 'Fizz'
    if not number % 5:
        result += 'Buzz'
    return result

def SillyFizzBuzz(number: int):
    result = ''
    suffix = 'zz'
    if not number % 3:
        result = 'Fi'
    if not number % 5:
        result += 'Bu'
    chunks = [result[i:i+2] for i in range(0, len(result), 2)] + ['']
    return ('zz').join(chunks)

def run():
    while __name__ == '__main__':
        number = input('Number: ')
        result = FizzBuzz(int(number))
        if result:
            print(result)

for number in range(1,101):
    result = SillyFizzBuzz(number)
    if result:
        print(f'{number}: {result}')
    else:
        print(f'{number}: -')
