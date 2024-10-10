from tqdm import tqdm

# https://reddit.com/r/PictureGame/comments/s6lrdj/round_105759_there_are_ten_different_letters_in/

for b in tqdm(range(10)):
    for u in range(10):
        for t in range(10):
            for l in range(10):
                for e in range(10):
                    for a in range(10):
                        for s in range(10):
                            least = 10000 * l + 1000 * e + 100 * a + 10 * s + t
                            but = 100 * b + 10 * u + t
                            o = 1
                            obo = 100 * o + 10 * b + o
                            if (100 * l + 10 * e + a) - but == obo:
                                for y in range(10):
                                    obos = 10 * obo + s
                                    osty = 1000 * o + 100 * s + 10 * t + y
                                    if but * u == osty and 100 * u + 10 * a + s == obos - osty:
                                        uast = (obos - osty) * 10 + t
                                        for r in range(10):
                                            uobt = 1000 * u + 100 * o + 10 * b + t
                                            if uobt == but * r:
                                                print(f'{b=} {u=} {t=} {l=} {e=} {a=} {s=} {o=} {y=} {r=}')