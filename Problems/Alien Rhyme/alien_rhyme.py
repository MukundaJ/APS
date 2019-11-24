from collections import defaultdict


class TNode(object):
    __slots__ = 'children', 'is_word_end', 'root'

    def __init__(self, root=False):
        self.children, self.is_word_end = [None] * 26, False
        self.root = root

    def add(self, string, pos):
        if pos == len(string):
            self.is_word_end = True
        else:
            child = ord(string[pos]) - ord('A')
            if self.children[child] is None:
                self.children[child] = TNode()
            self.children[child].add(string, pos + 1)

    # def ans(self, root):
    #     ans = [0, 1 if self.is_word_end else 0]
    #     for i in range(len(self.children)):
    #         if not self.children[i] is None:
    #             sub_ans = self.children[i].ans(False)
    #             ans[0] += sub_ans[0]
    #             ans[1] += sub_ans[1]
    #     if ans[1] >= 2 and not root:
    #         ans[0] += 1
    #         ans[1] -= 2
    #
    #     return ans
#
#
# def alien_rhyme_optimized(words):
#     root = TNode(True)
#     for word in words:
#         root.add(word[::-1], 0)
#     return root.ans(True)[0] * 2



def alien_rhyme(words):
    count, _words = defaultdict(int), defaultdict(set)
    for word in words:
        for suffix in suffixes(word):
            count[suffix] += 1
            _words[suffix].add(word)
    useful_suff = [suffix for suffix, _count in count.items() if _count > 1]
    useful_suff.sort(key=len, reverse=True)
    res, unavailable = 0, set()
    for suff in useful_suff:
        available = list(_words[suff] - unavailable)
        if len(available) > 1:
            res += 2
            unavailable |= set(available[:2])
    return res


def suffixes(word):
    return [word[i:] for i in range(len(word))]


def main():
    num_tests = int(input())
    for test_num in range(1, num_tests + 1):
        words = [input().strip() for _ in range(int(input()))]
        result = alien_rhyme(words)
        print('Case #{}: {}'.format(test_num, result))
    pass


if __name__ == '__main__':
    main()
