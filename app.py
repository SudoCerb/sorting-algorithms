from models import generators, algorithms


source_list = generators.generate(20000)
# print(generate(300))

copy = source_list.copy()
algorithms.selection(copy)
algorithms.insertion(copy)
algorithms.bubble(copy)
