def getsensorlist(listin):
    sensorlist = [
        [listin[7]   ,listin[6]   ,listin[5]   ,listin[4]   ,listin[3]   ,listin[2]   ,listin[1]   ,listin[0]   ,listin[11]  ,listin[10]]  , #1
        [listin[9]  ,listin[8]   ,listin[12]  ,listin[13]  ,listin[14]  ,listin[15]  ,listin[23]  ,listin[22]  ,listin[21]  ,listin[20]]  , #2
        [listin[16]  ,listin[17]  ,listin[18]  ,listin[19]  ,listin[24]  ,listin[25]  ,listin[26]  ,listin[27]  ,listin[28]  ,listin[29]]  ,    #3
        [listin[30]  ,listin[31]  ,listin[39]  ,listin[38]  ,listin[37]  ,listin[36]  ,listin[35]  ,listin[34]  ,listin[33]  ,listin[32]]  ,    #4
        [listin[40]  ,listin[41]  ,listin[42]  ,listin[43]  ,listin[44]  ,listin[45]  ,listin[46]  ,listin[47]  ,listin[55]  ,listin[54]]  ,    #5
        [listin[53]  ,listin[52]  ,listin[51]  ,listin[50]  ,listin[49]  ,listin[48]  ,listin[56]  ,listin[57]  ,listin[58]  ,listin[59]]  ,    #6 
        [listin[60]  ,listin[61]  ,listin[62]  ,listin[63]  ,listin[71]  ,listin[70]  ,listin[69]  ,listin[68]  ,listin[67]  ,listin[66]]  ,    #7
        [listin[65]  ,listin[64]  ,listin[72]  ,listin[73]  ,listin[74]  ,listin[75]  ,listin[76]  ,listin[77]  ,listin[78]  ,listin[79]]  ,    #8
        [listin[87]  ,listin[86]  ,listin[85]  ,listin[84]  ,listin[83]  ,listin[82]  ,listin[81]  ,listin[80]  ,listin[88]  ,listin[89]]  ,    #9
        [listin[90]  ,listin[91]  ,listin[92]  ,listin[93]  ,listin[94]  ,listin[95]  ,listin[103] ,listin[102] ,listin[101] ,listin[100]] ,    #10
        [listin[99]  ,listin[98]  ,listin[97]  ,listin[96]  ,listin[104] ,listin[105] ,listin[106] ,listin[107] ,listin[108] ,listin[109]] ,    #11
        [listin[110] ,listin[111] ,listin[119] ,listin[118] ,listin[117] ,listin[116] ,listin[115] ,listin[114] ,listin[113] ,listin[112]] ,    #12
        [listin[120] ,listin[121] ,listin[122] ,listin[123] ,listin[124] ,listin[125] ,listin[126] ,listin[127] ,listin[135] ,listin[134]] ,    #13
        [listin[133] ,listin[132] ,listin[131] ,listin[130] ,listin[129] ,listin[128] ,listin[136] ,listin[137] ,listin[138] ,listin[139]] ,    #14
        [listin[140] ,listin[141] ,listin[142] ,listin[143] ,listin[151] ,listin[150] ,listin[149] ,listin[148] ,listin[147] ,listin[146]] ,    #15
        [listin[145] ,listin[144] ,listin[152] ,listin[153] ,listin[154] ,listin[155] ,listin[156] ,listin[157] ,listin[158] ,listin[159]] ,    #16
        [listin[167] ,listin[166] ,listin[165] ,listin[164] ,listin[163] ,listin[162] ,listin[161] ,listin[160] ,listin[168] ,listin[169]] ,    #17
        [listin[170] ,listin[171] ,listin[172] ,listin[173] ,listin[174] ,listin[175] ,listin[183] ,listin[182] ,listin[181] ,listin[180]] ,    #18
        [listin[179] ,listin[178] ,listin[177] ,listin[176] ,listin[184] ,listin[185] ,listin[186] ,listin[187] ,listin[188] ,listin[189]] ,    #19
        [listin[190] ,listin[191] ,listin[199] ,listin[198] ,listin[197] ,listin[196] ,listin[195] ,listin[194] ,listin[193] ,listin[192]] ,    #20
        [listin[200] ,listin[201] ,listin[202] ,listin[203] ,listin[204] ,listin[205] ,listin[206] ,listin[207] ,listin[215] ,listin[214]] ,    #21
        [listin[213] ,listin[212] ,listin[211] ,listin[210] ,listin[209] ,listin[208] ,listin[216] ,listin[217] ,listin[218] ,listin[219]] ,    #22
        [listin[220] ,listin[221] ,listin[222] ,listin[223] ,listin[231] ,listin[230] ,listin[229] ,listin[228] ,listin[227] ,listin[226]] ,    #23
        [listin[225] ,listin[224] ,listin[232] ,listin[233] ,listin[234] ,listin[235] ,listin[236] ,listin[237] ,listin[238] ,listin[239]] ,    #24
        [listin[247] ,listin[246] ,listin[245] ,listin[244] ,listin[243] ,listin[242] ,listin[241] ,listin[240] ,listin[248] ,listin[249]]]     #25
    return sensorlist
def get_one_dim(listin):
    sensorlist=[[listin[247] ,listin[246] ,listin[245] ,listin[244] ,listin[243] ,listin[242] ,listin[241] ,listin[240] ,listin[248] ,listin[249]],
    [listin[225] ,listin[224] ,listin[232] ,listin[233] ,listin[234] ,listin[235] ,listin[236] ,listin[237] ,listin[238] ,listin[239]],
    [listin[220] ,listin[221] ,listin[222] ,listin[223] ,listin[231] ,listin[230] ,listin[229] ,listin[228] ,listin[227] ,listin[226]],
    [listin[213] ,listin[212] ,listin[211] ,listin[210] ,listin[209] ,listin[208] ,listin[216] ,listin[217] ,listin[218] ,listin[219]],
    [listin[200] ,listin[201] ,listin[202] ,listin[203] ,listin[204] ,listin[205] ,listin[206] ,listin[207] ,listin[215] ,listin[214]],
    [listin[190] ,listin[191] ,listin[199] ,listin[198] ,listin[197] ,listin[196] ,listin[195] ,listin[194] ,listin[193] ,listin[192]],
    [listin[179] ,listin[178] ,listin[177] ,listin[176] ,listin[184] ,listin[185] ,listin[186] ,listin[187] ,listin[188] ,listin[189]],
    [listin[170] ,listin[171] ,listin[172] ,listin[173] ,listin[174] ,listin[175] ,listin[183] ,listin[182] ,listin[181] ,listin[180]],
    [listin[167] ,listin[166] ,listin[165] ,listin[164] ,listin[163] ,listin[162] ,listin[161] ,listin[160] ,listin[168] ,listin[169]],
    [listin[145] ,listin[144] ,listin[152] ,listin[153] ,listin[154] ,listin[155] ,listin[156] ,listin[157] ,listin[158] ,listin[159]],
    [listin[140] ,listin[141] ,listin[142] ,listin[143] ,listin[151] ,listin[150] ,listin[149] ,listin[148] ,listin[147] ,listin[146]],
    [listin[133] ,listin[132] ,listin[131] ,listin[130] ,listin[129] ,listin[128] ,listin[136] ,listin[137] ,listin[138] ,listin[139]],
    [listin[120] ,listin[121] ,listin[122] ,listin[123] ,listin[124] ,listin[125] ,listin[126] ,listin[127] ,listin[135] ,listin[134]],
    [listin[110] ,listin[111] ,listin[119] ,listin[118] ,listin[117] ,listin[116] ,listin[115] ,listin[114] ,listin[113] ,listin[112]],
    [listin[99] ,listin[98]  ,listin[97]  ,listin[96]  ,listin[104] ,listin[105] ,listin[106] ,listin[107] ,listin[108] ,listin[109]],
    [listin[90]  ,listin[91]  ,listin[92]  ,listin[93]  ,listin[94]  ,listin[95]  ,listin[103] ,listin[102] ,listin[101] ,listin[100]],
    [listin[87]  ,listin[86]  ,listin[85]  ,listin[84]  ,listin[83]  ,listin[82]  ,listin[81]  ,listin[80]  ,listin[88]  ,listin[89]],
    [listin[65]  ,listin[64]  ,listin[72]  ,listin[73]  ,listin[74]  ,listin[75]  ,listin[76]  ,listin[77]  ,listin[78]  ,listin[79]],
    [listin[60]  ,listin[61]  ,listin[62]  ,listin[63]  ,listin[71]  ,listin[70]  ,listin[69]  ,listin[68]  ,listin[67]  ,listin[66]],
    [listin[53]  ,listin[52]  ,listin[51]  ,listin[50]  ,listin[49]  ,listin[48]  ,listin[56]  ,listin[57]  ,listin[58]  ,listin[59]],
    [listin[40]  ,listin[41]  ,listin[42]  ,listin[43]  ,listin[44]  ,listin[45]  ,listin[46]  ,listin[47]  ,listin[55]  ,listin[54]],
    [listin[30]  ,listin[31]  ,listin[39]  ,listin[38]  ,listin[37]  ,listin[36]  ,listin[35]  ,listin[34]  ,listin[33]  ,listin[32]],
    [listin[16]  ,listin[17]  ,listin[18]  ,listin[19]  ,listin[24]  ,listin[25]  ,listin[26]  ,listin[27]  ,listin[28]  ,listin[29]],
    [listin[9]  ,listin[8]   ,listin[12]  ,listin[13]  ,listin[14]  ,listin[15]  ,listin[23]  ,listin[22]  ,listin[21]  ,listin[20]],
    [listin[7]   ,listin[6]   ,listin[5]   ,listin[4]   ,listin[3]   ,listin[2]   ,listin[1]   ,listin[0]   ,listin[11]  ,listin[10]]]
    return sensorlist