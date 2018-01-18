import jieba

def get_output_str(input_str = ""):
	return str(string_to_list(input_str))

def string_to_list(input_str = ""):
	return (list)(jieba.cut(input_str))

if __name__ == "__main__":
	get_output_str()
