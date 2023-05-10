def print_incremental_integers(n, c):
    for i in range(n):
        for j in range(1, c+1):
            print(j, end=' ')
        print()

# Example usage
import sys
print_incremental_integers(int(sys.argv[1]), int(sys.argv[2]))

