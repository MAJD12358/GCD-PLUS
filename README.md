# GCD+ Programming Language

GCD+ is a simple yet powerful programming language designed for creating interactive and dynamic applications with a focus on design.

## Getting Started

To start using GCD+, follow these steps:

1. Clone the repository.
2. Include the GCD+ interpreter in your project.
3. Write your GCD+ code using the provided syntax.
4. Run your application.

## Example GCD+ Code

```GCD+
# App Definition
$name#HelloWorldApp
+Topbar#AppHeader
Color#4285F4

# Design Elements
+Length+width : 200, 100

# App Components
+
#Image
Source# "logo.png"
Opacity#1.0
//
Text# "Hello, GCD+!"
Color#000000
Font#Arial
Size#18
//

# Custom Styling
$design
Border#2px solid #CCCCCC
BoxShadow#3px 3px 5px #888888
///

# Animation
$animate
FadeIn#1s
///

# Interaction
$interact
OnClick#ShowPopup("GCD+ Clicked!")
///
