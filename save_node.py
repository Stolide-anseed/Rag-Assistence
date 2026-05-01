from src.graph import make_graph

def beatifull_graph():
    graph = make_graph()
    png_data = graph.get_graph().draw_mermaid_png()

    # Записываем в файл
    with open("graph.png", "wb") as f:
        f.write(png_data)

    print("Граф сохранен в файл graph.png")