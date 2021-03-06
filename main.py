def load_data(file_name):
	with open("input_data/" + file_name) as file:
		data = file.read()
	M = int(data.split()[0])
	N = int(data.split()[1])
	pizza_types = list(map(int, data.split()[2:]))
	return M, N, pizza_types


def save_data(file_name, data):
	with open("output_data/" + file_name.split('.')[0] + ".out", 'w') as file:
		file.write(data)


def find_solution(M, N, pizza_types):
	total_slices = 0
	solution = []
	solution_found = False
	for i in range(0, N): # add pizza one by one - and count total_slices
		if solution_found:
			break
		current_slices = 0
		temp_solution = []
		for j in range(i, -1, -1):
			temp_slices = current_slices + pizza_types[j]
			if temp_slices == M:
				current_slices = temp_slices
				temp_solution.insert(0, j)
				solution_found = True
				break
			elif temp_slices > M:
				continue
			elif temp_slices < M:
				current_slices = temp_slices
				temp_solution.insert(0, j)
				continue
		if total_slices < current_slices:
			total_slices = current_slices
			solution = temp_solution
	return solution


def process_file(file_name):
	M, N, pizza_types = load_data(file_name)
	solution = find_solution(M, N, pizza_types)
	K = len(solution) # the number of dierent types of pizza to order
	pizza_types_to_order = ' '.join(str(i) for i in solution) # which pizzas to order
	output_solution = f"{K}\n{pizza_types_to_order}"
	save_data(file_name, output_solution)


if __name__ == "__main__":
	files = ["a_example.in", "b_small.in", "c_medium.in", "d_quite_big.in", "e_also_big.in"]
	for file_name in files:
		process_file(file_name)

