# a list with one instruction
instructions = ['00000001101011100101100000100100',
                '10001101010010010000000000001000',
                '00001000000000010010001101000101',
                '00000010101010010101100000100010',
                '00000011111000000000000000001000',
                '00110101111100001011111011101111',
                '10101110100011010000000000100000',
                '00000010110011010101000000100000']

# dictionary of opcodes
op_codes = {0: 'R-type', 2: 'j', 3: 'jal', 8: 'addi', 12: 'andi', 13: 'ori', 35: 'lw', 43: 'sw'}

# dictionary of function codes
func_codes = {8: 'jr', 32: 'add', 34: 'sub', 36: 'and', 37: 'or'}

# dictionary of formats to print assembly instructions in - exceptional formats such as lw or sw can be specified here
formats = {'R-Default': '%(fn)s %(rd)s %(rs)s %(rt)s',
           'I-Default': '%(fn)s %(rt)s %(rs)s %(imm)s',
           'J-Default': '%(fn)s %(add)s',
           'jr':"%(fn)s %(rs)s",
           'lw':"%(fn)s %(rt)s %(imm)s %(rs)s",
           'sw':"%(fn)s %(rt)s %(imm)s %(rs)s"}

# dictionary of registers
registers = {0: '$zero', 1: '$at', 2: '$v0', 3: '$v1', 4: '$a0', 5: '$a1', 6: '$a2', 7: '$a3', 8: '$t0', 9: '$t1', 10: '$t2', 11: '$t3', 12: '$t4', 13: '$t5', 14: '$t6', 15: '$t7', 16: '$s0', 17: '$s1', 18: '$s2', 19: '$s3', 20: '$s4', 21: '$s5', 22: '$s6', 23: '$s7', 24: '$t8', 25: '$t9', 26: '$k0', 27: '$k1', 28: '$gp', 29: '$sp', 30: '$fp', 31: '$ra'}

# helper method
# converts a binary string to its hex representation by seperating the string into byte-length substrings and getting
# the hex of each (ex. "0010" => "0x2", "11000001" => 0xC1
def binary_to_hex(bin_string):
    hex_string = "0x"

    # if the # of bits is not div by 4 extract the leading 1-3 bits and treat these as the first "byte"
    j = len(bin_string) % 4
    if (j != 0):
        byte_string = bin_string[0:j]
        hex_string += hex(int(byte_string, 2)).split('0x')[1]

    # for the remaining bits go through and convert in hex by groups of 4
    for i in range(j, len(bin_string), 4):
        x = i
        byte_string = bin_string[x:x + 4]
        hex_string += hex(int(byte_string, 2)).split('0x')[1]

    return hex_string

# loop thru instructions and deassemble
for instruction in instructions:
    # get the first 6 bits (opcode) of the first instruction (index 0)
    opcode = instruction[0:6]

    # print instruction in binary and hex
    print(instruction)
    print(binary_to_hex(instruction))

    # get the instruction format
    if int(opcode, 2) == 0:
        print('This is an R-type instruction')

        # parse the instruction according to the R type format

        # 1. get the 6-bit function code using string slicing
        func_code = instruction[26:32]
        print('function code (binary): ' + func_code)

        # 2. look-up the function code in the dictionary
        instruction_name = func_codes[int(func_code,2)]
        print('MIPS Instruction: ' + instruction_name)

        # 3. get the 5-bit RS register and look it up in the dictionary
        rs = instruction[6:11]
        rs_register = registers[int(rs, 2)]
        print('RS Register: ' + rs_register)

        # 4. get the 5-bit RT register and look it up in the dictionary
        rt = instruction[11:16]
        rt_register = registers[int(rt, 2)]
        print('RT Register: ' + rt_register)

        # 5. get the 5-bit RD register and look it up in the dictionary
        rd = instruction[16:21]
        rd_register = registers[int(rd, 2)]
        print('RD Register: ' + rd_register)

        # 6. print the instruction with the operands in the correct order
        if instruction_name in formats:
            print(formats[instruction_name] %{'fn':instruction_name, 'rs':rs_register})
        else:
            print(formats['R-Default'] %{'fn':instruction_name, 'rd':rd_register, 'rs':rs_register, 'rt':rt_register})

    elif int(opcode, 2) == 2 or int(opcode, 2) == 3:
        print('This is a J-type instruction')

        # 1. look-up the instruction based on the opcode
        instruction_name = op_codes[int(opcode, 2)]
        print('MIPS Instruction: ' + instruction_name)

        # 2. get the 26-bit address
        address = instruction[6:32]
        print('Address: ' + address)

        # 3. print the instruction with the operands in the correct order
        print(formats['J-Default'] %{'fn': instruction_name, 'add': binary_to_hex(address)})

    elif int(opcode, 2) > 3:
        print('This is an I-type instruction')

        # 1. look-up the instruction based on the opcode
        instruction_name = op_codes[int(opcode, 2)]
        print('MIPS Instruction: ' + instruction_name)

        # 2. get the 5-bit RS register and look it up in the dictionary
        rs = instruction[6:11]
        rs_register = registers[int(rs,2)]
        print('RS Register: ' + rs_register)

        # 3. get the 5-bit RT register and look it up in the dictionary
        rt = instruction[11:16]
        rt_register = registers[int(rt, 2)]
        print('RT Register: ' + rt_register)

        # 3. get the 16-bit immediate address
        immediate = instruction[16:32]
        print('Immediate Address: ' + immediate)

        # 4. print the instruction with the operands in the correct order
        if instruction_name in formats:
            print(formats[instruction_name] %{'fn':instruction_name, 'imm':binary_to_hex(immediate), 'rs':rs_register, 'rt':rt_register})
        else:
            print(formats['I-Default'] %{'fn':instruction_name, 'rt':rt_register, 'rs':rs_register, 'imm':binary_to_hex(immediate)})

    print("================================")