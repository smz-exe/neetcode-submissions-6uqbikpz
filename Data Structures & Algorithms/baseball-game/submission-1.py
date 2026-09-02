class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for c in operations:
            if c == "+":
                record.append(record[-1] + record[-2])
            elif c == "D":
                record.append(2 * record[-1])
            elif c == "C":
                record.pop()
            else:
                record.append(int(c))

        return sum(record)