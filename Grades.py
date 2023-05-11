marks = int(input('Please enter your marks: '))

if marks >= 85:
    grade = 'A+'
    comment = 'Excellent!'

elif 80 <= marks < 85:
    grade = 'A'
    comment = 'Well done.'

elif 75 <= marks < 80:
    grade = 'B+'
    comment = ''

elif 70 <= marks < 75:
    grade = 'B'
    comment = ''

elif 65 <= marks < 70:
    grade = 'C+'
    comment = ''

elif 60 <= marks < 65:
    grade = 'C'
    comment = ''

elif 55 <= marks < 60:
    grade = 'D+'
    comment = ''

elif 50 <= marks < 55:
    grade = 'D'
    comment = ''

else:
    grade = 'F'
    comment = 'See me.'


print('Grade:', grade)
print(comment)
