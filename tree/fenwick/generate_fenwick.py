def generate_fenwick_svg(n=64, filename="fenwick64.html"):
    # Размеры элементов
    box_w = 40
    box_h = 20
    gap = 4
    level_h = 35

    max_level = n.bit_length() - 1
    total_w = n * (box_w + gap)
    total_h = (max_level + 1) * level_h + 80

    svg = [
        f'<svg width="{total_w}" height="{total_h}" xmlns="http://www.w3.org/2000/svg" style="background-color: white; font-family: monospace;">'
    ]

    # 1. Рисуем индексы снизу и вертикальные линии-указатели
    for i in range(n):
        x_center = i * (box_w + gap) + box_w / 2
        # Текст индекса
        svg.append(
            f'<text x="{x_center}" y="{total_h - 10}" text-anchor="middle" font-size="12">{i}</text>'
        )
        # Маленькая вертикальная засечка у индекса
        svg.append(
            f'<line x1="{x_center}" y1="{total_h - 25}" x2="{x_center}" y2="{total_h - 35}" stroke="black" stroke-width="1"/>'
        )

    # 2. Рисуем сами узлы дерева (1-based индексы)
    for i in range(1, n + 1):
        lowbit = i & -i
        level = lowbit.bit_length() - 1
        start = i - lowbit  # 0-based индекс начала белой полосы
        end = i - 1  # 0-based индекс серой клетки

        x_start = start * (box_w + gap)
        x_end = end * (box_w + gap) + box_w
        y = total_h - 50 - level * level_h

        # Белая полоса (диапазон)
        svg.append(
            f'<rect x="{x_start}" y="{y}" width="{x_end - x_start}" height="{box_h}" fill="white" stroke="black" stroke-width="2"/>'
        )

        # Серая клетка (сам узел)
        svg.append(
            f'<rect x="{x_end - box_w}" y="{y}" width="{box_w}" height="{box_h}" fill="grey" stroke="black" stroke-width="2"/>'
        )

        # Вертикальная линия от серой клетки вниз к индексу
        center_x = x_end - box_w / 2
        svg.append(
            f'<line x1="{center_x}" y1="{y + box_h}" x2="{center_x}" y2="{total_h - 25}" stroke="black" stroke-width="2"/>'
        )

        # Подпись длины блока слева (1, 2, 4, 8, 16, 32, 64)
        if i == lowbit:  # Рисуем цифру только для первого блока на уровне
            svg.append(
                f'<text x="{x_start - 10}" y="{y + 15}" text-anchor="end" font-size="14" font-weight="bold">{lowbit}</text>'
            )

    svg.append("</svg>")
    html_content = f"<html><body>{''.join(svg)}</body></html>"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Схема успешно сгенерирована в файл: {filename}")


# Запуск генерации
generate_fenwick_svg(64)
