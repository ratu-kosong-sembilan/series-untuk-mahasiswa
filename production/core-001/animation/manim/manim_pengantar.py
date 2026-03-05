from manim import *
import numpy as np

class Segment1_PreModuleHook(Scene):
    def construct(self):
        # [0:00–0:20] Split screen: kiri rumus, kanan phasor
        left_panel = Rectangle(height=5, width=6, color=BLUE).shift(LEFT*3)
        right_panel = Rectangle(height=5, width=6, color=GREEN).shift(RIGHT*3)
        
        left_formulas = VGroup(
            MathTex(r"\sin(\omega t + \phi_1) + \sin(\omega t + \phi_2)"),
            MathTex(r"= 2\sin\left(\frac{\phi_1+\phi_2}{2}\right)\cos\left(\omega t + \frac{\phi_1-\phi_2}{2}\right)")
        ).arrange(DOWN, buff=0.3).scale(0.7).shift(LEFT*3)
        
        right_phasor = MathTex(r"\tilde{V}_1 + \tilde{V}_2 = V_1\angle\phi_1 + V_2\angle\phi_2").scale(0.9).shift(RIGHT*3)
        
        self.play(
            Create(left_panel),
            Create(right_panel),
            Write(left_formulas),
            Write(right_phasor)
        )
        self.wait(2)
        
        # [0:20–1:05] Trig vs Phasor
        trig_example = MathTex(
            r"\sin(\omega t+45^\circ) = \sin(\omega t)\cos45^\circ + \cos(\omega t)\sin45^\circ"
        ).shift(UP*2)
        phasor_example = MathTex(
            r"100\angle0^\circ + 80\angle45^\circ = ?"
        ).next_to(trig_example, DOWN, buff=0.8)
        
        self.play(
            Transform(left_formulas, trig_example),
            Transform(right_phasor, phasor_example)
        )
        self.wait(3)
        
        # [1:05–1:50] Montage industri - TAMBAH FADEOUT
        industries = VGroup(
            Text("Generator", font_size=24),
            Text("Relay Proteksi", font_size=24),
            Text("Power Analyzer", font_size=24),
            Text("3-Phase System", font_size=24)
        ).arrange(RIGHT, buff=0.5).shift(DOWN*1)
        
        self.play(
            FadeOut(left_formulas),
            FadeOut(right_phasor),
            FadeOut(left_panel),
            FadeOut(right_panel),
            FadeIn(industries)
        )
        self.wait(2)
        
        # [1:50–2:25] Daftar kuliah & industri - TAMBAH FADEOUT
        courses = BulletedList(
            "Rangkaian AC", "Sistem Tenaga", "Mesin Listrik", "Proteksi", "Elektronika Daya",
            font_size=24
        ).shift(LEFT*3 + UP*0.5)
        
        industrial_apps = BulletedList(
            "Load Flow Analysis", "Relay Setting", "Power Quality", "Motor Control",
            font_size=24
        ).shift(RIGHT*3 + UP*0.5)
        
        self.play(
            FadeOut(industries),
            Write(courses),
            Write(industrial_apps)
        )
        self.wait(3)
        
        # [2:25–2:40] Statistik teks - TAMBAH FADEOUT
        stat_text = Text(
            "Banyak mahasiswa bisa menghitung,\ntapi tidak paham kenapa harus kompleks",
            font_size=28, color=RED
        ).shift(UP*0.5)
        
        consequence = Text(
            "Hafal rumus, tapi kosong makna",
            font_size=32, color=RED
        ).next_to(stat_text, DOWN, buff=0.8)
        
        self.play(
            FadeOut(courses),
            FadeOut(industrial_apps),
            Write(stat_text),
            Write(consequence)
        )
        self.wait(2)
        
        # [2:40–3:00] Title card - TAMBAH FADEOUT
        title = Text(
            "Kenapa Ada Bilangan Kompleks di AC?",
            font_size=36, color=YELLOW
        )
        subtitle = Text(
            "Dari Fenomena ke Aplikasi Industri",
            font_size=24, color=WHITE
        ).next_to(title, DOWN, buff=0.5)
        
        self.play(
            FadeOut(stat_text),
            FadeOut(consequence),
            Write(title),
            Write(subtitle)
        )
        self.wait(3)
        
        # Clear everything at the end
        self.play(FadeOut(title), FadeOut(subtitle))

# ============================================
# SEGMEN 2: FENOMENA FISIK (±6 menit)
# ============================================

class Segment2_FenomenaFisik(Scene):
    def construct(self):
        # [8:00–8:40] Osiloskop 3 fasa
        axes = Axes(
            x_range=[0, 2*np.pi, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE}
        )
        
        # Tiga gelombang sinus
        def sine_wave(x, phase=0):
            return np.sin(x + phase)
        
        wave_R = axes.plot(lambda x: sine_wave(x, 0), color=RED)
        wave_S = axes.plot(lambda x: sine_wave(x, -2*np.pi/3), color=GREEN)
        wave_T = axes.plot(lambda x: sine_wave(x, -4*np.pi/3), color=BLUE)
        
        labels = VGroup(
            Text("R", color=RED).next_to(wave_R, UP),
            Text("S", color=GREEN).next_to(wave_S, UP),
            Text("T", color=BLUE).next_to(wave_T, UP)
        )
        
        self.play(Create(axes))
        self.play(
            Create(wave_R),
            Create(wave_S),
            Create(wave_T),
            Write(labels)
        )
        self.wait(2)
        
        # [8:40–9:40] Persamaan matematis
        equations = VGroup(
            MathTex(r"v_R(t) = 100\sin(\omega t)"),
            MathTex(r"v_S(t) = 100\sin(\omega t - 120^\circ)"),
            MathTex(r"v_T(t) = 100\sin(\omega t - 240^\circ)")
        ).arrange(DOWN, buff=0.5).shift(RIGHT*3)
        
        question = Text(
            "Berapa total tegangan di titik tertentu?",
            font_size=28,
            color=YELLOW
        ).shift(DOWN*2)
        
        self.play(Write(equations))
        self.play(Write(question))
        self.wait(2)
        
        # [9:40–10:20] Langkah trig manual
        trig_steps = VGroup(
            MathTex(r"1.\ \text{Ekspansi: } \sin(\omega t - 120^\circ)"),
            MathTex(r"2.\ \sin(\omega t)\cos120^\circ - \cos(\omega t)\sin120^\circ"),
            MathTex(r"3.\ -\frac{1}{2}\sin(\omega t) - \frac{\sqrt{3}}{2}\cos(\omega t)"),
            MathTex(r"4.\ \text{Ulangi untuk } -240^\circ"),
            MathTex(r"5.\ \text{Gabungkan semua suku}"),
            MathTex(r"6.\ \text{Sederhanakan}")
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.8).shift(LEFT*3)
        
        self.play(
            FadeOut(question),
            Write(trig_steps)
        )
        
        # Animate steps one by one
        for i in range(6):
            self.play(trig_steps[i].animate.set_color(YELLOW))
            self.wait(0.5)
            if i < 5:
                self.play(trig_steps[i].animate.set_color(WHITE))
        
        self.wait(1)
        
        # [10:20–11:00] Stopwatch
        stopwatch_text = Text(
            "Bayangkan bukan 3, tapi 10 atau 100 beban...",
            font_size=24,
            color=RED
        ).shift(DOWN*2)
        
        self.play(Write(stopwatch_text))
        
        # Count from 1 to 10
        counter = Text("3 gelombang", font_size=32, color=WHITE).shift(DOWN*3)
        self.play(Write(counter))
        
        for i in range(4, 11):
            self.wait(0.3)
            self.play(
                counter.animate.become(
                    Text(f"{i} gelombang", font_size=32, color=RED)
                )
            )
        
        self.wait(1)
        self.play(FadeOut(counter), FadeOut(stopwatch_text))
        
        # [11:00–12:00] Perbandingan trig vs phasor
        trig_side = VGroup(
            Text("Trigonometry:", font_size=28, color=RED),
            MathTex(r"5-10\ \text{langkah}"),
            MathTex(r"\text{Rumit untuk banyak gelombang}"),
            MathTex(r"\text{Rentan error}")
        ).arrange(DOWN, buff=0.4).shift(LEFT*3.5)
        
        phasor_side = VGroup(
            Text("Phasor:", font_size=28, color=GREEN),
            MathTex(r"\tilde{V}_{total} = \tilde{V}_R + \tilde{V}_S + \tilde{V}_T"),
            MathTex(r"1\ \text{baris operasi}"),
            MathTex(r"\text{Skalabel untuk 100+ gelombang}")
        ).arrange(DOWN, buff=0.4).shift(RIGHT*3.5)
        
        separator = Line(UP*3, DOWN*3, color=WHITE)
        
        self.play(
            FadeOut(axes), FadeOut(wave_R), FadeOut(wave_S), FadeOut(wave_T),
            FadeOut(labels), FadeOut(equations), FadeOut(trig_steps)
        )
        
        self.play(
            Create(separator),
            Write(trig_side),
            Write(phasor_side)
        )
        self.wait(3)
        
        # [12:00–12:40] Case industri: load flow 100 bus
        bus_diagram = VGroup(
            Circle(radius=0.1, color=BLUE).shift(LEFT*2 + UP),
            Circle(radius=0.1, color=BLUE).shift(UP*1.5),
            Circle(radius=0.1, color=BLUE).shift(RIGHT*2 + UP),
            # Add more circles for 100 bus
        )
        
        bus_text = Text(
            "Load Flow 100 Bus:",
            font_size=28,
            color=YELLOW
        ).shift(UP*2)
        
        trig_calc = Text(
            "Trig: Ribuan langkah,\nmembutuhkan waktu lama",
            font_size=24,
            color=RED
        ).shift(DOWN*1)
        
        phasor_calc = Text(
            "Phasor: 300 persamaan sederhana,\ncepat diotomasi komputer",
            font_size=24,
            color=GREEN
        ).next_to(trig_calc, DOWN, buff=0.8)
        
        self.play(
            FadeOut(separator),
            FadeOut(trig_side),
            FadeOut(phasor_side)
        )
        
        self.play(Write(bus_text))
        self.play(Create(bus_diagram))
        self.wait(1)
        self.play(Write(trig_calc))
        self.wait(1)
        self.play(Write(phasor_calc))
        self.wait(2)
        
        # [12:40–14:00] Transition ke visualisasi
        self.play(
            FadeOut(bus_text),
            FadeOut(bus_diagram),
            FadeOut(trig_calc),
            FadeOut(phasor_calc)
        )
        
        transition_text = Text(
            "Sekarang Anda sudah melihat masalahnya.\n"
            "Tahap berikutnya: VISUALISASI\n"
            "Mengapa sinus bisa direpresentasikan sebagai vektor berputar",
            font_size=28,
            color=YELLOW
        )
        
        self.play(Write(transition_text))
        self.wait(3)

# ============================================
# SEGMEN 3: VISUALISASI (±9 menit)
# ============================================

class Segment3_Visualisasi(Scene):
    def construct(self):
        # [14:00–14:50] Satu gelombang sinus dan vektor berputar
        axes = Axes(
            x_range=[0, 2*np.pi, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=7,
            y_length=4
        ).shift(LEFT*3)
        
        sine_wave = axes.plot(lambda x: np.sin(x), color=BLUE)
        sine_label = Text("Gelombang Sinus", font_size=20, color=BLUE).next_to(axes, DOWN)
        
        # Complex plane untuk vektor
        complex_plane = ComplexPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=4,
            y_length=4,
            background_line_style={"stroke_opacity": 0.3}
        ).shift(RIGHT*3)
        
        # Vektor yang berputar
        vector = Arrow(
            complex_plane.coords_to_point(0, 0),
            complex_plane.coords_to_point(1, 0),
            color=RED,
            buff=0
        )
        
        vector_label = MathTex(r"\tilde{V}").next_to(vector.get_end(), RIGHT)
        
        self.play(
            Create(axes),
            Create(sine_wave),
            Write(sine_label),
            Create(complex_plane),
            Create(vector),
            Write(vector_label)
        )
        
        # [14:50–15:40] Animasi vektor berputar dan proyeksi
        dot = Dot(color=YELLOW).move_to(axes.c2p(0, 0))
        trace = TracedPath(dot.get_center, stroke_color=YELLOW, stroke_width=2)
        
        self.add(trace, dot)
        
        # Animate rotation
        for theta in np.linspace(0, 2*np.pi, 25):
            new_vector_end = complex_plane.coords_to_point(np.cos(theta), np.sin(theta))
            new_dot_pos = axes.c2p(theta, np.sin(theta))
            
            self.play(
                vector.animate.put_start_and_end_on(
                    complex_plane.coords_to_point(0, 0),
                    new_vector_end
                ),
                dot.animate.move_to(new_dot_pos),
                vector_label.animate.next_to(new_vector_end, RIGHT),
                rate_func=linear,
                run_time=0.1
            )
        
        self.wait(1)
        
        # [15:40–16:50] Dua vektor berbeda
        self.play(
            FadeOut(axes), FadeOut(sine_wave), FadeOut(sine_label),
            FadeOut(dot), FadeOut(trace)
        )
        
        # Complex plane untuk dua vektor
        complex_plane_full = ComplexPlane(
            x_range=[-2, 2, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=8
        )
        
        vector1 = Arrow(
            ORIGIN, [1.5, 0, 0],
            color=RED,
            buff=0
        )
        vector1_label = MathTex(r"\tilde{V}_1 = 100\angle0^\circ", color=RED).next_to(vector1.get_end(), RIGHT)
        
        vector2 = Arrow(
            ORIGIN, [np.sqrt(2)/2, np.sqrt(2)/2, 0],
            color=GREEN,
            buff=0
        )
        vector2_label = MathTex(r"\tilde{V}_2 = 80\angle45^\circ", color=GREEN).next_to(vector2.get_end(), UP)
        
        self.play(
            Transform(complex_plane, complex_plane_full),
            Transform(vector, vector1),
            Transform(vector_label, vector1_label)
        )
        
        self.play(
            Create(vector2),
            Write(vector2_label)
        )
        self.wait(2)
        
        # [16:50–17:40] Penjumlahan vektor tip-to-tail
        vector2_copy = vector2.copy()
        
        # Move vector2 to tip of vector1
        self.play(
            vector2_copy.animate.shift(vector1.get_end())
        )
        
        # Resultant vector
        resultant = Arrow(
            ORIGIN, vector1.get_end() + vector2.get_end(),
            color=YELLOW,
            buff=0
        )
        resultant_label = MathTex(r"\tilde{V}_{total}", color=YELLOW).next_to(resultant.get_end(), UR)
        
        self.play(Create(resultant), Write(resultant_label))
        self.wait(2)
        
        # [17:40–18:30] Proyeksi menjadi gelombang sinus baru
        self.play(
            FadeOut(vector2_copy),
            FadeOut(vector1),
            FadeOut(vector2),
            FadeOut(vector1_label),
            FadeOut(vector2_label),
            resultant.animate.move_to(ORIGIN)
        )
        
        # Kembalikan axes untuk gelombang
        new_axes = Axes(
            x_range=[0, 2*np.pi, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=4
        ).shift(DOWN*2)
        
        new_sine = new_axes.plot(
            lambda x: np.linalg.norm(resultant.get_end()[:2]) * np.sin(x + np.arctan2(resultant.get_end()[1], resultant.get_end()[0])),
            color=YELLOW
        )
        
        self.play(
            Create(new_axes),
            Create(new_sine)
        )
        
        self.wait(2)
        
        # [18:30–19:55] Koordinat kartesius ke complex plane
        self.play(
            FadeOut(new_axes),
            FadeOut(new_sine)
        )
        
        # Highlight sumbu real dan imajiner
        real_axis = Arrow(
            complex_plane.coords_to_point(-2, 0),
            complex_plane.coords_to_point(2, 0),
            color=BLUE,
            buff=0
        )
        imag_axis = Arrow(
            complex_plane.coords_to_point(0, -2),
            complex_plane.coords_to_point(0, 2),
            color=GREEN,
            buff=0
        )
        
        real_label = MathTex(r"\text{Re} = \text{Real}", color=BLUE).next_to(real_axis, RIGHT)
        imag_label = MathTex(r"\text{Im} = \text{Imaginer}", color=GREEN).next_to(imag_axis, UP)
        
        self.play(
            Create(real_axis),
            Create(imag_axis),
            Write(real_label),
            Write(imag_label)
        )
        
        # Komponen rectangular dari vektor
        comp_x = DashedLine(
            complex_plane.coords_to_point(0, resultant.get_end()[1]),
            resultant.get_end(),
            color=GRAY
        )
        comp_y = DashedLine(
            complex_plane.coords_to_point(resultant.get_end()[0], 0),
            resultant.get_end(),
            color=GRAY
        )
        
        self.play(Create(comp_x), Create(comp_y))
        
        comp_labels = VGroup(
            MathTex(r"a = \text{Re}").next_to(comp_x, DOWN),
            MathTex(r"b = \text{Im}").next_to(comp_y, LEFT)
        )
        
        self.play(Write(comp_labels))
        self.wait(2)
        
        # [19:55–20:45] Tiga bentuk penulisan
        self.play(
            FadeOut(real_axis), FadeOut(imag_axis), FadeOut(real_label), FadeOut(imag_label),
            FadeOut(comp_x), FadeOut(comp_y), FadeOut(comp_labels),
            FadeOut(resultant), FadeOut(resultant_label)
        )
        
        forms = VGroup(
            MathTex(r"1.\ \text{Rectangular: } Z = a + jb"),
            MathTex(r"2.\ \text{Polar: } Z = R \angle \theta"),
            MathTex(r"3.\ \text{Euler: } Z = R e^{j\theta}")
        ).arrange(DOWN, buff=0.5).scale(1.2)
        
        self.play(Write(forms[0]))
        self.wait(1)
        self.play(Write(forms[1]))
        self.wait(1)
        self.play(Write(forms[2]))
        self.wait(2)
        
        # [20:45–21:35] Highlight 'j = rotasi 90°'
        j_explanation = VGroup(
            MathTex(r"j = \sqrt{-1} \quad\text{(matematika)}"),
            MathTex(r"j = \text{rotasi } 90^\circ \quad\text{(domain AC)}")
        ).arrange(DOWN, buff=0.5)
        
        # Animasi rotasi dengan j
        dot_example = Dot(color=YELLOW)
        vector_example = Arrow(ORIGIN, [1, 0, 0], color=WHITE, buff=0)
        
        self.play(
            FadeOut(forms),
            Create(vector_example),
            Create(dot_example)
        )
        
        # Rotasi 90 derajat
        for _ in range(4):
            self.play(
                Rotate(vector_example, 90*DEGREES, about_point=ORIGIN),
                run_time=1
            )
            self.wait(0.5)
        
        self.play(
            Write(j_explanation[0]),
            Write(j_explanation[1])
        )
        self.wait(2)
        
        # [21:35–23:00] Ringkasan perbandingan dan transition
        summary = Text(
            "Kenapa bilangan kompleks lebih cepat?\n"
            "Karena mengubah problem gelombang\n"
            "menjadi problem vektor sederhana",
            font_size=28,
            color=YELLOW
        )
        
        self.play(
            FadeOut(vector_example),
            FadeOut(dot_example),
            FadeOut(j_explanation),
            Write(summary)
        )
        self.wait(3)
        
        next_topic = Text(
            "Selanjutnya: MAKNA FISIS\n"
            "Apa arti real dan imajiner dalam dunia nyata?",
            font_size=24,
            color=GREEN
        ).next_to(summary, DOWN, buff=1)
        
        self.play(Write(next_topic))
        self.wait(3)

# ============================================
# SEGMEN 4: MAKNA FISIS (±9 menit)
# ============================================

class Segment4_MaknaFisis(Scene):
    def construct(self):
        # [23:00–23:55] Complex plane dengan R dan jX
        complex_plane = ComplexPlane(
            x_range=[-1, 3, 0.5],
            y_range=[-2, 2, 0.5],
            x_length=8,
            y_length=6
        )
        
        # Vektor impedansi
        vector = Arrow(
            ORIGIN, [2, 1.5, 0],
            color=YELLOW,
            buff=0,
            stroke_width=4
        )
        
        # Komponen
        comp_x = DashedLine(ORIGIN, [2, 0, 0], color=BLUE)
        comp_y = DashedLine([2, 0, 0], [2, 1.5, 0], color=GREEN)
        
        labels = VGroup(
            MathTex(r"R", color=BLUE).next_to(comp_x, DOWN),
            MathTex(r"jX", color=GREEN).next_to(comp_y, RIGHT),
            MathTex(r"Z = R + jX", color=YELLOW).next_to(vector.get_end(), UR)
        )
        
        title = Text("Impedansi dalam Bidang Kompleks", font_size=28, color=WHITE).to_edge(UP)
        
        self.play(Create(complex_plane))
        self.play(Write(title))
        self.play(
            Create(vector),
            Create(comp_x),
            Create(comp_y),
            Write(labels)
        )
        self.wait(2)
        
        # [23:55–24:50] Diagram impedansi dan makna
        explanation = VGroup(
            Text("R = Resistansi", color=BLUE, font_size=24),
            Text("Membuang energi (menjadi panas)", font_size=20),
            Text("jX = Reaktansi", color=GREEN, font_size=24),
            Text("Menyimpan & mengembalikan energi", font_size=20)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        self.play(Write(explanation))
        self.wait(3)
        
        # [24:50–26:00] Animasi operator j sebagai rotasi
        self.play(
            FadeOut(explanation),
            FadeOut(title),
            FadeOut(comp_x),
            FadeOut(comp_y),
            labels.animate.shift(UP*2)
        )
        
        rot_title = Text("Operator j = Rotasi 90°", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(rot_title))
        
        # Vektor awal
        vector_base = Arrow(ORIGIN, [1, 0, 0], color=WHITE, buff=0)
        vector_base_label = MathTex(r"\tilde{V}", color=WHITE).next_to(vector_base.get_end(), RIGHT)
        
        # Hasil perkalian dengan j
        vector_j = Arrow(ORIGIN, [0, 1, 0], color=GREEN, buff=0)
        vector_j_label = MathTex(r"j\tilde{V}", color=GREEN).next_to(vector_j.get_end(), UP)
        
        # Hasil perkalian dengan j²
        vector_j2 = Arrow(ORIGIN, [-1, 0, 0], color=RED, buff=0)
        vector_j2_label = MathTex(r"j^2\tilde{V} = -\tilde{V}", color=RED).next_to(vector_j2.get_end(), LEFT)
        
        self.play(
            Create(vector_base),
            Write(vector_base_label)
        )
        self.wait(1)
        
        self.play(
            Transform(vector_base, vector_j),
            Transform(vector_base_label, vector_j_label)
        )
        self.wait(1)
        
        self.play(
            Transform(vector_base, vector_j2),
            Transform(vector_base_label, vector_j2_label)
        )
        self.wait(2)
        
        # [26:00–27:10] Komponen R, L, C dengan fase
        self.play(
            FadeOut(vector_base),
            FadeOut(vector_base_label),
            FadeOut(rot_title),
            labels.animate.shift(DOWN*2)
        )
        
        components = VGroup(
            VGroup(
                Rectangle(height=1, width=2, color=BLUE),
                Text("Resistor", font_size=20),
                MathTex(r"Z_R = R", color=BLUE),
                MathTex(r"V\text{ dan }I\text{ sefasa}")
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Rectangle(height=1, width=2, color=GREEN),
                Text("Induktor", font_size=20),
                MathTex(r"Z_L = j\omega L", color=GREEN),
                MathTex(r"V\text{ mendahului }I\ 90^\circ")
            ).arrange(DOWN, buff=0.2),
            
            VGroup(
                Rectangle(height=1, width=2, color=RED),
                Text("Kapasitor", font_size=20),
                MathTex(r"Z_C = -j\frac{1}{\omega C}", color=RED),
                MathTex(r"I\text{ mendahului }V\ 90^\circ")
            ).arrange(DOWN, buff=0.2)
        ).arrange(RIGHT, buff=0.5).shift(DOWN*1)
        
        self.play(FadeIn(components))
        self.wait(3)
        
        # [27:10–28:25] Segitiga impedansi
        self.play(
            FadeOut(components),
            FadeOut(complex_plane),
            FadeOut(vector),
            FadeOut(labels)
        )
        
        # Segitiga impedansi
        triangle = Polygon(
            [0, 0, 0],
            [3, 0, 0],
            [3, 2, 0],
            color=WHITE
        )
        
        triangle_labels = VGroup(
            MathTex(r"R", color=BLUE).next_to(triangle.get_center(), DOWN),
            MathTex(r"X", color=GREEN).next_to(triangle.get_center(), RIGHT),
            MathTex(r"|Z|", color=YELLOW).next_to(triangle.get_center(), UL),
            MathTex(r"\theta", color=RED).move_to([2.8, 0.3, 0])
        )
        
        formulas = VGroup(
            MathTex(r"|Z| = \sqrt{R^2 + X^2}"),
            MathTex(r"\theta = \arctan\left(\frac{X}{R}\right)"),
            MathTex(r"\text{Power Factor} = \cos\theta")
        ).arrange(DOWN, buff=0.5).shift(RIGHT*3)
        
        self.play(Create(triangle))
        self.play(Write(triangle_labels))
        self.wait(1)
        self.play(Write(formulas))
        self.wait(2)
        
        # [28:25–29:20] Segitiga daya
        self.play(
            FadeOut(triangle),
            FadeOut(triangle_labels),
            FadeOut(formulas)
        )
        
        # Segitiga daya
        power_triangle = Polygon(
            [0, 0, 0],
            [4, 0, 0],
            [4, 3, 0],
            color=WHITE
        )
        
        power_labels = VGroup(
            MathTex(r"P = \text{Daya Nyata (W)}", color=BLUE).next_to(power_triangle.get_center(), DOWN),
            MathTex(r"Q = \text{Daya Reaktif (VAR)}", color=GREEN).next_to(power_triangle.get_center(), RIGHT),
            MathTex(r"S = \text{Daya Semu (VA)}", color=YELLOW).next_to(power_triangle.get_center(), UL),
            MathTex(r"\theta = \text{Sudut Daya}", color=RED).move_to([3.8, 0.3, 0])
        )
        
        power_formula = MathTex(r"S = P + jQ").scale(1.5).shift(DOWN*2)
        
        self.play(Create(power_triangle))
        self.play(Write(power_labels))
        self.wait(1)
        self.play(Write(power_formula))
        self.wait(2)
        
        # [29:20–30:10] Contoh power factor
        example = VGroup(
            Text("Contoh: Faktor Daya = 0.6", font_size=28, color=YELLOW),
            MathTex(r"\cos\theta = 0.6 \Rightarrow \theta \approx 53^\circ"),
            Text("Banyak energi bolak-balik", font_size=24, color=RED),
            Text("tidak berubah menjadi kerja nyata", font_size=24, color=RED)
        ).arrange(DOWN, buff=0.5)
        
        self.play(
            FadeOut(power_triangle),
            FadeOut(power_labels),
            FadeOut(power_formula),
            Write(example)
        )
        self.wait(3)
        
        # [30:10–30:50] Recap poin makna fisis
        recap = VGroup(
            Text("Ringkasan Makna Fisis:", font_size=32, color=YELLOW),
            Text("• Real part → dissipasi energi", font_size=24, color=BLUE),
            Text("• Imaginary part → penyimpanan energi", font_size=24, color=GREEN),
            Text("• Magnitude → besar total", font_size=24, color=WHITE),
            Text("• Phase → timing antar gelombang", font_size=24, color=RED)
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        
        self.play(
            FadeOut(example),
            Write(recap)
        )
        self.wait(3)
        
        # [30:50–32:00] Transition ke model matematis
        transition = Text(
            "Sekarang maknanya sudah jelas.\n"
            "Selanjutnya: MODEL MATEMATIS\n"
            "Bagaimana rumus diturunkan dari fisika dasar",
            font_size=28,
            color=GREEN
        )
        
        self.play(
            FadeOut(recap),
            Write(transition)
        )
        self.wait(3)

# ============================================
# SEGMEN 5: MODEL MATEMATIS (±8 menit)
# ============================================

class Segment5_ModelMatematis(Scene):
    def construct(self):
        # [32:00–32:40] Rangkaian RLC seri sederhana
        circuit = VGroup(
            # Sumber AC
            Circle(radius=0.3, color=YELLOW),
            # Resistor
            Rectangle(height=0.5, width=1, color=BLUE).shift(RIGHT*1.5),
            # Induktor
            Arc(radius=0.2, angle=2*PI, color=GREEN).shift(RIGHT*3),
            # Kapasitor
            Line(UP*0.3, DOWN*0.3, color=RED).shift(RIGHT*4.5),
            Line(UP*0.3, DOWN*0.3, color=RED).shift(RIGHT*4.5 + RIGHT*0.3),
            # Garis penghubung
            Line(ORIGIN, RIGHT*1.2, color=WHITE),
            Line(RIGHT*1.8, RIGHT*2.8, color=WHITE),
            Line(RIGHT*3.2, RIGHT*4.2, color=WHITE),
            Line(RIGHT*4.8, RIGHT*6, color=WHITE),
            Line(RIGHT*6, DOWN*1 + LEFT*6, color=WHITE),
            Line(DOWN*1, ORIGIN, color=WHITE)
        )
        
        labels = VGroup(
            MathTex(r"v_s(t)").next_to(circuit[0], UP),
            MathTex(r"R").next_to(circuit[1], UP),
            MathTex(r"L").next_to(circuit[2], UP),
            MathTex(r"C").next_to(circuit[3], UP)
        )
        
        title = Text("Rangkaian RLC Seri", font_size=32, color=YELLOW).to_edge(UP)
        
        self.play(Create(circuit))
        self.play(Write(labels))
        self.play(Write(title))
        self.wait(2)
        
        # [32:40–33:35] Resistor
        resistor_eq = VGroup(
            MathTex(r"\text{Hukum Ohm:}"),
            MathTex(r"v_R(t) = R \cdot i(t)"),
            MathTex(r"\text{Dalam domain phasor:}"),
            MathTex(r"\tilde{V}_R = R \cdot \tilde{I}"),
            MathTex(r"Z_R = R", color=BLUE)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        self.play(Write(resistor_eq))
        self.wait(2)
        
        # [33:35–34:45] Induktor
        inductor_eq = VGroup(
            MathTex(r"\text{Hukum Faraday:}"),
            MathTex(r"v_L(t) = L \frac{di(t)}{dt}"),
            MathTex(r"\text{Misal } i(t) = I_m\sin(\omega t):"),
            MathTex(r"v_L(t) = \omega L I_m\cos(\omega t)"),
            MathTex(r"= \omega L I_m\sin(\omega t + 90^\circ)"),
            MathTex(r"Z_L = j\omega L", color=GREEN)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        self.play(
            Transform(resistor_eq, inductor_eq)
        )
        self.wait(3)
        
        # [34:45–36:00] Kapasitor
        capacitor_eq = VGroup(
            MathTex(r"\text{Hukum Kapasitor:}"),
            MathTex(r"i_C(t) = C \frac{dv_C(t)}{dt}"),
            MathTex(r"v_C(t) = \frac{1}{C}\int i_C(t) dt"),
            MathTex(r"\text{Misal } i(t) = I_m\sin(\omega t):"),
            MathTex(r"v_C(t) = -\frac{1}{\omega C} I_m\cos(\omega t)"),
            MathTex(r"= \frac{1}{\omega C} I_m\sin(\omega t - 90^\circ)"),
            MathTex(r"Z_C = -j\frac{1}{\omega C}", color=RED)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        self.play(
            Transform(resistor_eq, capacitor_eq)
        )
        self.wait(3)
        
        # [36:00–36:55] Gabungan RLC
        self.play(
            FadeOut(resistor_eq),
            FadeOut(title)
        )
        
        total_eq = VGroup(
            Text("Impedansi Total RLC Seri:", font_size=28, color=YELLOW),
            MathTex(r"Z_{total} = Z_R + Z_L + Z_C"),
            MathTex(r"= R + j\omega L - j\frac{1}{\omega C}"),
            MathTex(r"= R + j\left(\omega L - \frac{1}{\omega C}\right)"),
            MathTex(r"= R + jX", color=WHITE)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(total_eq))
        self.wait(3)
        
        # [36:55–37:50] Konversi rectangular ke polar
        conversion = VGroup(
            Text("Konversi ke Bentuk Polar:", font_size=28, color=GREEN),
            MathTex(r"|Z| = \sqrt{R^2 + X^2}"),
            MathTex(r"\theta = \arctan\left(\frac{X}{R}\right)"),
            Text("Magnitude menentukan besar arus", font_size=20, color=BLUE),
            Text("Sudut menentukan hubungan fase V dan I", font_size=20, color=RED)
        ).arrange(DOWN, buff=0.4).shift(DOWN*1)
        
        self.play(Write(conversion))
        self.wait(3)
        
        # [37:50–38:45] Contoh numerik
        example = VGroup(
            Text("Contoh Numerik:", font_size=28, color=YELLOW),
            MathTex(r"R = 10\ \Omega,\quad L = 0.05\ H,\quad C = 100\ \mu F"),
            MathTex(r"f = 50\ Hz \Rightarrow \omega = 2\pi f = 314\ rad/s"),
            MathTex(r"X_L = \omega L = 15.7\ \Omega"),
            MathTex(r"X_C = \frac{1}{\omega C} = 31.8\ \Omega"),
            MathTex(r"X = X_L - X_C = -16.1\ \Omega\ (\text{kapasitif})"),
            MathTex(r"|Z| = \sqrt{10^2 + (-16.1)^2} = 19.0\ \Omega"),
            MathTex(r"\theta = \arctan\left(\frac{-16.1}{10}\right) = -58.1^\circ")
        ).arrange(DOWN, buff=0.2).scale(0.8).shift(DOWN*1)
        
        self.play(
            FadeOut(total_eq),
            FadeOut(conversion),
            Write(example)
        )
        self.wait(4)
        
        # [38:45–39:25] Cheatsheet rumus
        self.play(
            FadeOut(circuit),
            FadeOut(labels),
            FadeOut(example)
        )
        
        cheatsheet = VGroup(
            Text("Cheatsheet Rumus Impedansi:", font_size=32, color=YELLOW),
            MathTex(r"Z_R = R", color=BLUE),
            MathTex(r"Z_L = j\omega L", color=GREEN),
            MathTex(r"Z_C = -j\frac{1}{\omega C}", color=RED),
            MathTex(r"Z_{total} = R + jX", color=WHITE),
            Text("Ini bukan sekadar rumus.", font_size=24),
            Text("Ini cara membaca perilaku fisik rangkaian.", font_size=24, color=GREEN)
        ).arrange(DOWN, buff=0.4)
        
        self.play(Write(cheatsheet))
        self.wait(3)
        
        # [39:25–40:00] Transition ke simulasi
        transition = Text(
            "Sekarang kita uji semua rumus ini\n"
            "melalui SIMULASI interaktif",
            font_size=32,
            color=YELLOW
        )
        
        self.play(
            FadeOut(cheatsheet),
            Write(transition)
        )
        self.wait(3)

# ============================================
# SEGMEN 6: SIMULASI & APLIKASI (±15 menit)
# ============================================

class Segment6_SimulasiAplikasi(Scene):
    def construct(self):
        # [40:00–40:25] Simulator interface
        simulator_frame = Rectangle(
            height=5, width=8,
            color=BLUE,
            stroke_width=3
        )
        
        title = Text("Simulator RLC Interaktif", font_size=32, color=YELLOW).to_edge(UP)
        
        # Sliders
        freq_slider = VGroup(
            Line(LEFT*2, RIGHT*2, color=WHITE),
            Triangle(color=GREEN).scale(0.1).move_to(LEFT*2)
        ).shift(UP*1)
        freq_label = Text("Frekuensi (Hz)", font_size=20).next_to(freq_slider, UP)
        
        cap_slider = VGroup(
            Line(LEFT*2, RIGHT*2, color=WHITE),
            Triangle(color=RED).scale(0.1).move_to(LEFT*1)
        ).shift(DOWN*0.5)
        cap_label = Text("Kapasitansi (μF)", font_size=20).next_to(cap_slider, UP)
        
        ind_slider = VGroup(
            Line(LEFT*2, RIGHT*2, color=WHITE),
            Triangle(color=GREEN).scale(0.1).move_to(RIGHT*1)
        ).shift(DOWN*2)
        ind_label = Text("Induktansi (H)", font_size=20).next_to(ind_slider, UP)
        
        # Diagram RLC
        circuit_diagram = VGroup(
            Circle(radius=0.2, color=YELLOW).shift(LEFT*3 + UP*2),
            Rectangle(height=0.3, width=0.8, color=BLUE).shift(LEFT*1.5 + UP*2),
            Arc(radius=0.15, angle=2*PI, color=GREEN).shift(LEFT*0 + UP*2),
            Line(UP*0.15, DOWN*0.15, color=RED).shift(RIGHT*1 + UP*2),
            Line(UP*0.15, DOWN*0.15, color=RED).shift(RIGHT*1 + UP*2 + RIGHT*0.2)
        )
        
        # Display values
        value_display = VGroup(
            Text("f = 50 Hz", font_size=20, color=GREEN),
            Text("C = 100 μF", font_size=20, color=RED),
            Text("L = 0.05 H", font_size=20, color=GREEN),
            Text("R = 10 Ω", font_size=20, color=BLUE)
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3 + UP*1)
        
        self.play(Create(simulator_frame))
        self.play(Write(title))
        self.play(
            Create(freq_slider),
            Write(freq_label),
            Create(cap_slider),
            Write(cap_label),
            Create(ind_slider),
            Write(ind_label),
            Create(circuit_diagram),
            Write(value_display)
        )
        self.wait(2)
        
        # [40:25–41:35] Simulasi perubahan parameter
        # Complex plane untuk phasor
        phasor_plane = ComplexPlane(
            x_range=[-2, 2, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=4,
            y_length=3
        ).shift(DOWN*2 + LEFT*2)
        
        voltage_phasor = Arrow(
            phasor_plane.coords_to_point(0, 0),
            phasor_plane.coords_to_point(1, 0.5),
            color=YELLOW,
            buff=0
        )
        
        current_phasor = Arrow(
            phasor_plane.coords_to_point(0, 0),
            phasor_plane.coords_to_point(0.8, -0.3),
            color=TEAL,
            buff=0
        )
        
        phase_angle = Arc(
            radius=0.5,
            start_angle=0,
            angle=np.arctan2(0.5, 1) - np.arctan2(-0.3, 0.8),
            color=RED
        ).move_to(phasor_plane.coords_to_point(0, 0))
        
        angle_label = MathTex(r"\theta = 45^\circ", color=RED, font_size=20).next_to(phase_angle, RIGHT)
        
        self.play(
            Create(phasor_plane),
            Create(voltage_phasor),
            Create(current_phasor),
            Create(phase_angle),
            Write(angle_label)
        )
        
        # [41:35–42:45] Naikkan frekuensi
        self.play(
            freq_slider[1].animate.move_to(RIGHT*2),  # Pindah slider ke kanan
            value_display[0].animate.become(Text("f = 100 Hz", font_size=20, color=GREEN))
        )
        
        # Update phasor
        new_voltage_phasor = Arrow(
            phasor_plane.coords_to_point(0, 0),
            phasor_plane.coords_to_point(1.2, 0.8),
            color=YELLOW,
            buff=0
        )
        
        self.play(
            Transform(voltage_phasor, new_voltage_phasor),
            Transform(phase_angle, Arc(
                radius=0.5,
                start_angle=0,
                angle=np.arctan2(0.8, 1.2) - np.arctan2(-0.3, 0.8),
                color=RED
            ).move_to(phasor_plane.coords_to_point(0, 0))),
            angle_label.animate.become(MathTex(r"\theta = 60^\circ", color=RED, font_size=20).next_to(phase_angle, RIGHT))
        )
        self.wait(2)
        
        # [42:45–43:55] Cari resonansi
        self.play(
            freq_slider[1].animate.move_to(RIGHT*0.5),
            value_display[0].animate.become(Text("f = 71.2 Hz", font_size=20, color=GREEN))
        )
        
        resonant_phasor = Arrow(
            phasor_plane.coords_to_point(0, 0),
            phasor_plane.coords_to_point(1, 0),
            color=YELLOW,
            buff=0
        )
        
        self.play(
            Transform(voltage_phasor, resonant_phasor),
            Transform(phase_angle, Arc(
                radius=0.5,
                start_angle=0,
                angle=0,
                color=GREEN
            ).move_to(phasor_plane.coords_to_point(0, 0))),
            angle_label.animate.become(MathTex(r"\theta = 0^\circ\ (resonansi)", color=GREEN, font_size=20).next_to(phase_angle, RIGHT))
        )
        self.wait(2)
        
        # [43:55–45:05] Ubah kapasitansi
        self.play(
            cap_slider[1].animate.move_to(RIGHT*2),
            value_display[1].animate.become(Text("C = 200 μF", font_size=20, color=RED))
        )
        
        capacitive_phasor = Arrow(
            phasor_plane.coords_to_point(0, 0),
            phasor_plane.coords_to_point(0.8, -0.6),
            color=YELLOW,
            buff=0
        )
        
        self.play(
            Transform(voltage_phasor, capacitive_phasor),
            Transform(phase_angle, Arc(
                radius=0.5,
                start_angle=0,
                angle=np.arctan2(-0.6, 0.8),
                color=BLUE
            ).move_to(phasor_plane.coords_to_point(0, 0))),
            angle_label.animate.become(MathTex(r"\theta = -37^\circ\ (kapasitif)", color=BLUE, font_size=20).next_to(phase_angle, RIGHT))
        )
        self.wait(2)
        
        # [45:05–46:15] Ubah resistansi
        self.play(
            value_display[3].animate.become(Text("R = 20 Ω", font_size=20, color=BLUE))
        )
        
        # [46:15–47:05] Recap simulasi
        self.play(
            FadeOut(phasor_plane),
            FadeOut(voltage_phasor),
            FadeOut(current_phasor),
            FadeOut(phase_angle),
            FadeOut(angle_label),
            FadeOut(simulator_frame),
            FadeOut(title),
            FadeOut(freq_slider),
            FadeOut(freq_label),
            FadeOut(cap_slider),
            FadeOut(cap_label),
            FadeOut(ind_slider),
            FadeOut(ind_label),
            FadeOut(circuit_diagram),
            FadeOut(value_display)
        )
        
        recap_text = Text(
            "Simulasi membuktikan:\n"
            "Bilangan kompleks bukan teori abstrak.\n"
            "Ia menggambarkan perilaku sistem nyata.",
            font_size=28,
            color=YELLOW
        )
        
        self.play(Write(recap_text))
        self.wait(3)
        
        # [47:05–49:05] Studi kasus pabrik motor induksi
        case_study = VGroup(
            Text("Studi Kasus: Pabrik Motor Induksi", font_size=32, color=YELLOW),
            Text("Faktor Daya = 0.6", font_size=24, color=RED),
            Text("Tagihan listrik naik karena penalty", font_size=20, color=WHITE)
        ).arrange(DOWN, buff=0.4)
        
        self.play(
            FadeOut(recap_text),
            Write(case_study)
        )
        self.wait(2)
        
        # [49:05–50:15] Power triangle dan perhitungan
        power_triangle = Polygon(
            [0, 0, 0],
            [4, 0, 0],
            [4, 3, 0],
            color=WHITE
        ).shift(LEFT*2)
        
        power_labels = VGroup(
            MathTex(r"P = 50\ kW", color=BLUE).next_to(power_triangle.get_center(), DOWN),
            MathTex(r"Q = 66.7\ kVAR", color=GREEN).next_to(power_triangle.get_center(), RIGHT),
            MathTex(r"S = 83.3\ kVA", color=YELLOW).next_to(power_triangle.get_center(), UL),
            MathTex(r"\theta = 53^\circ", color=RED).move_to([3.8, 0.3, 0])
        )
        
        calculations = VGroup(
            MathTex(r"P = 50\ kW,\quad \cos\theta = 0.6"),
            MathTex(r"S = \frac{P}{\cos\theta} = \frac{50}{0.6} = 83.3\ kVA"),
            MathTex(r"Q = \sqrt{S^2 - P^2} = 66.7\ kVAR")
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        self.play(
            FadeOut(case_study),
            Create(power_triangle),
            Write(power_labels),
            Write(calculations)
        )
        self.wait(3)
        
        # [50:15–51:50] Tambahkan kapasitor bank
        correction = VGroup(
            Text("Koreksi Faktor Daya:", font_size=28, color=GREEN),
            MathTex(r"\text{Target: } \cos\theta = 0.95"),
            MathTex(r"Q_{baru} = P\tan(\arccos 0.95) \approx 16.5\ kVAR"),
            MathTex(r"Q_{kapasitor} = Q_{lama} - Q_{baru}"),
            MathTex(r"= 66.7 - 16.5 = 50.2\ kVAR")
        ).arrange(DOWN, buff=0.3).shift(RIGHT*3)
        
        capacitor_bank = Rectangle(
            height=1, width=3,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.3
        ).shift(DOWN*2)
        capacitor_label = Text("Kapasitor Bank 50 kVAR", font_size=20).next_to(capacitor_bank, UP)
        
        self.play(
            Transform(calculations, correction),
            Create(capacitor_bank),
            Write(capacitor_label)
        )
        self.wait(3)
        
        # [51:50–53:00] Before-after phasor
        before_after = VGroup(
            VGroup(
                Text("Sebelum:", font_size=24, color=RED),
                Arrow(ORIGIN, [2, 1.5, 0], color=RED, buff=0),
                MathTex(r"\theta = 53^\circ", color=RED)
            ).arrange(DOWN, buff=0.3),
            
            VGroup(
                Text("Sesudah:", font_size=24, color=GREEN),
                Arrow(ORIGIN, [2, 0.5, 0], color=GREEN, buff=0),
                MathTex(r"\theta = 18^\circ", color=GREEN)
            ).arrange(DOWN, buff=0.3)
        ).arrange(RIGHT, buff=2).shift(DOWN*1)
        
        benefits = VGroup(
            Text("Manfaat Koreksi:", font_size=24, color=YELLOW),
            Text("• Arus turun", font_size=20),
            Text("• Rugi-rugi I²R turun", font_size=20),
            Text("• Tagihan listrik berkurang", font_size=20),
            Text("• Kapasitas jaringan optimal", font_size=20)
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).shift(UP*1)
        
        self.play(
            FadeOut(power_triangle),
            FadeOut(power_labels),
            FadeOut(calculations),
            FadeOut(capacitor_bank),
            FadeOut(capacitor_label),
            Write(before_after),
            Write(benefits)
        )
        self.wait(3)
        
        # [53:00–53:50] Rekap 6 tahap
        self.play(
            FadeOut(before_after),
            FadeOut(benefits)
        )
        
        stages = VGroup(
            Text("REKAP 6 TAHAP PEMBELAJARAN:", font_size=32, color=YELLOW),
            Text("1) Fenomena: trigonometri tidak praktis", font_size=20),
            Text("2) Visualisasi: sinus = proyeksi vektor berputar", font_size=20),
            Text("3) Makna fisis: real & imajiner = dua dimensi nyata", font_size=20),
            Text("4) Model matematis: rumus diturunkan dari fisika", font_size=20),
            Text("5) Simulasi: verifikasi perilaku", font_size=20),
            Text("6) Aplikasi: kasus industri nyata", font_size=20)
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        
        self.play(Write(stages))
        self.wait(4)
        
        # [53:50–54:35] Closing statement
        closing = VGroup(
            Text("Sekarang Anda tidak lagi sekadar bisa menghitung.", font_size=28, color=WHITE),
            Text("Anda memahami bahasa kerja engineer.", font_size=32, color=YELLOW),
            Text("Dan itu yang membedakan", font_size=24, color=WHITE),
            Text("antara hafal dan paham.", font_size=32, color=GREEN)
        ).arrange(DOWN, buff=0.4)
        
        self.play(
            FadeOut(stages),
            Write(closing)
        )
        self.wait(3)
        
        # [54:35–55:00] CTA + teaser
        cta = VGroup(
            Text("Di modul berikutnya:", font_size=24, color=WHITE),
            Text("Sinyal dan Sistem", font_size=36, color=YELLOW),
            Text("Dengan fondasi ini,", font_size=20, color=WHITE),
            Text("semuanya akan jauh lebih masuk akal.", font_size=20, color=WHITE),
            Text("Terima kasih sudah mengikuti sampai akhir.", font_size=24, color=GREEN),
            Text("Sampai jumpa di episode berikutnya!", font_size=28, color=YELLOW)
        ).arrange(DOWN, buff=0.4)
        
        self.play(
            FadeOut(closing),
            Write(cta)
        )
        self.wait(5)

# ============================================
# RENDER INSTRUKSI
# ============================================
"""
Untuk merender setiap segmen secara terpisah, gunakan perintah:

manim -pqh manim_pengantar.py Segment1_PreModuleHook
manim -pqh manim_pengantar.py Segment2_FenomenaFisik
manim -pqh manim_pengantar.py Segment3_Visualisasi
manim -pqh manim_pengantar.py Segment4_MaknaFisis
manim -pqh manim_pengantar.py Segment5_ModelMatematis
manim -pqh manim_pengantar.py Segment6_SimulasiAplikasi

Untuk kualitas tinggi (1080p), ganti -pql dengan -pqh
Untuk merender semua sekaligus:
manim -pql script_nama.py -a

CATATAN:
1. Placeholder image harus diganti dengan gambar asli
2. Durasi animasi dapat disesuaikan dengan mengubah self.wait()
3. Warna dan ukuran font dapat disesuaikan sesuai preferensi
4. Beberapa bagian mungkin perlu penyesuaian untuk presisi matematis
5. Untuk simulasi interaktif nyata, mungkin perlu integrasi dengan library eksternal
"""