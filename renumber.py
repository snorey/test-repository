stuff = "122-126, 219-224,250-269, 300-302,306-314,341-360,386-392,397-403,404-405"

todo2 = "30-31,64-71,157-150, 285-291,101-104,157-160,74-81,112-116, 163-167"
todo3 = "60,152-153,249,339,26-27,271-272,274-277"
todo4 = "324,279-281,34-35, 34-35, 36-37, 37-40, 191"
todo5 = ", 29-30,36, 522-526, 522, 426, 430, 440-442"
todo6 = "55,76, 34-35, 230-231, 139"
todo7 = "325, 325, 337, 68-71"
todo8 = "69-70, 76-78, 230-231, 112, 325, 102-104, 104"
todo9 = "158-160,304,159-160,112-116, 120, 165"
todo10 = "285, 101, 113-116,231, 185-186"
todo11 = "166, 178"

these = [todo2,todo3,todo4,todo5,todo6,todo7,todo8,todo9,todo10,todo11]

def render_todos(todo):
	items = decomma(todo)
	output = []
	for i in items:
		if not i:
			continue
		if "-" not in i:
			output.append(int(i))
		else:
			newitem = map(int,i.split("-",2))
			output.append(tuple(newitem))
	return output


def renumber_todos(todo):
	todo = render_todos(todo)
	print str(todo)
	renumbered = []
	elisions = tuplify(stuff)
	for t in todo:
		if type(t) == int:
			renumbered.append(renumber(t,elisions))
		elif type(t) == tuple:
			this = []
			for tt in t:
				this.append(renumber(tt,elisions))
			renumbered.append(tuple(this))
		else:
			print t
			raise ValueError
	return renumbered


def decomma(commastring):
	items = commastring.split(",")
	items = map(lambda x: x.strip(),items)
	return items


def tuplify(commas_and_dashes):
	items = decomma(commas_and_dashes)
	elisions = []
	for i in items:
		if not i:
			continue
		elision = map(int,i.split("-",2))
		if len(elision) > 1:
			elisions.append(tuple(elision))
		else:
			elisions.append((elision,elision))
	return elisions


def get_length(elision):
	elision_length = (elision[1] - elision[0]) + 1
	return elision_length


def summate(elisions):
	total = 0
	for e in elisions:
		length = get_length(e)
		if length < 1:
			raise ValueError
		total += length
	return total


def renumber(index,elisions): # where elisions is list of tuples of pages removed
	newdex = index
	for e in elisions:
		if index < e[0]:
			continue
		elif e[0] <= index <= e[1]:
			return "!!!"
		else:
			newdex = newdex - get_length(e)
	return newdex

