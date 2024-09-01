m = float(input('\n P:Digite uma mediação em metros: '))
mili = m*1000
cm = m*100
dm = m*10
dam = m*(1/10)
hm = m*(1/100)
km = m*(1/1000)
print('\nR: {} metros é o equivalente à: \n{:.0f}mm \n{:.0f}cm \n{:.0f}dm \n{:.1f}dam \n{:.2f}hm \n{:.3f}km \nEND'.format(m, mili, cm, dm, dam, hm, km))




