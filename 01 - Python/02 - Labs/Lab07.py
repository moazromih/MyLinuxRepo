def SET_BIT(REG,BIT):
    return REG | (1<<BIT)

def CLR_BIT(REG,BIT):
    return REG & ~(1<<BIT)

def GET_BIT(REG,BIT):
    return ((REG>>BIT)&1)

def TOG_BIT(REG,BIT):
    return REG ^ (1<<BIT)


REG = 0xF0

print(REG)
REG = SET_BIT(REG,0)
print("SET",REG)
REG = CLR_BIT(REG,7)
print("CLR",REG)
print("GET",GET_BIT(REG,4))
print("GET",GET_BIT(REG,3))
REG = TOG_BIT(REG,2)
print("TOG",REG)





