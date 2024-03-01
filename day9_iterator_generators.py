# Iterables ? minimum requirement to be an iterable -> __iter__ (does not have __next__)
# | Loop it many times | Which can be looped: List

# Iterator? minimum requirement to be an iterator -> __next__
# | Can only be looped once | Memory


def main():
    nums = [5, 10, 20]
    # prints all methods possible
    print(dir(nums))

    # Can loop list many times no problem
    # for n in nums:
    #     print(n)
    # for n in nums:
    #     print(n)

    # Now it's an iterator (LAZY EXECUTION)
    # nums_iter = nums.__iter__() # converts to Iterator! | Iterable -> Iterator!
    nums_iter = iter(nums)  # preferred syntax
    print(nums_iter)  # <list_iterator object at 0x03051400>
    print(
        dir(nums_iter)
    )  # Both functions are available in Iterator -> __next__ & __iter__
    # Conclusion: All Iterators are Iterables | But not the other way around!

    # can get values of iterator
    print(next(nums_iter))
    print(next(nums_iter))
    print(next(nums_iter))
    # exhasusted the iterator
    # print(next(nums_iter)) # error since you can only loop through it once (StopIteration)

    # Looping with Iterators!!!!!!!!!!!!!!!!!!!
    # Create an Iterator and loop it with while loop
    print("New numbers")
    numbers = [10, 20, 30]
    numbers_iter = iter(numbers)
    # try:
    #     while True:
    #         print(next(numbers_iter))
    # except StopIteration as e:
    #     print("Cannot go any further than this :)", e)
    # OR
    while True:
        try:
            print(next(numbers_iter))
        except StopIteration as e:
            print("Cannot go any further than this :)", e)
            break

    # range does not hold all values in memory. It just gives you next value as you go
    # List holds all values in memory
    # Iterator remembers one thing at a time | save memory
    # range(0, 100_000_000, 1) #100 million values
    # Iterator version
    # __next__ & __iter__ -> defines an iterator
    # count values, start and end and skip with one


# to create your own iterator you need "__iter__" and "__next__" dunder methods
class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # already an iterator so it returns self! ("__iter__" converts to an iterator)
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1


# Generator - clean | infinite_integers() -> iterator
# LAZY EXECUTION
# can do infinite values, pauses execution with each yield until next "next()" is called
def infinite_integers():
    n = 0
    while True:  # 3. then back to yield because of while condition
        # Generator syntax - lazy
        yield n  # 1. yield -> execution pauses here (it knows when to exit with function)
        n += 1  # 2. only goes here when next "next" is called


if __name__ == "__main__":
    # main()
    # # Example of using iterator for looping
    # for n in MyRange(1, 5):
    #     print(n)
    # integers is an iterator as it has the "next" method
    integers = infinite_integers()
    print(next(integers))  # 0
    print(next(integers))  # 1
    # print(next(integers))

    def fib1(limit):
        a = 0
        b = 1
        while a < limit:
            yield a
            c = a + b
            a = b
            b = c
            # or
            # a, b = b, a + b

    def fib2(limit):
        a = 0
        b = 1
        i = 0
        while i < limit:
            yield a
            c = a + b
            a = b
            b = c
            i += 1

    # fib - generator function
    print("Fibonacci Ting 1")
    for num in fib1(10):
        print(num)
    # Output
    # 0 1 1 2 3 5 8
    print("Fibonacci Ting 2")
    for num in fib2(10):
        print(num)
    # Output
    # 0 1 1 2 3 5 8 13 21 34
