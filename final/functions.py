import main

def process_values(x_array,y_array) :
	x_res = np.array([0,[]])
	y_res = np.array([0,[]])
	for i in range(horizontal_led) :
		if  x_array[i] < threshold and 
			x_array[i] < x_array[i+1] and 
			x_array[i] < x_array[i-1] :
			x_res[0] += 1
			np.append(x_res[1],i)
	for i in range(vertical_led) :
		if  y_array[i] < threshold and 
			y_array[i] < y_array[i+1] and 
			y_array[i] < y_array[i-1] :
			y_res[0] += 1
			np.append(y_res[1],i)
			#change this condition, to something better
	if x_res[0] == 0 and y_res[0] == 0 :
		return 0, []

	elif x_res[0] == 1 and y_res[0] == 1 :
		return 1 , x_res[1], y_res[1]

	elif x_res[0] == 2 and y_res[0] == 2 :
		return 2 , x_res[1], y_res[1]

	elif x_res[0] == 2 and y_res[0] == 1 :
		return 2, x_res[1], np.array([y_res[1],y_res[1]])

	elif x_res[0] == 1 and y_res[0] == 2 :
		return 2, np.array([x_res[1],x_res[1]]), y_res[1]

	elif x_res[0] == 3 or y_res[0] == 3 :
		return 3, x_res[1], y_res[1]

	else :
	 	return 0 , []

def do_click(count) :
	# do this either for x or y, it's fine
	# y array is smaller
	if memory_array_y[count-1] == False or memory_array_y[count-2] == False :
		mouse.click(Button.left, 1)

def do_doubleclick(count) :
	truth_val = 0
	for i in range(no_of_prev_measurements) :
		if memory_array_y[count-i-1] == False and not memory_array_y[count-i-2] == False :
			mouse.click(Button.left,2)

def do_rightclick(count) :
	truth_val = 0
	#for i in range(2*no_of_prev_measurements) :
	#	if memory_array_y[count-i] == False :
	#		truth_val += 1
	#if truth_val < 3 :
	for i in range(2*no_of_prev_measurements) :
		if memory_array_y[count-i-1] == False :
			truth_val+= 1

	if truth_val == 2*no_of_prev_measurements :	
		mouse.click(Button.right, 1)

def drag(count, key) :
	truth_val

def pinch_zoom(key) : 
	if key == 'out' :
		pyautogui.hotkey('cmd','-') 
	elif key == 'in' :
		pyautogui.hotkey('cmd','+')


def do_scroll(count,key) :
	if key == 'up' :
		mouse.scroll(0,scrolling_factor)
	if key == 'down' :
		mouse.scroll(0,-scrolling_factor)
	if key == 'left' :
		mouse.scroll(scrolling_factor,0)
	if key == 'right' :
		mouse.scroll(-scrolling_factor,0)

def collection_without_normalisation() :

    arduinoString_x = arduinoData.readline()
    volt_x = np.array([float(x) for x in arduinoString_x.split()])

    arduinoString_y = arduinoData.readline()
    volt_y = np.array([float(y) for y in arduinoString_y.split()])

    return np.array([volt_x,volt_y])

def collection_with_normalisation() :

    arduinoString_x = arduinoData.readline()
    volt_x = np.array([1.0/float(x) for x in arduinoString_x.split()])

    arduinoString_y = arduinoData.readline()
    volt_y = np.array([1.0/float(y) for y in arduinoString_y.split()])

    return np.array([volt_x,volt_y])

def nearby_collected(collected_values,extent,pos) : # given 1d array it returns array +- 5 elements

	x_ans = np.array([])
	low = pos - extent

	while x-extent >= 0 and x+extent < screen_width :
		np.append(x_ans, collected_values[0][])

def scale_values (reference_array):

    volt_x = np.array([1.0/x for x in reference_array[0]])
    volt_y = np.array([1.0/y for y in reference_array[1]])
	return np.array([volt_x,volt_y])

def nearest_led_number (x,y) :
	return screen_width*x/horizontal_led , screen_height*y/vertical_led

def almost_equal(x,y) :
	if abs(x-y) < allowed_pixels :
		return True
	return False

def swipe(key) :
	if key == 'left' :
		pyautogui.hotkey('ctrl','right')
	elif key == 'right' :
		pyautogui.hotkey('ctrl','left')
	elif key == 'up' :
		pyautogui.hotkey('ctrl','down')
	elif key == 'down' :
		pyautogui.hotkey('ctrl','up')

def distance_between_fingers(count) :
	ans = 0
	try :
		ans =(memory_array_x[count][0] - memory_array_x[count][1])**0.5  + (memory_array_y[count][0] - memory_array_y[count][1])**0.5
	except :
		pass
	return ans


def find_key(count,index) :
	# will return either left or right, returns the values who have greater difference
	x = 0
	y = 0
	x1 = memory_array_x[count-1][index]
	x1 = memory_array_y[count-1][index]
	x0 = memory_array_x[count][index]
	y0 = memory_array_y[count][index]
	try :
		if len(memory_array_x[count-1]) == 2:
			if x1 > x0 :
				x = 'left'
			elif x1 < x0 :
				x = 'right'
			if y1 > y0 :
				y = 'down'
			elif y1 < y0 :
				y = 'up'
	except :
		pass
	if abs(x1-x0) > abs(y1-y0) :
		return x
	else :
		return y

def min_index (dataset) :
	return dataset.index(min(dataset))

def nearest_led_number(x,y) :
		return min_index(collected[0]), min_index(collected[1])

