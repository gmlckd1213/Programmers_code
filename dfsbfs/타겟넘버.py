def solution(numbers, target):
    super = [0]
    for num in numbers:
        sub_node = []
        for sup in super:
            sub_node.append(sup+num)
            sub_node.append(sup-num)
        super = sub_node
        print(sub_node)
    return super.count(target)
