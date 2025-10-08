def recursive(start):
    if start < 0:
        return
    print(start)
    recursive(start-1)
    
recursive(10)