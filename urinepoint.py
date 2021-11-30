def getlist(list, point):
    
    #2021-10-19-1
    if point=='2021-10-19-1-p1':
        urinelist = list[0][1:9]+list[1][1:10]+list[2][2:7]+list[3][4:8]+list[4][5:8]
    elif point=='2021-10-19-1-p2':
        urinelist = list[9][5:7]+list[10][3:7]+list[11][4:7]
    elif point=='2021-10-19-1-p3':
        urinelist = list[14][1:6]+list[15][1:6]
    elif point=='2021-10-19-1-p4':
        urinelist = list[17][2:5]+list[18][2:7]+list[19][5:7]
    
    #2021-10-19-2
    elif point=='2021-10-19-2-p1':
        urinelist = list[1][5:9]
    elif point=='2021-10-19-2-p2':
        urinelist = list[2][3:7]+list[3][2:9]+list[4][2:9]+list[5][4:8]
    elif point=='2021-10-19-2-p3':
        urinelist = list[6][5:8]+list[7][4:8]
    elif point=='2021-10-19-2-p4':
        urinelist = list[9][1:6]+list[10][1:8]+list[11][1:7]+list[12][4:7]
    elif point=='2021-10-19-2-p5':
        urinelist = list[15][0:8]+list[16][0:9]+list[17][0:9]+list[18][0:7]+list[19][1:6]+list[20][2:6]
    
    #2021-10-20
    elif point=='2021-10-20-p1':
        urinelist = list[0][3:10]+list[1][2:10]+list[2][1:10]+list[3][1:10]+list[4][2:10]
    elif point=='2021-10-20-p2':
        urinelist = list[20][0:5]+list[21][0:8]+list[22][0:10]+list[23][0:10]+list[24][0:10]
        
    #2021-10-20
    elif point=='2021-10-20-p1':
        urinelist = list[0][3:10]+list[1][2:10]+list[2][1:10]+list[3][1:10]+list[4][2:10]
    elif point=='2021-10-20-p2':
        urinelist = list[20][0:5]+list[21][0:8]+list[22][0:10]+list[23][0:10]+list[24][0:10]
    
    #2021-10-20
    elif point=='2021-10-22-p1':
        urinelist = list[0][5:7]+list[1][3:9]+list[2][1:9]+list[3][1:10]+list[4][2:9]
    elif point=='2021-10-22-p2':
        urinelist = list[17][4:6]+list[18][4:6]+list[19][0:7]+list[20][0:5]+list[21][0:7]+\
                    list[22][0:7]+list[23][2:4]
    
    return urinelist