def compute(x1:int = 3, x2: int = 5, limit: int = 10):
    return sum(
        set(
            [i for i in range(limit) 
             if i%x1==0 or i%x2==0]
        )
    )

if __name__ == "__main__":
    print(compute(limit=1000))
