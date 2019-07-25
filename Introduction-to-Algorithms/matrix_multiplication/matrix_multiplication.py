import numpy as np
from tqdm import tqdm
from pprint import pprint
from itertools import chain, product, combinations

multiples = {_m: np.eye(1, 16, _i, dtype=int)[0]
             for _i, _m in
             enumerate((_p, _f)
                       for _p in 'abcd'
                       for _f in 'efgh'
                       )}

res = np.array([[1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])


def translate(formula: str):
    if not isinstance(formula, str):
        yield from formula
    else:
        _sgn = 1
        for _c in formula:
            if _c is '-':
                _sgn = -1
            elif _c is not '+':
                yield _c, _sgn
                _sgn = 1


def formula2array(formulas):
    yield from (sum(_sgn1 * _sgn2 * multiples[_c1, _c2]
                    for (_c1, _sgn1),
                        (_c2, _sgn2) in
                    product(translate(f1),
                            translate(f2)))
                for f1, f2 in formulas)


def check_strassen(num: int):
    def _bin_product(string: str):
        def _iter(_num_tuple):
            _total = 2 ** (_i - 1)
            for _count in range(_total):
                _ret = [(_num_tuple[0], 1)]
                for _j, _c in enumerate(_num_tuple[1:]):
                    _ret.append((_c, (_count >> _j) % 2 or -1))
                yield _ret

        for _i in range(1, num + 1):
            for _i_tuple in combinations(string, _i):
                yield from _iter(_i_tuple)

    pre, post = map(_bin_product, ('abcd', 'efgh'))
    pre_post = product(pre, post)
    for _i, formulas in tqdm(enumerate(combinations(pre_post, num))):
        # if _i < 10000000:
        #     continue
        mat = np.array(list(formula2array(formulas)))
        diff = mat.T.dot(np.linalg.pinv(mat.T).dot(res)) - res
        # print()
        # pprint(formulas)
        # break
        if ((diff > -0.01) & (diff < 0.01)).all():
            return mat


if __name__ == '__main__':
    # Strassen 给出的解
    fs = (('a', 'f-h'),
          ('a+b', 'h'),
          ('c+d', 'e'),
          ('d', 'g-e'),
          ('a+d', 'e+h'),
          ('b-d', 'g+h'),
          ('a-c', 'e+f'),)
    mat = np.array(list(formula2array(fs)))
    diff = mat.T.dot(np.linalg.pinv(mat.T).dot(res)) - res
    print("Strassen's hypothesis:", ((diff > -0.01) & (diff < 0.01)).all())
    # strassen_mul = np.array([[0, -1, 0, 1, 1, 1, 0],
    #                          [1, 1, 0, 0, 0, 0, 0],
    #                          [0, 0, 1, 1, 0, 0, 0],
    #                          [1, 0, -1, 0, 1, 0, -1]])
    # diff = np.linalg.pinv(mat.T).dot(res) - strassen_mul
    # print("Test:", ((diff > -0.01) & (diff < 0.01)).all())

    print(check_strassen(2))
