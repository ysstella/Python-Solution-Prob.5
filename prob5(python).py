import matplotlib.pylab as plot
import numpy as np

n=np.linspace(0,199,200) ; y=np.linspace(0,199,200)   
  
x=eval((input("Write an equation for x(n):")))
i=0
while i in range(0,200):
    if i==199:
        y[i]=(1.5*x[i])-(2*x[i-1])+(0.5*x[i-2])
    elif i==0:
        y[i]=(-1.5*x[i])+(2*x[i+1])-(0.5*x[i+2])
    else:
        y[i]= (0.5*x[i+1])-(0.5*x[i-1])
    i+=1
    
plot.plot(x,color="g")
plot.plot(y,color="r")
plot.suptitle('piecewise of f(n)')
plot.xlabel('n=0 to n=199')
plot.legend(['x(n) Value', 'y(n) Value'],loc=1)
plot.show