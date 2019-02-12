# Count unique emails
class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        count = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            full = '@'.join([local, domain])
            count.add(full)
        return len(count)


# return most common emails.
class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        from collections import defaultdict
        count = defaultdict(int)
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')
            full = '@'.join([local, domain])
            count[full] += 1
        maximum = 0
        ret = None
        for email, counting in count.items():
            if counting > maximum:
                ret = email
                maximum = counting
        return ret

solution = Solution()
list1 = []
print(solution.numUniqueEmails(list1))
list2 = ['a+c@b.com', 'a.a@b.com', 'a+a@b.com', 'a.b.c+1@x.edu',
         'a.b.c+2@x.edu', 'a.bc+1.1@x.edu', 'abc+2.3@x.edu']
print(solution.numUniqueEmails(list2))
list2 = ['@', '@', 'x@', 'x@', 'x@']
print(solution.numUniqueEmails(list2))