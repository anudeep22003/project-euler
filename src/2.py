def fibbonacci_generator(limit:int = 100):
    fib_sequence = [1]
    while fib_sequence[-1]<limit:
        if len(fib_sequence)>1:
            fib_sequence.append(sum(fib_sequence[-2:]))
        else:
            fib_sequence.append(2)
    return fib_sequence

def compute(limit: int = 4E6):
    fib_seq = fibbonacci_generator(limit)
    return sum(
        [ix for ix in fib_seq 
         if ix%2==0]
    )

if __name__ == "__main__":
    print(compute())
