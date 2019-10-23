def main():
    num_tests = int(input())
    for test in range(num_tests):
        A = list(input())
        print(A)
        if '4' not in set(A):
            print(''.join(A), '0')
        B = ['0'] * len(A)
        for place, digit in enumerate(A):
            if digit == '4':
                A[place] = '3'
                B[place] = '1'
        print(''.join(A), ''.join(B).lstrip('0'))


if __name__ == '__main__':
    main()
