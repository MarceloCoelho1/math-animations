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
            pesos = [f"{random.uniform(-1, 1):+.2f}" for _ in range(6)] + ["\\vdots", f"{random.uniform(-1, 1):+.2f}"]
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


        vocab = Brace(colunas, UP, buff=0.2)
        vocab_text = MathTex("Vocab \\text{ size } \\approx 50k", font_size=30)
        vocab_text.next_to(vocab, UP, buff=0.2)
        vocab_annotation = VGroup(vocab, vocab_text)
        colunas.add(vocab_annotation)

        self.play(
            GrowFromCenter(vocab),
            GrowFromCenter(vocab_text), 
            run_time=1.5
        )
        self.wait(0.5)

        self.play(
            GrowFromCenter(chave),
            GrowFromCenter(texto_chave), 
            run_time=1.5
        )
        self.wait(3)

class Embedding2D(Scene):
    def construct(self):
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.2 
            }
        )
        
        coord_manga = [2, 1, 0]
        coord_comida = [2.1, 1.7, 0]
        coord_camisa = [-3, 2, 0]
        coord_fruta = [3, 1.2, 0]

        def create_word_point(coord, label_text, color):
            dot = Dot(plane.coords_to_point(*coord[:2]), color=color)
            vec = Arrow(plane.get_origin(), dot.get_center(), buff=0, color=color, stroke_width=3)
            label = Text(label_text, font_size=24).next_to(dot, UR, buff=0.1)
            return VGroup(vec, dot, label)

        manga = create_word_point(coord_manga, "manga", BLUE)
        comida = create_word_point(coord_comida, "comida", PURE_CYAN)
        camisa = create_word_point(coord_camisa, "camisa", RED)
        fruta = create_word_point(coord_fruta, "fruta", WHITE)

        self.play(Create(plane), run_time=1.5)
        self.wait(0.5)

        self.play(GrowArrow(manga[0]), FadeIn(manga[1:]))
        self.wait(0.3)

        self.play(GrowArrow(comida[0]), FadeIn(comida[1:]))

        self.play(GrowArrow(fruta[0]), FadeIn(fruta[1:]))

        
        surround_circle = Circle(radius=0.9, color=YELLOW, stroke_width=2).move_to(manga[1])
        self.play(Create(surround_circle))

        self.wait(0.5)

        
        self.play(GrowArrow(camisa[0]), FadeIn(camisa[1:]))
        
        self.wait(3)