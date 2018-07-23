def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your = set((yourLeft, yourRight))
    friends = set((friendsLeft, friendsRight))
    return your == friends