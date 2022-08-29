from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# Designate our .kv design file
Builder.load_file("animations.kv")

class MyLayout(Widget):
    def animate_it(self, widget, *args):

        # Define the animation
        animate = Animation(
            background_color=(0,0,1,1),
            duration=.5
        )

        # Do second animation
        animate += Animation(
            size_hint= (1,1)
        )

        # Do third animation
        animate += Animation(
            size_hint = (.5,.5)
        )



        # Start the Animation
        animate.start(widget)

class AnimationsApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AnimationsApp().run()