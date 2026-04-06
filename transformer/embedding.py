from manim import *
import random
from utils import ColoredVector

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