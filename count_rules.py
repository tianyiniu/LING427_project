import csv
from operator import itemgetter

print("Give output file name: ")
x = input()
with open("rule_count.tsv", "w", encoding="utf8") as out:
    with open(x, "r", encoding="utf8") as f:
        i = 0
        out.write("Line\tSingular\tPlural\tCount\n")
        for line in f:
            i+=1
            if i < 9 : continue

            count = 0
            backslash = 0
            bs_one = 0
            bs_two = 0

            for char in line:
                if char == '\\':
                    backslash += 1
                if char == '(' :
                    count += 1
                if backslash == 0 :
                    bs_one += 1
                if backslash < 2 :
                    bs_two += 1

            sg = line[1:bs_one]
            pl = line[bs_one+1:bs_two]
            out.write(f"{i}\t{sg}\t{pl}\t{count}\n")

    reader = csv.reader(out, delimiter="\t")

    with open("sorted_rule_count.tsv", "w", encoding = "utf8") as sort_out:
        for line in sorted(reader, key=itemgetter(3)):
            sort_out.write(line)

            
