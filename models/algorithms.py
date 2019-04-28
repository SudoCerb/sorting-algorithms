import time

# bubble sort
def bubble(input):
    # copy input
    source = input.copy()
    unordered = True
    start = time.time()
    cycles = 0
    while unordered:
        swap_count = 0
        # scan through the array
        for i in range(len(source) - cycles - 1):
            if source[i] > source[i+1]:
                swap = source[i+1]
                source[i+1] = source[i]
                source[i] = swap
                swap_count += 1
        if swap_count == 0:
            unordered = False
        cycles += 1
    end = time.time()
    # print(source)
    print('Bubble sort completed in {}'.format(end-start))

def selection(input):
    source = input.copy()
    unordered = True
    cycles = 0
    start = time.time()
    while unordered and cycles < len(source):
        swap_count = 0
        # for i in range(cycles, len(source) - 1):
        # find minimum and swap i with min's position
        min_index = source.index(min(source[cycles:])) # this is the index of the min value
        swap = source[cycles]
        source[cycles] = source[min_index]
        source[min_index] = swap
        cycles += 1


    end = time.time()
    # print(source)
    print('Selection sort completed in {}'.format(end - start))

def insertion(input):
    source = input.copy()
    cycles = 0
    start = time.time()
    while cycles < len(source):
        element = source[cycles]
        tgtIndex = cycles
        for i in reversed(range(cycles)):
            if element < source[i]:
                tgtIndex -= 1
            else:
                break
        source.pop(cycles)
        source.insert(tgtIndex, element)
        cycles += 1
    end = time.time()
    # print(source)
    print('Insertion sort completed in {}'.format(end - start))

def heap(input):
    # create binary tree in array

    # extract values from the heap and rebuild

    # accept
    def build(input):
        pass