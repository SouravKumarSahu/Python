#Bit Wise Operation

#Try it online https://code.sololearn.com/cX4t8ddqKxN9

i = 15
j = 22

print(f'''
Bit Wise Operation

# hex and bit representation of numbers
i = {i} ; i hex = {hex(i)} ; i bin = {bin(i)}
j = {j} ; j hex = {hex(j)} ; j bin = {bin(j)}


# Logical and vs Bit &
Logical operations and -> i and j = {i and j} ; bit = {bin(i and j)} \nBit operations & -> i & j = {i & j} ; bit = {bin(i & j)}


# Logical or vs Bit |
Logical operations or -> i or j = {i or j} ; bit = {bin(i or j)} \nBit operations | -> i | j = {i | j} ; bit = {bin(i | j)}


# Bit ^ (xor)
Bit operations ^ -> i ^ j = {i ^ j} ; bit = {bin(i ^ j)}


# Bit ~ (negation)
Bit operations ~ -> ~i = {~i} ; bit = {bin(~i)}
''')

print('''
# Using Bit operators to identify one bit of in a byte, set the bit and reset the bit
# Example: We have to change 3rd bit of a 32 bits register Register = 0000000000000000000000000000x000
''')

flagRegister = 0x1234
print(f'\nflagRegister = {flagRegister} ; hex flagRegister = {hex(flagRegister)} ; bit flagRegister = {bin(flagRegister)}')

theMask = 2**3
print(f"\n# Note: the mask value is {theMask} because it's bin value is only 1 at 3rd position i.e. bin theMask = {bin(theMask)}")

print(f'\n# Check the state of your 3rd bit')
print(f'Value of 3rd bit = flagRegister & theMask = {flagRegister & theMask}')

print(f'\n# Set the state of your 3rd bit')
dummy_flagRegister = flagRegister | theMask
print(f'Set 3rd bit to 1 -> flagRegister | theMask = {dummy_flagRegister} ; bits = {bin(dummy_flagRegister)}')

print(f'\n# Reset the state of your 3rd bit')
dummy_flagRegister = flagRegister & ~theMask
print(f'Reset 3rd bit to 0 -> flagRegister & ~theMask = {dummy_flagRegister} ; bits = {bin(dummy_flagRegister)}')

print(f'\n# Negate the state of your 3rd bit')
print('NOTE: Bitwise negate equivalent to ## -1 x (variable + 1) ##')
dummy_flagRegister = flagRegister ^ theMask
print(f'Negate 3rd bit -> flagRegister ^ theMask = {dummy_flagRegister} ; bits = {bin(dummy_flagRegister)}')

print(f'''
# Binary left shift << | #Binary right shift >>
Syntax Variable Operator No. of positions to shift
NOTE: Binary left shift is equivalent to ## variable x (2 x n) ##
NOTE: Binary right shift is equivalent to ## variable / (2 x n) ##


In decimal system base is 10, hence
number multiplied by 10 is bassically left shift of all digits by one place
12345 × 10 = 123450
number divided by 10 is bassically right shift of all digits by one place
123450 / 10 = 12345


Similarly in binary system base is 2, hence

bin 17 = {bin(17)}

digits multiplied by 2 is bassically left shift of all digits by one place
17 << 1 = {bin(17)} × {bin(2)} = {17 << 1} = bin {bin(17 << 1)}

digits divided by 2 is bassically right shift of all digits by one place
17 >> 1 = {bin(17)} / {bin(2)} = {17 >> 1} = bin {bin(17 >> 1)}

digits shifted by two place is like number multiplied by 4
17 << 2 = {17 << 2} = bin {bin(17 << 2)}

digits shifted by three place is like number multiplied by 6
17 >> 3 = {17 >> 3} = bin {bin(17 >> 3)}

digits shifted by four place is like number multiplied by 8
17 << 4 = {17 << 4} = bin {bin(17 << 4)}
''')
