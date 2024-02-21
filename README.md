# GCD+ Programming Language

GCD+ is an advanced programming language designed for modern and feature-rich applications.

## Getting Started

### Installation
To use GCD+, download the interpreter from [gcdplus.com/download](https://gcdplus.com/download) and follow the installation instructions.

### Hello World Example
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
