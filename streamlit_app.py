import streamlit as st
from maze_solver import MAZE, START, END, solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")
st.write("App cargada desde streamlit_app.py (debug)")


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


st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo",
    ["BFS", "DFS (no implementado)", "A* (no implementado)"],
)
solve_button = st.sidebar.button("Resolver Laberinto")

render_maze(MAZE)

if solve_button:
    st.write("Click en Resolver (debug)")
    if algorithm != "BFS":
        st.warning(f"El algoritmo {algorithm} aún no está implementado. Usa BFS.")
    else:
        path = solve_maze_bfs(MAZE, START, END)
        st.write("Path calculado, longitud:", len(path) if path else None)
        if path:
            st.success(f"¡Camino encontrado con {algorithm}!")
            render_maze(MAZE, path)
        else:
            st.error("No se encontró un camino.")
