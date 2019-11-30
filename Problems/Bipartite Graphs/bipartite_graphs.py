def bipartite_graphs(n: int, m: int, d: int, D: int) -> str:
    """
    Finds if a graph with the given property is available or not.
    :param n: The number of vertices on each part of the bipartite graph.
    :param m: The total number of edges.
    :param d: The minimum degree of any vertex v.
    :param D: The maximum degree of any vertex v.
    :return: A string of m lines where each line is of the form 'u v'
    denoting an edge between u and v if such a graph is possible
    else -1.
    """
    # If the total number of edges, m, is
    # less than n * d (i.e. minimum # edges that could be made) or
    # more than n * D (i.e. maximum # edges that can be made),
    # No such graph exists.
    if m < n * d or m > n * D: return '-1'
    # Vars to hold
    # min_deg = equally distributing the edges among all vertices (i.e. m // n).
    # remaining = the number edges still to be made after each vertex has
    # degree = min_deg.
    # res -> to hold the string representation of the bipartite graph.
    min_deg, remaining, result = *divmod(m, n), []

    # For each vertex numbered from 1 to n,
    for vertex in range(n):
        # Make the degree of each vertex min_deg,
        for deg in range(min_deg):
            result.append(f'{vertex + 1} {(vertex + deg) % n + 1}')

    # Make the remaining edges.
    for vertex in range(remaining):
        result.append(f'{vertex + 1} {(vertex + min_deg) % n + 1}')

    # return tte result
    return '\n'.join(result)


def main():
    """
    Driver function.
    :return: None
    """
    # For all the test cases,
    for _ in range(int(input())):
        # Get the input,
        n, m, d, D = map(int, input().split())
        # Solve for possible graphs.
        result = bipartite_graphs(n, m, d, D)
        # Output the result.
        print(result)


if __name__ == '__main__':
    main()
