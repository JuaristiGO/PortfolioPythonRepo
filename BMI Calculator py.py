#!/usr/bin/env python
# coding: utf-8

# # BMI CALCULATOR
# 
# 

# In[2]:


#Body mass index calculator, is a measurement of body fat based on height and weight
#BMI = (weight in pounds * 703) / (height in inches * height in inches)


# In[28]:


def BMI_calculator(weight,height):
    BMI = ((weight * 703) / (height * height))
    print(f'Yor BMI is: {round(BMI,4)}')
    if BMI > 0:
        if BMI <= 18.5:
            print('You are Underwight.')
        elif BMI > 18.5 and BMI <= 24.9:
            print('You are Normal Weight.')
        elif BMI >24.9 and BMI <=29.9:
            print('You are Overweight.')
        elif BMI >29.9:
            print('You are Obese')
        elif BMI >35:
            print('You are Severely Obese.')
        elif BMI > 39.9:
            print('You are Morbidly Obese')
    else:
        print('Enter valid input.')

BMI_calculator(150,69)


# In[12]:


weight = input('Enter your weight in pounds: ')
weight = int(weight)
height = input('Enter your height in inches: ')
height = int(height)
BMI = ((weight * 703)/(height*height))
print(round(BMI,4))


# In[13]:


#Add more information
# Under 18.5: Underweight*Minimal.
# 18.5 - 24.9: Normal Weight-*Minimal.
# 25 - 29.9: Overweight-*Increased
# 30 - 34.9: Obese--*High
# 35 - 39.9: Severely Obese-*Very High
# 40 and over: Morbidly Obese-*Extremely High


# In[14]:


if BMI > 0:
    if BMI <= 18.5:
        print('You are Underwight.')
    elif BMI > 18.5 and BMI <= 24.9:
        print('You are Normal Weight.')
    elif BMI >24.9 and BMI <=29.9:
        print('You are Overweight.')
    elif BMI >29.9:
        print('You are Obese')
    elif BMI >35:
        print('You are Severely Obese.')
    elif BMI > 39.9:
        print('You are Morbidly Obese')
else:
    print('Enter valid input.')


# In[16]:


weight = input('Enter your weight in pounds: ')
weight = int(weight)
height = input('Enter your height in inches: ')
height = int(height)
BMI = ((weight * 703)/(height*height))
print(f'Your BMI is: {round(BMI,4)}')
if BMI > 0:
    if BMI <= 18.5:
        print('You are Underwight.')
    elif BMI > 18.5 and BMI <= 24.9:
        print('You are Normal Weight.')
    elif BMI >24.9 and BMI <=29.9:
        print('You are Overweight.')
    elif BMI >29.9:
        print('You are Obese')
    elif BMI >35:
        print('You are Severely Obese.')
    elif BMI > 39.9:
        print('You are Morbidly Obese')
else:
    print('Enter valid input.')




# In[17]:


#Add centimeters and kilograms input



# In[56]:


def centimeters_inches(cm):
    inches = cm*.393701
    return print(f'Your height is {round(inches,0)} inches.')

centimeters_inches(200)


# In[57]:


def kilograms_pounds(kg):
    pounds = kg*2.20462
    return print(f'Your weight is {round(pounds,0)} pounds.')
    
    
kilograms_pounds(80)


# In[65]:


def BMI_calculator(weight,height):
    BMI = ((weight * 703) / (height * height))
    print(f'Yor BMI is: {round(BMI,4)}')
    if BMI > 0:
        if BMI <= 18.5:
            return print('You are Underweight.')
        elif BMI > 18.5 and BMI <= 24.9:
            return print('You are Normal Weight.')
        elif BMI >24.9 and BMI <=29.9:
            return print('You are Overweight.')
        elif BMI >29.9:
            return print('You are Obese')
        elif BMI >35:
            return print('You are Severely Obese.')
        elif BMI > 39.9:
            return print('You are Morbidly Obese')
    else:
        return print('Enter valid input.')
    return BMI 


# In[66]:


print("""Welcome to the BMI calculator. 
1) Use the BMI_calculator to know your BMI and physical status with pounds and inches.
2) You can convert centimeters to inches using the centimeters_inches calculator.
3) You can convert kilograms to pounds using the kilograms_punds calculator.""" )
option = input('Which option do you want to use: ')
option = int(option)
if option == 1:
    BMI_calculator(int(input('Pounds: ')), (int(input('Inches: '))))
elif option == 2: 
    centimeters_inches(int(input('Centimeters: '))) 
    print('Write down your height in inches to reuse the BMI calculator')
elif option == 3:
    kilograms_pounds(int(input('Kilograms: '))) 
    print('Write down your weight in inches to reuse the BMI calculator')
else:
    print('Enter a valid input: ')

    


# In[ ]:





# In[ ]:




