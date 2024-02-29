## Filter 
- Always returns a copy of the list
- sourceList.length >= outputList.length
- input data type === output data type E.g.) list [int] -> list[int]

| Iterables?                    | Iterator?                    |
| ----------------------------- | ---------------------------- |
| `__iter__`                    | `__next__` & `__iter__`      |
| Loop it many times            | Loop it one time             |
| But not the other way around  | All Iterator are Iterables   |
| Doest know where I am in loop | They know where I am in loop |
| Lot of Memory                 | Memory efficient             |
| Eager                         | Lazy                         |
 
 
 
| a   | b   | a + b |
| --- | --- | ----- |
| 0   | 1   | 1     |
| 1   | 1   | 2     |
| 1   | 2   | 3     |
| 2   | 3   | 5     |