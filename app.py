f = open("data.dat", "r")

lines = f.readlines()
i = 0

for line in lines:
    zeros = line.count("0")
    ones = line.count("1")

    if (zeros % 3 == 0):
        i += 1
    elif (ones % 2 == 0):
        i += 1
    print("zeros: {}, ones: {}, i: {}".format(zeros, ones, i), end=' ')
    print(line, end='')

print(i)

if __name__ == "main":
    main()
