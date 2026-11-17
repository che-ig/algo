"""
Сравнение array-based красно-чёрного дерева и array-based splay-дерева.
Python 3.12. Только стандартная библиотека.

Оба дерева используют одинаковое представление:
    key[i], left[i], right[i], parent[i]  -- плоские списки индексов
    RB дополнительно: color[i] (0=RED, 1=BLACK), узел 0 = NIL-страж
    Splay: -1 = отсутствие узла

Почему list, а не array.array: при чтении list[i] возвращает уже существующий
объект int, а array.array[i] на каждый доступ создаёт НОВЫЙ int (boxing).
В чисто питоновском цикле list обычно быстрее. Харнесс позволяет проверить оба.
"""

from __future__ import annotations

import random
import statistics
import time
import tracemalloc


# =========================== Красно-чёрное дерево ===========================
class ArrayRB:
    __slots__ = ("key", "left", "right", "parent", "color", "free", "n", "root")

    def __init__(self) -> None:
        # индекс 0 -- NIL: чёрный, все ссылки на себя
        self.key: list[int] = [0]
        self.left: list[int] = [0]
        self.right: list[int] = [0]
        self.parent: list[int] = [0]
        self.color: list[int] = [1]
        self.free: list[int] = []
        self.n: int = 0
        self.root: int = 0

    def _new(self, k: int) -> int:
        if self.free:
            i = self.free.pop()
            self.key[i] = k
        else:
            i = len(self.key)
            self.key.append(k)
            self.left.append(0)
            self.right.append(0)
            self.parent.append(0)
            self.color.append(0)
        self.left[i] = 0
        self.right[i] = 0
        self.color[i] = 0  # новый узел красный
        return i

    def _rot_l(self, x: int) -> None:
        L, R, P = self.left, self.right, self.parent
        y = R[x]
        R[x] = L[y]
        if L[y]:
            P[L[y]] = x
        P[y] = P[x]
        if P[x] == 0:
            self.root = y
        elif L[P[x]] == x:
            L[P[x]] = y
        else:
            R[P[x]] = y
        L[y] = x
        P[x] = y

    def _rot_r(self, y: int) -> None:
        L, R, P = self.left, self.right, self.parent
        x = L[y]
        L[y] = R[x]
        if R[x]:
            P[R[x]] = y
        P[x] = P[y]
        if P[y] == 0:
            self.root = x
        elif R[P[y]] == y:
            R[P[y]] = x
        else:
            L[P[y]] = x
        R[x] = y
        P[y] = x

    def insert(self, k: int) -> bool:
        K, L, R, P, C = self.key, self.left, self.right, self.parent, self.color
        p, x = 0, self.root
        while x:
            p = x
            if k < K[x]:
                x = L[x]
            elif k > K[x]:
                x = R[x]
            else:
                return False
        z = self._new(k)
        P[z] = p
        if p == 0:
            self.root = z
        elif k < K[p]:
            L[p] = z
        else:
            R[p] = z
        self.n += 1

        while C[P[z]] == 0:  # родитель красный
            pp = P[z]
            g = P[pp]
            if pp == L[g]:
                y = R[g]
                if C[y] == 0:  # дядя красный
                    C[pp] = 1
                    C[y] = 1
                    C[g] = 0
                    z = g
                else:
                    if z == R[pp]:
                        z = pp
                        self._rot_l(z)
                        pp = P[z]
                        g = P[pp]
                    C[pp] = 1
                    C[g] = 0
                    self._rot_r(g)
            else:
                y = L[g]
                if C[y] == 0:
                    C[pp] = 1
                    C[y] = 1
                    C[g] = 0
                    z = g
                else:
                    if z == L[pp]:
                        z = pp
                        self._rot_r(z)
                        pp = P[z]
                        g = P[pp]
                    C[pp] = 1
                    C[g] = 0
                    self._rot_l(g)
        C[self.root] = 1
        C[0] = 1  # страховка стража
        return True

    def _transplant(self, u: int, v: int) -> None:
        L, R, P = self.left, self.right, self.parent
        if P[u] == 0:
            self.root = v
        elif L[P[u]] == u:
            L[P[u]] = v
        else:
            R[P[u]] = v
        P[v] = P[u]  # CLRS допускает запись в NIL.parent

    def _del_fixup(self, x: int) -> None:
        L, R, P, C = self.left, self.right, self.parent, self.color
        while x != self.root and C[x] == 1:
            if x == L[P[x]]:
                w = R[P[x]]
                if C[w] == 0:
                    C[w] = 1
                    C[P[x]] = 0
                    self._rot_l(P[x])
                    w = R[P[x]]
                if C[L[w]] == 1 and C[R[w]] == 1:
                    C[w] = 0
                    x = P[x]
                else:
                    if C[R[w]] == 1:
                        C[L[w]] = 1
                        C[w] = 0
                        self._rot_r(w)
                        w = R[P[x]]
                    C[w] = C[P[x]]
                    C[P[x]] = 1
                    C[R[w]] = 1
                    self._rot_l(P[x])
                    x = self.root
            else:
                w = L[P[x]]
                if C[w] == 0:
                    C[w] = 1
                    C[P[x]] = 0
                    self._rot_r(P[x])
                    w = L[P[x]]
                if C[R[w]] == 1 and C[L[w]] == 1:
                    C[w] = 0
                    x = P[x]
                else:
                    if C[L[w]] == 1:
                        C[R[w]] = 1
                        C[w] = 0
                        self._rot_l(w)
                        w = L[P[x]]
                    C[w] = C[P[x]]
                    C[P[x]] = 1
                    C[L[w]] = 1
                    self._rot_r(P[x])
                    x = self.root
        C[x] = 1

    def delete(self, k: int) -> bool:
        K, L, R, P, C = self.key, self.left, self.right, self.parent, self.color
        z = self.root
        while z:
            if k < K[z]:
                z = L[z]
            elif k > K[z]:
                z = R[z]
            else:
                break
        if not z:
            return False

        y = z
        y_orig = C[y]
        if L[z] == 0:
            x = R[z]
            self._transplant(z, R[z])
        elif R[z] == 0:
            x = L[z]
            self._transplant(z, L[z])
        else:
            y = R[z]
            while L[y]:
                y = L[y]
            y_orig = C[y]
            x = R[y]
            if P[y] == z:
                P[x] = y
            else:
                self._transplant(y, R[y])
                R[y] = R[z]
                P[R[y]] = y
            self._transplant(z, y)
            L[y] = L[z]
            P[L[z]] = y
            C[y] = C[z]

        self.free.append(z)
        self.n -= 1
        if y_orig == 1:
            self._del_fixup(x)
        C[0] = 1
        return True

    def search(self, k: int) -> bool:
        K, L, R = self.key, self.left, self.right
        x = self.root
        while x:
            if k < K[x]:
                x = L[x]
            elif k > K[x]:
                x = R[x]
            else:
                return True
        return False

    def inorder(self) -> list[int]:
        out: list[int] = []
        st: list[int] = []
        x = self.root
        while st or x:
            while x:
                st.append(x)
                x = self.left[x]
            x = st.pop()
            out.append(self.key[x])
            x = self.right[x]
        return out

    def height(self) -> int:
        """Итеративно: дерево может выродиться в цепочку."""
        best = 0
        st: list[tuple[int, int]] = [(self.root, 1)]
        while st:
            x, d = st.pop()
            if not x:
                continue
            if d > best:
                best = d
            st.append((self.left[x], d + 1))
            st.append((self.right[x], d + 1))
        return best


# ============================== Splay-дерево ================================
class ArraySplay:
    __slots__ = ("key", "left", "right", "parent", "free", "n", "root")

    def __init__(self) -> None:
        self.key: list[int] = []
        self.left: list[int] = []
        self.right: list[int] = []
        self.parent: list[int] = []
        self.free: list[int] = []
        self.n: int = 0
        self.root: int = -1

    def _new(self, k: int) -> int:
        if self.free:
            i = self.free.pop()
            self.key[i] = k
        else:
            i = len(self.key)
            self.key.append(k)
            self.left.append(-1)
            self.right.append(-1)
            self.parent.append(-1)
        self.left[i] = -1
        self.right[i] = -1
        self.parent[i] = -1
        return i

    def _rot(self, x: int) -> None:
        """Поднимает x над его родителем. КЛЮЧЕВОЕ: правим ссылку дедушки."""
        L, R, P = self.left, self.right, self.parent
        p = P[x]
        g = P[p]
        if L[p] == x:
            b = R[x]
            R[x] = p
            L[p] = b
        else:
            b = L[x]
            L[x] = p
            R[p] = b
        if b != -1:
            P[b] = p
        P[p] = x
        P[x] = g
        if g != -1:
            if L[g] == p:
                L[g] = x
            else:
                R[g] = x

    def _splay(self, x: int) -> None:
        L, P = self.left, self.parent
        while P[x] != -1:
            p = P[x]
            g = P[p]
            if g == -1:  # zig
                self._rot(x)
            elif (L[g] == p) == (L[p] == x):  # zig-zig
                self._rot(p)
                self._rot(x)
            else:  # zig-zag
                self._rot(x)
                self._rot(x)
        self.root = x

    def insert(self, k: int) -> bool:
        K, L, R, P = self.key, self.left, self.right, self.parent
        if self.root == -1:
            self.root = self._new(k)
            self.n += 1
            return True
        x, p = self.root, -1
        while x != -1:
            p = x
            if k < K[x]:
                x = L[x]
            elif k > K[x]:
                x = R[x]
            else:
                self._splay(x)
                return False
        z = self._new(k)
        P[z] = p
        if k < K[p]:
            L[p] = z
        else:
            R[p] = z
        self.n += 1
        self._splay(z)
        return True

    def search(self, k: int) -> bool:
        K, L, R = self.key, self.left, self.right
        x, last = self.root, -1
        while x != -1:
            last = x
            if k < K[x]:
                x = L[x]
            elif k > K[x]:
                x = R[x]
            else:
                self._splay(x)
                return True
        if last != -1:  # textbook: splay и при промахе
            self._splay(last)
        return False

    def delete(self, k: int) -> bool:
        K, L, R, P = self.key, self.left, self.right, self.parent
        x, last = self.root, -1
        while x != -1:
            last = x
            if k < K[x]:
                x = L[x]
            elif k > K[x]:
                x = R[x]
            else:
                break
        if last == -1:
            return False
        self._splay(last)
        if K[last] != k:
            return False

        z = last
        l, r = L[z], R[z]
        if l == -1:
            self.root = r
            if r != -1:
                P[r] = -1
        elif r == -1:
            self.root = l
            P[l] = -1
        else:
            P[l] = -1
            self.root = l
            m = l
            while R[m] != -1:
                m = R[m]
            self._splay(m)  # максимум левого поддерева в корень
            R[m] = r
            P[r] = m
        self.free.append(z)
        self.n -= 1
        return True

    def inorder(self) -> list[int]:
        out: list[int] = []
        st: list[int] = []
        x = self.root
        while st or x != -1:
            while x != -1:
                st.append(x)
                x = self.left[x]
            x = st.pop()
            out.append(self.key[x])
            x = self.right[x]
        return out

    def height(self) -> int:
        best = 0
        st: list[tuple[int, int]] = [(self.root, 1)]
        while st:
            x, d = st.pop()
            if x == -1:
                continue
            if d > best:
                best = d
            st.append((self.left[x], d + 1))
            st.append((self.right[x], d + 1))
        return best


# ============================ Self-тесты ====================================
def selftest(cls, name: str, trials: int = 20, n: int = 250) -> None:
    rnd = random.Random(7)
    for _ in range(trials):
        t = cls()
        model: set[int] = set()
        for _ in range(n * 3):
            op = rnd.random()
            k = rnd.randrange(n)
            if op < 0.45:
                assert t.insert(k) == (k not in model), (name, "insert", k)
                model.add(k)
            elif op < 0.75:
                assert t.delete(k) == (k in model), (name, "delete", k)
                model.discard(k)
            else:
                assert t.search(k) == (k in model), (name, "search", k)
            assert t.n == len(model), (name, "size")
        assert t.inorder() == sorted(model), (name, "order")
    print(f"{name}: self-test OK")


def rb_invariants(t: ArrayRB) -> None:
    assert t.color[t.root] == 1
    st = [(t.root, 0)]
    blacks: set[int] = set()
    while st:
        x, b = st.pop()
        if x == 0:
            blacks.add(b + 1)
            continue
        if t.color[x] == 0:
            assert t.color[t.left[x]] == 1 and t.color[t.right[x]] == 1, "red-red"
        st.append((t.left[x], b + (t.color[x] == 1)))
        st.append((t.right[x], b + (t.color[x] == 1)))
    assert len(blacks) == 1, f"black-height differs: {blacks}"


# ============================ Бенчмарк ======================================
def timeit(fn, repeat: int = 3) -> float:
    best: list[float] = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn()
        best.append(time.perf_counter() - t0)
    return statistics.median(best)


def build(cls, keys):
    t = cls()
    ins = t.insert
    for k in keys:
        ins(k)
    return t


def bench(n: int = 25000, repeat: int = 3) -> None:
    rnd = random.Random(42)
    keys = list(range(n))
    rnd.shuffle(keys)
    sorted_keys = list(range(n))

    hits = [rnd.randrange(n) for _ in range(n)]
    misses = [n + rnd.randrange(n) for _ in range(n)]
    hot = keys[: max(1, n // 20)]  # 5% "горячих"
    skewed = [
        rnd.choice(hot) if rnd.random() < 0.8 else rnd.randrange(n) for _ in range(n)
    ]
    sequential = list(range(n))
    to_delete = keys[: n // 2]

    rows: list[tuple[str, float, float]] = []

    for label, work in [
        ("insert random", lambda t: [t.insert(k) for k in keys]),
        ("insert sorted", lambda t: [t.insert(k) for k in sorted_keys]),
    ]:
        vals = []
        for cls in (ArrayRB, ArraySplay):
            vals.append(timeit(lambda cls=cls, work=work: work(cls()), repeat))
        rows.append((f"{label} (n={n})", *vals))

    # поиск по уже построенным деревьям (строятся один раз на повтор)
    for label, probe in [
        ("search uniform hit", hits),
        ("search skewed 80/20", skewed),
        ("search miss", misses),
        ("search sequential", sequential),
    ]:
        vals = []
        for cls in (ArrayRB, ArraySplay):

            def run(cls=cls, probe=probe):
                t = build(cls, keys)
                s = t.search
                for k in probe:
                    s(k)

            # вычитаем стоимость построения
            base = timeit(lambda cls=cls: build(cls, keys), repeat)
            vals.append(timeit(run, repeat) - base)
        rows.append((f"{label} (n={n})", *vals))

    for label in ("delete random 50%",):
        vals = []
        for cls in (ArrayRB, ArraySplay):

            def run(cls=cls):
                t = build(cls, keys)
                d = t.delete
                for k in to_delete:
                    d(k)

            base = timeit(lambda cls=cls: build(cls, keys), repeat)
            vals.append(timeit(run, repeat) - base)
        rows.append((f"{label} (n={n})", *vals))

    print(f"\n{'workload':<30}{'RB, s':>10}{'Splay, s':>12}{'RB/Splay':>12}")
    print("-" * 64)
    for name, rb, sp in rows:
        print(f"{name:<30}{rb:>10.4f}{sp:>12.4f}{rb / sp:>12.2f}")

    # структура и память
    for cls in (ArrayRB, ArraySplay):
        t = build(cls, keys)
        print(f"{cls.__name__:<12} height(random)={t.height():>4}", end="  ")
        t2 = build(cls, sorted_keys)
        print(f"height(sorted)={t2.height():>6}")

    for cls in (ArrayRB, ArraySplay):
        tracemalloc.start()
        t = build(cls, keys)
        cur, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"{cls.__name__:<12} live={cur / 1e6:.2f} MB  peak={peak / 1e6:.2f} MB")
        del t


if __name__ == "__main__":
    selftest(ArrayRB, "ArrayRB")
    selftest(ArraySplay, "ArraySplay")
    r = ArrayRB()
    for k in random.Random(1).sample(range(5000), 2000):
        r.insert(k)
    rb_invariants(r)
    print("RB invariants OK")

    for n in (1000, 5000, 15000):
        bench(n)
