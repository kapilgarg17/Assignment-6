# Answer Number 1
def perfect_number(n):

    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
n=int(input("enter the number :"))
if perfect_number(n)== True:
    print(n,",this is perfect number")
else:
    print(n,",this is not a perfect number")
print()
# ANSWER NUMBER 2
def isPalindrome(s):
    return s == s[::-1]
s=input("Enter the word:")
ans = isPalindrome(s)

if ans:
    print("Yes")
else:
    print("No")

print()
# Answer Number 3
def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(1,n+1):
      print(" "*(n-x),trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
n=int(input("enter the no of rows :"))
pascal_triangle(n)

print()
# ANSWER NUMBER 4
def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True
string =input("Enter the Sentence:")
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")


print()
# ANSWER NUMBER 5
n=input("enter the string: ")
l=n.split('-')
l.sort()
print('-'.join(l))

print()
# Answer Number 6
def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
        print(f"\nStudent Name:{kwargs['student_name']}")
        print(f"Student Class: {kwargs['student_class']}")

print()
# Answer Number 7
class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

print()
# Answer Number 8
class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

print()
# Answer Number 9
class py_solution:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(py_solution().is_valid_parenthese("(){}[]"))
print(py_solution().is_valid_parenthese("()[{)}"))
print(py_solution().is_valid_parenthese("()"))
