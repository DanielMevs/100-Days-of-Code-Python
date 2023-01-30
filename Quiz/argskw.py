def all_aboard(a, *args, **kw):
    print(a, args, kw)


print(all_aboard(4, 7, 3, 0, x=10, y=64))
