def hanoi_solver(n):
    rods = [
        list(range(n, 0, -1)),
        [],
        []
    ]

    moves = []

    def record():
        moves.append(" ".join(str(rod) for rod in rods))

    def move_disk(source, target):
        disk = rods[source].pop()
        rods[target].append(disk)
        record()

    def solve(n, source, auxiliary, target):
        if n == 1:
            move_disk(source, target)
            return

        solve(n - 1, source, target, auxiliary)
        move_disk(source, target)
        solve(n - 1, auxiliary, source, target)

    # Starting arrangement
    record()

    # Solve the puzzle
    solve(n, 0, 1, 2)

    return "\n".join(moves)