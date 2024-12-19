# callback functions are a powerful concept where a function is passed as an argument to another function, allowing it to be executed after the parent function completes its task.
# This is especially useful for event-driven programming and asynchronous tasks.

def callback(a, b):
    print(f'Sum = {a+b}')

def main(callback):
    print('Add any two digits.')
    if callback != None:
        callback

main(callback(1, 2))

