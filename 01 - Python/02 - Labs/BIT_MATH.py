def SET_BIT(REG,BIT):
    return REG | (1<<BIT)

def CLR_BIT(REG,BIT):
    return REG & ~(1<<BIT)

def GET_BIT(REG,BIT):
    return ((REG>>BIT)&1)

def TOG_BIT(REG,BIT):
    return REG ^ (1<<BIT)








