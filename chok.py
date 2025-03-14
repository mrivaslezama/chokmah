from manimlib.imports import *

class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Chokma")
        second_line = TextMobject("store")
        final_line = TextMobject("Elite Sportware!", color=BLUE)
        color_final_line = TextMobject("Unleash Your Athletic Potential!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)

        #Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)