def membalikkankata (kata):
    membalik = []
    pembalikkan = len(kata)
    a =1
    while a <= pembalikkan :
        b = a* (-1)
        membalik.append (kata[b])
        a = a+1
    cetak = ''
    for i in range (len(membalik)) :
        cetak += membalik[i]
    return cetak
pembalikkan = (input('masukkan kata atau angka;'))
print ('', membalikkankata(pembalikkan))