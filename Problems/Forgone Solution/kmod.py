import sys

if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    for _T in range(T):
        S = f.readline().strip()

        A = list(S)
        B = ['0'] * len(A)

        for i in range(len(A)):
            if A[i] == '4':
                A[i] = '3'
                B[i] = '1'

        A = ''.join(A)
        B = ''.join(B).lstrip('0')
        print("Case #%d: %s %s" % (_T + 1, A, B))
