import collections

s = "the quick brown fox jumped over the little moon"


s = s.lower()
letters = collections.Counter(s)
most_common = letters.most_common()
# Remove spaces from char freq calculations
most_common = [i for i in most_common if i[0] != ' ']
mc_array = []
for k,v in most_common:
    if k != ' ':
        k = k.lower()
        mc_array.append(k)
	#print mc_array
topfivestring = str(mc_array[0]+mc_array[1]+mc_array[2]+mc_array[3]+mc_array[4]+mc_array[5]+mc_array[6]+mc_array[7]+mc_array[8]+mc_array[9]+mc_array[10])

score = 0

if 'e' in topfivestring:
    score += 1
if 'a' in topfivestring:
    score += 1
if 't' in topfivestring:
    score += 1
if 'o' in topfivestring:
    score += 1
if 'n' in topfivestring:
    score += 1
if 'i' in topfivestring:
    score += 1

etaoinpass = False
if score >= 4:
	etaoinpass = True

if etaoinpass == True:
	if topfivestring[0] == 'e':
		score += 2

return score


'''
def calc_str_score(s):
	# Count total letter in input string
	s = s.lower()
	letters = collections.Counter(s)
	most_common = letters.most_common()
	mc_array = []
	for k,v in most_common:
	    if k != ' ':
	        k = k.lower()
	        mc_array.append(k)
	#print mc_array

	topfivestring = str(mc_array[0]+mc_array[1]+mc_array[2]+mc_array[3]+mc_array[4]+mc_array[5]+mc_array[6]+mc_array[7]+mc_array[8]+mc_array[9]+mc_array[10])

	#print topfivestring

	score = 0

	if 'e' in topfivestring:
	    score += 1
	if 'a' in topfivestring:
	    score += 1
	if 't' in topfivestring:
	    score += 1
	if 'o' in topfivestring:
	    score += 1
	if 'n' in topfivestring:
	    score += 1
	if 'i' in topfivestring:
	    score += 1

	return score
'''