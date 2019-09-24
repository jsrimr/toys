# co routine next 와 send  close s이용해보기
# sub coroutine 을 main_coroutine 에서 호출하기
def subcoroutine():
    x = yield 10
    print("Recv : ", x)
    x = yield 100
    print("Recv : ", x)

def subcoroutine2():
    x = yield 20
    print("Recv : ", x)
    x = yield 200
    print("Recv : ", x)

def main_coroutine():
    yield from subcoroutine()
    yield from subcoroutine2()

t = main_coroutine()

print(t.send(5))
print(t.send(5))
print(t.send(5))
print(t.send(5))

