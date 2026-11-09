def generate_fenwick_with_table(N=16, filename="fenwick_1based_table.html"):
    # ==========================================
    # 1. НАСТРОЙКИ ДЛЯ SVG (ДИАГРАММА)
    # ==========================================
    cell_width = 50
    box_width = 24
    box_height = 24
    level_height = 65
    margin_left = 100
    margin_top = 80
    margin_bottom = 80

    max_level = N.bit_length() - 1
    width = margin_left + N * cell_width + 50
    height = margin_top + max_level * level_height + margin_bottom

    svg = [
        f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" style="background-color: white; font-family: sans-serif;">'
    ]
    svg.append(
        f'<text x="{margin_left}" y="50" font-size="36" font-weight="bold" font-family="sans-serif">Binary indexed tree</text>'
    )

    for i in range(1, N + 1):
        lb = i & -i
        level = lb.bit_length() - 1
        cx = margin_left + (i - 1) * cell_width + cell_width / 2
        y = margin_top + (max_level - level) * level_height

        grey_right = cx + box_width / 2
        grey_left = cx - box_width / 2

        start_idx = i - lb + 1
        white_left = (
            margin_left + (start_idx - 1) * cell_width + cell_width / 2 - box_width / 2
        )

        # Линия вниз
        svg.append(
            f'<line x1="{cx}" y1="{y + box_height}" x2="{cx}" y2="{height - margin_bottom + 20}" stroke="black" stroke-width="2"/>'
        )

        # Белый блок
        if lb > 1:
            svg.append(
                f'<rect x="{white_left}" y="{y}" width="{grey_left - white_left}" height="{box_height}" fill="white" stroke="black" stroke-width="2"/>'
            )

        # Серый блок
        svg.append(
            f'<rect x="{grey_left}" y="{y}" width="{box_width}" height="{box_height}" fill="#888888" stroke="black" stroke-width="2"/>'
        )

        # Индексы по X
        svg.append(
            f'<text x="{cx}" y="{height - margin_bottom + 45}" text-anchor="middle" font-size="16" font-weight="bold">{i}</text>'
        )

        # Подписи слева (1, 2, 4...)
        if i == lb:
            svg.append(
                f'<text x="{white_left - 15}" y="{y + box_height / 2 + 6}" text-anchor="end" font-size="16" font-weight="bold">{lb}</text>'
            )

    svg.append(
        f'<text x="{margin_left - 40}" y="{height - margin_bottom + 45}" text-anchor="end" font-size="16" font-weight="bold">i:</text>'
    )
    svg.append("</svg>")

    # ==========================================
    # 2. ГЕНЕРАЦИЯ HTML-ТАБЛИЦЫ
    # ==========================================
    bit_width = max(8, N.bit_length() + 1)
    mask = (1 << bit_width) - 1

    table_html = ["<table>"]
    table_html.append("""
        <tr>
            <th>i<br><small>(dec)</small></th>
            <th>i<br><small>(bin)</small></th>
            <th>-i<br><small>(two's comp)</small></th>
            <th>i & -i<br><small>(bin)</small></th>
            <th>lowbit<br><small>(dec)</small></th>
        </tr>
    """)

    for i in range(1, N + 1):
        i_bin = format(i, f"0{bit_width}b")
        neg_i_bin = format(-i & mask, f"0{bit_width}b")
        lowbit_bin = format(i & -i, f"0{bit_width}b")
        lowbit_dec = i & -i

        table_html.append(f"""
            <tr>
                <td><b>{i}</b></td>
                <td class="mono">{i_bin}</td>
                <td class="mono">{neg_i_bin}</td>
                <td class="mono highlight">{lowbit_bin}</td>
                <td><b>{lowbit_dec}</b></td>
            </tr>
        """)

    table_html.append("</table>")
    table_str = "".join(table_html)

    # ==========================================
    # 3. СБОРКА И СОХРАНЕНИЕ HTML (ИЗМЕНЕН CSS)
    # ==========================================
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{
                font-family: sans-serif;
                margin: 20px;
                background-color: #f9f9f9;
            }}
            .container {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                display: inline-block; /* Контейнер сжимается по содержимому */
            }}
            table {{
                border-collapse: collapse;
                margin-top: 30px;
                font-size: 14px;
                table-layout: fixed; /* Фиксированная ширина колонок */
                width: max-content;  /* Таблица не растягивается на весь экран */
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 6px 8px;
                text-align: center;
                white-space: nowrap; /* Запрет переноса текста */
            }}
            /* Фиксированные ширины для каждой колонки */
            th:nth-child(1), td:nth-child(1) {{ width: 60px; }}
            th:nth-child(2), td:nth-child(2) {{ width: 100px; }}
            th:nth-child(3), td:nth-child(3) {{ width: 120px; }}
            th:nth-child(4), td:nth-child(4) {{ width: 110px; }}
            th:nth-child(5), td:nth-child(5) {{ width: 70px; }}

            th {{
                background-color: #f2f2f2;
                line-height: 1.2;
            }}
            .mono {{
                font-family: monospace;
                font-size: 15px;
                letter-spacing: 1px;
            }}
            .highlight {{
                background-color: #e6f3ff;
                font-weight: bold;
            }}
            tr:nth-child(even) {{
                background-color: #fafafa;
            }}
            tr:hover {{
                background-color: #f0f0f0;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            {"".join(svg)}
            {table_str}
        </div>
    </body>
    </html>
    """

    with open(filename, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Диаграмма и таблица успешно сохранены в файл: {filename}")


# Запуск
generate_fenwick_with_table(64)
