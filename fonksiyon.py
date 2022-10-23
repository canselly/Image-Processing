def yashesaplama(dogumyılı):
    return 2022-dogumyılı


def emeklilikhesaplama(dogumyılı, ad):
    yas = yashesaplama(dogumyılı)
    emeklilik= 65 - yas
    if emeklilik > 0:
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("zaten emekli oldunuz...")

emeklilikhesaplama(1968, "fatma")
emeklilikhesaplama(1989, "reyyan")
emeklilikhesaplama(1998, "cansel")