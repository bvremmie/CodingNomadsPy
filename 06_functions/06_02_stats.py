'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(input_list):
  maxL = max(input_list)
  minL = min(input_list)
  avgL = sum(input_list) / len(input_list)
  sumL = sum(input_list)
  state = print(f"Max: {maxL}, Min: {minL}, Average: {avgL}, Sum: {sumL}")
  return state
  pass
# call the function below here

list_stats = stats(example_list)
print(list_stats)