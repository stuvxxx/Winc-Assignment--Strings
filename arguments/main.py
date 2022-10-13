# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greet='Hello, <name>!'):
    return greet.replace("<name>", name)

def force(mass, body="earth"):
    surface_gravs = {
        "sun" : 274,
        "jupiter" : 24.9,
        "neptune" : 11.6,
        "saturn" : 10.4,
        "earth" : 9.8,
        "uranus" : 8.9,
        "venus" : 8.9,
        "mars" : 3.7,
        "mercury" : 3.7,
        "moon" : 1.6,
        "pluto" : 0.6
    }
    return mass*surface_gravs[body]

def pull(m1, m2, d):
    x = (m1*m2)/d**2
    return (6.674*10**-11)*x

