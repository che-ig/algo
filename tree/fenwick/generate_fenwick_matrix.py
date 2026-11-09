def generate_fenwick_matrix_svg(n=64, filename="fenwick_matrix_64.html"):
    cell_size = 14  # Размер одной клетки
    margin = 40  # Отступ для подписей осей
    total_size = n * cell_size + margin

    svg = [
        f'<svg width="{total_size + 20}" height="{total_size + 20}" xmlns="http://www.w3.org/2000/svg" style="background-color: white; font-family: monospace;">'
    ]

    # 1. Рисуем клетки матрицы
    for y in range(n):  # Ось Y (узлы дерева)
        # В 1-based индексации текущий узел имеет номер y + 1
        node_1based = y + 1
        # Длина покрытия этого узла (lowbit)
        lowbit = node_1based & -node_1based

        # Узел покрывает 0-based индексы от (node_1based - lowbit) до (node_1based - 1)
        start_x = node_1based - lowbit
        end_x = node_1based - 1

        for x in range(n):  # Ось X (элементы массива)
            # Вычисляем координаты с учетом того, что ось Y на картинке идет снизу вверх
            px = margin + x * cell_size
            py = margin + (n - 1 - y) * cell_size

            # Проверяем, покрывает ли узел y элемент x
            if start_x <= x <= end_x:
                fill_color = "#888888"  # Серый цвет для покрытия
            else:
                fill_color = "#ffffff"  # Белый цвет для пустоты

            # Рисуем квадрат (клетку) с черной обводкой
            svg.append(
                f'<rect x="{px}" y="{py}" width="{cell_size}" height="{cell_size}" fill="{fill_color}" stroke="black" stroke-width="1"/>'
            )

    # 2. Рисуем подписи осей (каждое 4-е число для читаемости на 64 элементах)
    font_size = 9
    for i in range(0, n, 4):
        # Подписи снизу (ось X)
        px_x = margin + i * cell_size + cell_size / 2
        py_x = margin + n * cell_size + 12
        svg.append(
            f'<text x="{px_x}" y="{py_x}" text-anchor="middle" font-size="{font_size}">{i}</text>'
        )

        # Подписи слева (ось Y)
        px_y = margin - 10
        py_y = margin + (n - 1 - i) * cell_size + cell_size / 2 + 3
        svg.append(
            f'<text x="{px_y}" y="{py_y}" text-anchor="end" font-size="{font_size}">{i}</text>'
        )

    svg.append("</svg>")

    html_content = f"<html><body>{''.join(svg)}</body></html>"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Матрица успешно сгенерирована в файл: {filename}")


# Запуск генерации
generate_fenwick_matrix_svg(64)
