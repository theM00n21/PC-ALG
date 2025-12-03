import time
import streamlit as st
from maze_solver import (
    MAZE,
    START,
    END,
    solve_maze_bfs,
    solve_maze_dfs,
    solve_maze_astar,
)

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")


def render_maze(maze, path=None):
    if path is None:
        path = []

    cell_wall = "⬛"
    cell_free = "⬜"
    cell_start = "🚀"
    cell_end = "🏁"
    cell_path = "🟦"

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            position = (r_idx, c_idx)
            if position == START:
                display_row.append(cell_start)
            elif position == END:
                display_row.append(cell_end)
            elif position in path:
                display_row.append(cell_path)
            elif col == 1:
                display_row.append(cell_wall)
            else:
                display_row.append(cell_free)
        display_maze.append("".join(display_row))

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


ALGORITHMS = {
    "BFS": solve_maze_bfs,
    "DFS": solve_maze_dfs,
    "A*": solve_maze_astar,
}

st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo",
    list(ALGORITHMS.keys()),
)
solve_button = st.sidebar.button("Resolver Laberinto")

render_maze(MAZE)

if solve_button:
    solver = ALGORITHMS.get(algorithm)
    start_time = time.time()
    path = solver(MAZE, START, END)
    end_time = time.time()
    if path:
        st.success(
            f"¡Camino encontrado con {algorithm}! Pasos: {len(path) - 1} "
            f"- Tiempo: {end_time - start_time:.5f} s"
        )
        render_maze(MAZE, path)
    else:
        st.error("No se encontró un camino.")
