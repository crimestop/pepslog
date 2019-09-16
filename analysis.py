import re

def integrity(paragraph):
	return not (re.search(r'energy =',paragraph) is None)

def get_value(paragraph,consts):
	ene = re.search(r'energy = ([^ \n]+)',paragraph)
	dt = re.search(r'delta_t = ([^ \n]+),',paragraph)
	return (float(ene.group(1)),float(dt.group(1)))+consts

def get_sampling(paragraph):
	msamp = re.search(r'i  sampling +([^ \n]+)',paragraph)
	samp=int(msamp.group(1))
	mproc = re.search(r'running on ([^ ]+) cores',paragraph)
	proc=int(mproc.group(1))
	return samp*proc

def analysis(filestring):
	data=re.split(r'\d+th step,',filestring)
	sampling = get_sampling(data[0])
	rest=(sampling, )
	if(integrity(data[-1])):
		return [get_value(x,rest) for x in data[1:]]
	else:
		return [get_value(x,rest) for x in data[1:-1]]

def get_title(filestring):
	data=re.split(r'\d+th step,',filestring)
	titl = re.search(r'''SU\ parameters
		.*L1\ +([^ \n]+)
		.*L2\ +([^ \n]+)
		.*lattice\ +([^ \n]+)
		.*model\ +([^ \n]+)
		.*GM\ parameters
		.*D\ +([^ \n]+)''',data[0],re.S|re.X)
	return 'L1='+titl.group(1)+' L2='+titl.group(2)+' D='+titl.group(5)+' Lat='+titl.group(3)+' Mod='+titl.group(4)

def smear(list, n):
	newlist = []
	for i in range(len(list)):
		left = i-n//2
		right=left+n
		left=max(left,0)
		right=min(right,len(list))
		newlist.append(sum(list[left:right])/(right-left))
	return newlist

def masage(results,erange,perc):
	ene=[x[0] for x in results]
	errlist = []
	for i in range(len(ene)):
		left = i-erange
		right=i+erange
		left=max(left,0)
		right=min(right,len(ene))
		errlist.append(abs(((sum(ene[left:i])+sum(ene[i+1:right]))/(right-left-1))/ene[i]-1))
	newlist = [results[i] for i in range(len(results)) if errlist[i]<perc]
	error_num = list(filter(lambda x: x >= perc, errlist))
	print(str(len(error_num))+' items have been masaged')
	return newlist

def locate_diff(results):
	diff=[]
	for i in range(len(results)):
		if i==0 or results[i][1:]!=results[i-1][1:]:
			diff.append({'pos':i, 'info': ' dt '+str(results[i][1])+'\n sp '+str(results[i][2])})
	return diff

if __name__ == '__main__':
	file = open('test.log','r')
	ene = analysis(file.read())
	print(ene)