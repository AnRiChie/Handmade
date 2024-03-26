import matplotlib.pyplot as pip
with open('potential.xvg', 'r') as op:
    read = op.readlines()
i = 0    
read = [i.strip().split() for i in read]
print(read[1])
on = [int(i[0][:-7]) for i in read]
read = [float(i[1]) for i in read]
pip.plot(read, on)
pip.show()