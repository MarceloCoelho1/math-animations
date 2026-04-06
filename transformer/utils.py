from manim import *
import random

class ColoredVector(VGroup):
    def __init__(self, values, colors, vertical=True, font_size=30, **kwargs):
        super().__init__(**kwargs)
        
        inicio = "\\begin{bmatrix}"
        fim = "\\end{bmatrix}"
        separador = " \\\\ " if vertical else " & "
        elementos = [inicio]
        
        for i, v in enumerate(values):
            elementos.append(v)
            if i < len(values) - 1:
                elementos.append(separador)
        elementos.append(fim)

        self.vector_obj = MathTex(*elementos, font_size=font_size)

        for i, item in enumerate(elementos):
            if item not in [inicio, fim, separador]:
                if "\\" in item and "dots" in item:
                    self.vector_obj[i].set_color(GRAY)
                else:
                    cor_aleatoria = random.choice(colors)
                    self.vector_obj[i].set_color(cor_aleatoria)

        self.add(self.vector_obj)