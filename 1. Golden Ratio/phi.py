import turtle


PHI: float = 2 / (5 ** 0.5 - 1)

# Complexity
#   Time: O(n)
#   Memory: O(1)
def fibo(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Complexity
#   Time: O(Φ^n)
#   Memory: O(n)
def fibo2(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibo2(n - 1) + fibo2(n - 2)


def print_fibo_seq() -> None:
    prev: int = 1
    for i in range(1, 100):
        x: int = fibo(i)
        print(f'{i:4} = {x} {x/prev}')
        prev = x


def square(size: int) -> None:
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def golden_spiral(n: int) -> None:
    size: float = 5
    for _ in range(n):
        turtle.pencolor('blue')
        square(int(size))
        turtle.pencolor('red')
        turtle.circle(size, 90)
        size *= PHI


if __name__ == '__main__':
    # print_fibo_seq()
    # print(PHI)
    turtle.speed('fastest')
    turtle.hideturtle()
    turtle.pensize(3)
    golden_spiral(9)
    turtle.done()
