import pyhop


# operators

def check_tool(state, elem):
	#print("check_tool" + elem)
	if state.tool[elem]:
		return state
	return False 

def check_ingredients(state, elem, num):
	#print("check_ingredient" + elem + str(num))
	if state.ingredients[elem] < num:
		return state
	return False	

def use_ingredient(state, elem, num):
	#print("use_ingredient" + elem + str(num))
	state.ingredients[elem] -= num
	return state

def use_time(state, num):
	if state.time >= num:
		state.time -= num
		return state
	else: return False

def store_ingredient(state, elem, num):
	#print("store_ingredient" + elem + str(num))
	state.ingredients[elem] += num
	return state

def store_tool(state, tool):
	state.tool[tool] = True
	return state

pyhop.declare_operators(check_tool, check_ingredients, use_ingredient, store_ingredient, use_time)



# mehtods

def wooden_axe_for_wood(state, num):
	#print("wooden_axe for wood")
	if state.time >= 1:
		state.time -= 1
		return[('check_ingredients', 'wood', num), ('check_tool', 'wooden_axe'), ('store_ingredient', 'wood', 1)]	
	else: return False

def stone_axe_for_wood(state, num):
	#print("stone_axe for wood")
	if state.time >= 1:
		state.time -= 1
		return[('check_ingredients', 'wood', num), ('check_tool', 'stone_axe'), ('store_ingredient', 'wood', 1)]	
	else: return False


def iron_axe_for_wood(state, num):
	#print("iron_axe for wood")
	if state.time >= 1:
		state.time -= 1
		return[('check_ingredients', 'wood', num), ('check_tool', 'iron_axe'), ('store_ingredient', 'wood', 1)]	
	else: return False


def punch_for_wood(state, num):
	if state.time >= 4:
		if num == 1:
			return [('store_ingredient', 'wood', 1), ('use_time', 4)]
		else:
			return [('store_ingredient', 'wood', 1), ('use_time', 4), ('produce_wood', num - 1)]


#pyhop.declare_methods('produce_wood', punch_for_wood, iron_axe_for_wood, stone_axe_for_wood, wooden_axe_for_wood)
pyhop.declare_methods('produce_wood', punch_for_wood)




# state init

state = pyhop.State('state1')
state.ingredients = {'wood' : 0, 'plank' : 0, 'cobble' : 0, 'ingot' : 0, 'coal' : 0, 'ore' : 0, 'stick' : 0}
state.tool = {'wooden_axe' : True, 'wooden_pickaxe' : False, 'stone_axe' : False, 'stone_pickaxe' : False, 'iron_axe' : False, 'iron_pickaxe' : False}
state.time = 50


if __name__ == '__main__':
	print("starting")
	pyhop.pyhop(state,[('produce_wood', 5)],verbose=1)
	