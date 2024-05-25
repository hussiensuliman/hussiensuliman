l1=['HTTP','HTTPS','FTP','DNS']
l2=[80,443,21,53]
d={K:V for (K,V) in zip(l1,l2)}
print (d)