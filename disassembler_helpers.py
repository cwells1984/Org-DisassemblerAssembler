def populate_registers():
    registers = {}
    registers[0] = '$zero'
    registers[1] = '$at'
    j = 0

    for i in range(2,3+1):
        registers[i] = '$v' + str(j)
        j += 1

    j = 0
    for i in range(4,7+1):
        registers[i] = '$a' + str(j)
        j += 1

    j = 0
    for i in range(8,15+1):
        registers[i] = '$t' + str(j)
        j += 1

    j = 0
    for i in range(16,23+1):
        registers[i] = '$s' + str(j)
        j += 1

    j = 8
    for i in range(24,25+1):
        registers[i] = '$t' + str(j)
        j += 1

    j = 0
    for i in range(26, 27 + 1):
        registers[i] = '$k' + str(j)
        j += 1

    registers[28] = '$gp'
    registers[29] = '$sp'
    registers[30] = '$fp'
    registers[31] = '$ra'

    return registers
