if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    li = student_marks[query_name]
    avg = sum(li) / len(li)
    print("{:.2f}".format(avg))