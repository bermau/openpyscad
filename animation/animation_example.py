# Example : Create an OpenSCAD animation directly from Python

# The animation functionality is based simply on an OpenSCAD variable $t
# that is changed automatically by OpenSCAD while repeatedly showing the model.
# To activate animation, select "View->Animate" from the OpenSCAD  menu;
# this will cause three fields to appear underneath the Preview console: Time, FPS & Steps.

# To commence animation, enter values into the FPS and Steps input
# fields (e.g. 50 FPS and 100 Steps for this animation).

# Although this is not intended to directly produce real-time animations
# but the image sequence can be exported to generate videos of the animation.

from openpyscad import *

# In this example, position will varie from 0 to 200 then 200 to 0, as time vay form 0 to 1
# The scat_str is an OpenSCAD string that will not be evaluated by Python, but written on the prologue
# of the OpenSCAD file.
scad_str = f"""
// The animation functionality is based simply on an OpenSCAD variable $t
// that is changed automatically by OpenSCAD while repeatedly showing the model.
// To activate animation, select "View->Animate" from the OpenSCAD  menu;
// this will cause three fields to appear
// underneath the Preview console: Time, FPS & Steps.
// To start animation, enter values into the FPS and Steps input
// fields (e.g. 50 FPS and 100 Steps for this animation).

// The image sequence can be exported to generate videos of the animation.


function position(time) = time < 0.5
      ? time * 400
      : 400/2 - ((time-0.5) * 400) ;

"""


U = Cube([15, 10, 50])
U += Cylinder(60, r=30).translate([Nonevaluated("position($t)"), -25, -30])

U.write("animated_cylinder.scad", prologue=scad_str)
