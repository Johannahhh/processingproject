
import time 
frame=0
last_frame = time.time()
images = []
def setup():
    global reset
    size(800, 600)

    intro = loadImage('intro.png')
    letter_a = loadImage('a.png')
    letter_b = loadImage('b.png')
    letter_c = loadImage('c.png')
    letter_d = loadImage('d.png')
    letter_e = loadImage('e.png')
    letter_f = loadImage('f.png')
    letter_g = loadImage('g.png')
    letter_h = loadImage('h.png')
    letter_i = loadImage('i.png')
    letter_j = loadImage('j.png')
    letter_k = loadImage('k.png')
    letter_l = loadImage('l.png')
    letter_m = loadImage('m.png')
    letter_n = loadImage('n.png')
    letter_o = loadImage('o.png')
    letter_p = loadImage('p.png')
    letter_q = loadImage('q.png')
    letter_r = loadImage('r.png')
    letter_s = loadImage('s.png')
    letter_t = loadImage('t.png')
    letter_u = loadImage('u.png')
    letter_v = loadImage('v.png')
    letter_w = loadImage('w.png')
    letter_x = loadImage('x.png')
    letter_y = loadImage('y.png')
    letter_z = loadImage('z.png')
    reset = loadImage('reset.png')

    images.append(intro)
    images.append(letter_a)
    images.append(letter_b)
    images.append(letter_c)
    images.append(letter_d)
    images.append(letter_e)   
    images.append(letter_f)   
    images.append(letter_g)   
    images.append(letter_h)   
    images.append(letter_i)    
    images.append(letter_j)   
    images.append(letter_k)   
    images.append(letter_l)   
    images.append(letter_m)   
    images.append(letter_n)   
    images.append(letter_o)   
    images.append(letter_p)   
    images.append(letter_q)   
    images.append(letter_r)   
    images.append(letter_s)   
    images.append(letter_t)   
    images.append(letter_u)   
    images.append(letter_v)   
    images.append(letter_w)   
    images.append(letter_x)   
    images.append(letter_y)   
    images.append(letter_z)


def draw():
    global frame, last_frame
    background(0)
    image(images[frame], 100, 100, 600, 400)
    image(reset, 600, 0, 200, 200)
    if (mousePressed and mouseX >600 and mouseY <200) :
        frame=0
        last_frame = time.time()
    if time.time() - last_frame > 2:
        frame = (frame + 1) % len(images)
        last_frame = time.time()                                                 
