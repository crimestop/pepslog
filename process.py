import analysis
import sys
import time

files = sys.stdin.read().split()
filedata=[open(f,'r').read()for f in files]
title=analysis.get_title(filedata[1])
results=map(analysis.analysis ,filedata)
results=sum(results, [])
results=analysis.masage(results,5,0.002)
results=analysis.masage(results,5,0.00018)
ene=[x[0] for x in results]
ene_sm=analysis.smear(analysis.smear(ene,10),10)
diff=analysis.locate_diff(results)

if len(sys.argv)>1:
	option = sys.argv[1]
else:
	option = 'pyplot'

if option=='pyplot':
	import plot_pyplot
	import matplotlib.pyplot as plt  
	plot_pyplot.plot(ene,ene_sm,diff,title)
	plt.show()
elif option=='android':
	import plot_plotly
	fig = plot_plotly.plot(ene,ene_sm,diff,title)
	fig.show(renderer='iframe')
	#fig.write_image("fig.pdf", width=1200, height=700)
elif option=='plotly':
	import plot_plotly
	fig = plot_plotly.plot(ene,ene_sm,diff,title)
	fig.show()
	#fig.write_image("fig.pdf", width=1200, height=700)
else:
	print('Option is invalid.')
