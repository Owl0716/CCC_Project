# def read_file(file_path):
#     new_lines = []
#     with open(file_path, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             if not line.strip() == '':
#                 line = line.strip()
#                 new_lines.append(line)
#
#     return new_lines
# def try_game(game,reactions,reaction=None,path=None):
#     path = path + reaction
#     if reaction in path:
#
#
#     def find_shortest_path(visited, person, friend):
#         visited = visited + [person]
#         if friend in visited:
#             return len(visited) - 1
#         shortest = None
#         for p in friends[person]:
#             if p not in visited:
#                 dist = find_shortest_path(visited, p, friend)
#                 if dist is not None:
#                     if shortest is None or dist < shortest:
#                         shortest = dist
#         return shortest
#
# def main():
#     reactions = [[2,1,0,2],[1,1,1,1],[0,0,2,1],[0,3,0,0],[1,0,0,1]]
#     lines = read_file('../../TextFiles/2010/P5_Input_2010')
#     amount_of_games = lines[0]
#     try_game(lines[0],reactions)
# if __name__ == '__main__':
#     main()