class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        sla = 0
        dot = 0
        flag = False
        s.append(path[0])

        i = 1
        while i < len(path):
            if s and path[i] == '/' and s[-1] != '/':
                s.append('/')
            elif s and path[i] == '.':
                while i < len(path) and path[i] == '.':
                    i += 1
                    dot += 1
                if i < len(path) and path[i] == '/':
                    if dot == 1:
                        if s:
                            dot = 0
                        if not s:
                            s.append('/')
                    elif dot == 2:
                        if s:
                            s.pop()
                        while s and s[-1] != '/':
                            s.pop()
                        dot = 0
                        if not s:
                            s.append('/')
                    else:
                        while dot != 0:
                            s.append('.')
                            dot -= 1
                else:
                    while dot != 0:
                        s.append('.')
                        dot -= 1
                    dot = 0
                i -= 1
            if path[i] != '.' and path[i] != '/':
                while i < len(path) and path[i] != '/':
                    s.append(path[i])
                    i += 1
                i -= 1
            i += 1

        if not s:
            return "/"
        if len(s) == 1 or len(s) == 0:
            return "/"
        elif s[-1] == '/':
            s.pop()
        if s[-1] == '.':
            j = len(s) - 1
            counter = 0
            while s[j] == '.':
                j -= 1
                counter += 1
            if s[j] == '/':
                if counter == 2:
                    while s and s[-1] != '/':
                        s.pop()
                    if s:
                        s.pop()
                    while s and s[-1] != '/':
                        s.pop()
                    if not s:
                        s.append('/')
                elif counter == 1:
                    if s:
                        s.pop()
                    if not s:
                        s.append('/')
        if s[-1] == '/':
            s.pop()
        if len(s) == 1 or len(s) == 0:
            return "/"
        return ''.join(s)


            
            