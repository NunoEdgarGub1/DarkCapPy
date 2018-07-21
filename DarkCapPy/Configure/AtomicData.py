########################
# Atomic Data 
########################
elementList = [
    'O16' ,
#     'Na23', No data for this
    'Mg24',
    'Al27',
    'Si28',
    'P31' ,
    'S32' ,
    'Ca40',
    'Cr52',
    'Fe56',
    'Ni58'
]

atomicNumbers = {
    'O16' :16.,
    'Na23':23.,
    'Mg24':24., # 78%
    'Al27':27.,
    'Si28':28.,
    'P31' :30.,
    'S32' :32.,
    'Ca40':40.,
    'Cr52':52., # 83%
    'Fe56':56.,
    'Ni58':59., # 58%
}

nProtons = {
    'O16' :8.,
    'Na23':11.,
    'Mg24':12., # 78%
    'Al27':13.,
    'Si28':14.,
    'P31' :15.,
    'S32' :16.,
    'Ca40':20.,
    'Cr52':24., # 83%
    'Fe56':26.,
    'Ni58':28., # 58%
}

coreMassFrac = {
    'O16' : 0.0,
    'Na23': 0.0,
    'Mg24': 0.0,
    'Al27': 0.0,
    'Si28': 0.06,
    'P31' : 0.002,
    'S32' : 0.019,
    'Ca40': 0.0,
    'Cr52': 0.009,
    'Fe56': 0.855,
    'Ni58': 0.052,
}


mantleMassFrac = {
    'O16' : 0.440,
    'Na23': 0.0027,
    'Mg24': 0.228,
    'Al27': 0.0235,
    'Si28': 0.210,
    'P31' : 0.00009,
    'S32' : 0.00025,
    'Ca40': 0.0253,
    'Cr52': 0.0026,
    'Fe56': 0.0626,
    'Ni58': 0.00196,
}
