from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

print("OS DETAILS : ", platform())                              #Windows-10-10.0.19613-SP0
print("HARDWARE : ", machine())                                 #AMD64
print("PROCESSOR : ", processor())                              #Intel64 Family 6 Model 78 Stepping 3, GenuineIntel
print("OS NAME : ", system())                                   #Windows
print("OS VERSION : ", version())                               #10.0.19613
print("Python COMPILER : ", python_implementation())            #CPython
print("Python COMPILER VERSION : ", python_version_tuple())     #('3', '6', '5')
