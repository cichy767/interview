import typing


class AbstractBatcher:
    size: int = 0

    def batch(self, values: typing.Iterable) -> typing.Generator:
        l = []
        for value in values:
            l.append(value)
            if self.size == len(l):
                print(l)
                yield l
                l = []
        if l:
            print(l)
            yield l

            # print(value[size])


class ConcreteBatcher2(AbstractBatcher):
    size: int = 2


class ConcreteBatcher3(AbstractBatcher):
    size: int = 3


class Processor:

    def __init__(self, *args, **kwargs) -> None:
        self.batcher = kwargs['batcher']

    def execute(self, values: typing.Iterable) -> typing.List:
        return list(self.batcher.batch(values))


# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [[1,2], [3,4], [5,6], [7,8], [9,10]]

# Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: [[1,2, 3], [4, 5, 6], [7,8, 9], [10]]

foo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

ab_2 = ConcreteBatcher2()
ab_3 = ConcreteBatcher3()
# for x in ab.batch(foo):
#    print(x)


# procesor = Processor(batcher=ab_2)
# result = procesor.execute(foo)
# print(result)


# assert Processor(batcher=ab_2).execute(foo) == [[1,2], [3,4], [5,6], [7,8], [9,10]], Processor(batcher=ab_2).execute(foo)
assert Processor(batcher=ab_3).execute(foo) == [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]], Processor(batcher=ab_3).execute(
    foo)



