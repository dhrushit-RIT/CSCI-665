# A = [5, 8, 2, 1, 7, 6, 4]
# A = [5, 10, 15, 20, 25, 30, 35, 40]
# A = [5]
# A = [1]
# A = [2]
# A = [5, 8]
# A = [1, 2]
# A = [10, 2]
# A = [5, 8, 10]
# A = [5, 10, 8]
# A = [1, 2,10]
# A = [10, 10,2]
# A = [10, 11,2]
# A = [10, 11,2,3,4]

# A = [1,2,3,4,5,6,7,8,7,6,5,4,3,2,1,8,7,6,5,6,7,2,1]

# A = [1,2,3,4,5,6,7,8, 9, 10, 11, 12, 13, 15, 16, 17]
# A = [1,2,3,4,5,6,7,8, 1,2,3,4,5,6,7,8]
# A = [1, 2, 3]
# A = [6, 6, 8, 8, 8]
# A = [6, 6,1,2,3,4, 8, 8]
A = [6, 7,5,4,3,2, 8, 8]


def mystery(left, right, tabs=0) -> (int, int, int):

    if left == right:
        return 1, 1, 1
    else:
        m = (left + right) // 2
        # for i in range(tabs):
        #     print("    ",end="")
        # print("m=",m)
        (part1Lrun, part1Rrun, part1maxrun) = mystery(left, m, tabs+1)
        (part2Lrun, part2Rrun, part2maxrun) = mystery(m + 1, right, tabs+1)

        # for i in range(tabs):
        #     print("    ",end="")
        # print(part1Lrun, part1Rrun, part1maxrun)

        # for i in range(tabs):
        #     print("    ",end="")
        # print(part2Lrun, part2Rrun, part2maxrun)

        if A[m] < A[m + 1]:
            maxrun = max(part1maxrun, part2maxrun, part1Rrun + part2Lrun)

            if part1maxrun == m - left + 1:
                Lrun = part1maxrun + part2Lrun
            else:
                Lrun = part1Lrun

            if part2maxrun == right - m:
                Rrun = part2maxrun + part1Rrun
            else:
                Rrun = part2Rrun

        else:
            maxrun = max(part1maxrun, part2maxrun)
            Lrun = part1Lrun
            Rrun = part2Rrun

        print(Lrun, Rrun, maxrun)
        return (Lrun, Rrun, maxrun)


def main():
    print(mystery(0, len(A)-1))


if __name__ == '__main__':
    main()
