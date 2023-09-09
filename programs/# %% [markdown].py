# %% [markdown]
# # Odd & Even number check

# %%
def is_oddEven(num):
    return True if num % 2 == 0 else False

num = int(input('Enter the number: '))
msg1 = 'is an Even Number'
msg2 = 'is an Odd Number'
print(num, msg1) if is_oddEven(num) else print(num, msg2)
    

# %% [markdown]
# ## Series of odd and even numbers

# %%
for i in range(1,11):
    print(i, msg1) if is_oddEven(i) else print(i,msg2)

# %%
def oddSeries(n):
    for i in range(n+1):
        print(i) if is_oddEven(i) else None

def evenSeries(n):
    for i in range(n+1):
        None if is_oddEven(i) else print(i)

# %%
choice = input('Which type of series you want to generate(odd/even): ')
choice = choice.lower()
n = int(input('Enter the number upto you want to generate series: '))
oddSeries(n) if choice == 'odd' else evenSeries(n)


# %%



