
def read_text_file(text_file):
    with open(text_file,"r") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        if not line.strip() == '':
            new_lines.append(line.strip())
    return new_lines

def read_constraint(lines):
    constraints =[]
    for line in lines:
        names= line.split(" ")
        constraints.append(names)

    return constraints
def build(new_lines):

    must_in_same_group, must_not_in_same_group, problem_group = None, None, None
    groups=[]
    index =0
    for i in range(3):
        if new_lines[index].isdigit():
            number_of_constraint = int(new_lines[index])
            groups.append(read_constraint(new_lines[index+1:index+number_of_constraint+1]))
        index = index+number_of_constraint+1
    return groups

def check_must_not_in_same_group_violation(must_not_in_same_groups,problem_group):
    for check_group in must_not_in_same_groups:
        if check_group[0] in problem_group and check_group[1] in problem_group:
            return True
    return False
def check_must_in_same_group_violation(must_in_same_groups,problem_group):
    for check_group in must_in_same_groups:
        if check_group[0] in problem_group and not check_group[1] in problem_group:
            return True
        elif check_group[1] in problem_group and not check_group[0] in problem_group:
            return True
    return False
def main():
  # 1: read problem from text file
  lines = read_text_file("../../TextFiles/2022/P4_Input_2022")

  # 2. build constraint list and problem list

  must_in_same_group, must_not_in_same_group, problem_groups = build(lines)

  # 3. check constraint violation

  violation_num = 0
  for problem_group in problem_groups:
      check_result = check_must_not_in_same_group_violation(must_not_in_same_group,problem_group)
      check_result_2= check_must_in_same_group_violation(must_in_same_group, problem_group)
      if check_result or check_result_2:
          violation_num+=1

  # 4. print out result

  print(violation_num)


if __name__ == "__main__":
    # code here runs only if you execute this file directly
    main()

















