print("Celsius till Farenheit tabell")
print("   Celsius\tFarenheit")
print("---------------------------")
for C in range(-40,41):
    print("   ",C,"\t",int(32+C*(9/5)))
