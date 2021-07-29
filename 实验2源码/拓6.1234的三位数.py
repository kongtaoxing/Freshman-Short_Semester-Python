for i in range(1,5):           #百位数
    for j in range(1,5):              #十位数
        for k in range(1,5):                 #个位数
            if i!=j!=k!=i:            #各位数字不同
                print(100*i+10*j+k)
