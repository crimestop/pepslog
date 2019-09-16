import matplotlib.pyplot as plt  
import matplotlib.ticker as tick

def plot(ene,ene_sm,diff,title):
	fig, ax = plt.subplots()
	ax.ticklabel_format(style='plain',axis='x',useOffset=False)
	ax.ticklabel_format(style='plain',axis='y',useOffset=False)
	ax.xaxis.set_major_locator(tick.MaxNLocator(integer=True))
	ax.plot(ene, 'b',label='data')
	#ax.plot(ene2, 'r',label='data with smear '+str(sm))
	ax.plot(ene_sm, 'r',label='data with smear')
	ax.set_xlabel('n')
	ax.set_ylabel('E')
	ax.legend()
	ymin=min(ene)-0.1*(max(ene)-min(ene))
	ymax=max(ene)+0.1*(max(ene)-min(ene))
	ax.set_ylim([ymin,ymax])
	for df in diff:
		if df['pos']>0:
			plt.axvline(x=df['pos'], color='k', linestyle='--')
		plt.text(df['pos'],ymin+0.9*(ymax-ymin),df['info'])
	plt.subplots_adjust(left=0.15)
	plt.title(title)