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

class Embedding(Scene):
    def construct(self):
        random.seed(42)
        frase_lista = [
            'casa',
            'mesa',
            'nuvem',
            'ovo',
            'amor',
            'osso',
            'neve',
            '\\dots',
            'exame',
            'nossa',
        ]
        paleta = [BLUE, BLUE_A, WHITE, RED, RED_A]

        colunas = VGroup()

        # 1. Criar as colunas individualmente
        for palavra in frase_lista:
            txt = Tex(palavra, font_size=30)
            pesos = [f"{random.uniform(0, 1):.2f}" for _ in range(6)] + ["\\vdots", f"{random.uniform(0, 1):.2f}"]
            vetor = ColoredVector(values=pesos, colors=paleta, vertical=True, font_size=24)
            
            # Agrupa texto e vetor. O arrange coloca o vetor abaixo do centro do texto.
            coluna = VGroup(txt, vetor).arrange(DOWN, buff=0.6)
            colunas.add(coluna)

        # 2. Posicionamento horizontal das colunas
        colunas.arrange(RIGHT, buff=0.4)

        colunas.center()

        # 4. Animação
        self.play(
            LaggedStart(
                *[Write(col[0]) for col in colunas],
                lag_ratio=0.3
            )
        )
        self.wait(0.5)
        self.play(
            *[Write(col[1]) for col in colunas],
            run_time=3,
            lag_ratio=0.1
        )
        self.wait(2)

        chave = Brace(colunas[0][1], LEFT, buff=0.2)
        texto_chave = MathTex("d=512", font_size=24)
        texto_chave.rotate(90 * DEGREES)
        texto_chave.next_to(chave, LEFT, buff=0.2)
        anotacao = VGroup(chave, texto_chave)
        colunas.add(anotacao)

        self.play(
            GrowFromCenter(chave),
            FadeIn(texto_chave, shift=UP*0.2), 
            run_time=1.5
        )
        self.wait(3)