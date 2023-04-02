#facebook practice problem
#Author : Darshan Radadiya

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  result = ""
  for i in input_str:
      if i.isdigit():
          result += (str((int(i)+rotation_factor)%10))
      elif i.isalpha():
          if i.isupper():
              result += chr((ord(i)+rotation_factor - 65)%26 + 65)
          else:
              result += chr((ord(i)+rotation_factor - 97)%26 + 97)
      else: 
          result += i
  print(result)
  return result

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)