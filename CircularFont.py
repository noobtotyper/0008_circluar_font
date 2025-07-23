import cairo
from math import sqrt,ceil,pi,tau,cos,sin
import random

def draw_char(char,ctx:cairo.Context,line_width,mode="connected"):
    if mode =="connected":
        adjustment=0
    elif mode == "tangential":
        adjustment=line_width/2
    pi2=pi/2
    match char:
        case "a":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,0)
            ctx.line_to(0,0.5)
        case "b":
            ctx.arc(0.5,0.5,0.5-adjustment,3*pi2,pi2)
            ctx.move_to(0-line_width/2,0.5)
            ctx.line_to(1,0.5)
        case "c":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,3*pi2)
        case "d":
            ctx.arc(0.5,0.5,0.5-adjustment,3*pi2,pi2)
            ctx.line_to(0.5,0)
        case "e":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,3*pi2)
            ctx.move_to(0,0.5)
            ctx.line_to(1+line_width/2,0.5)
        case "f":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,3*pi2)
            ctx.move_to(0,0.5)
            ctx.line_to(1+line_width/2,0.5)
        case "g":
            ctx.arc(0.5,0.5,0.5-adjustment,0,3*pi2)
            ctx.move_to(0.5,0.5)
            ctx.line_to(1,0.5)
        case "h":
            ctx.arc(0.5,0.5,0.5-adjustment,3/4*pi,5/4*pi)
            ctx.stroke()
            ctx.arc(0.5,0.5,0.5-adjustment,7/4*pi,1/4*pi)
            ctx.move_to(0,0.5)
            ctx.line_to(1,0.5)
        case "i":
            ctx.arc(0.5,0.5,0.5-adjustment,1/4*pi,3/4*pi)
            ctx.stroke()
            ctx.arc(0.5,0.5,0.5-adjustment,5/4*pi,7/4*pi)
            ctx.move_to(0.5,0)
            ctx.line_to(0.5,1)
        case "j":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,pi)
            ctx.move_to(0.5,0-line_width/2)
            ctx.line_to(0.5,1)
        case "k":
            ctx.arc(0.5,0.5,0.5-adjustment,pi/4,7*pi/4)
            #ctx.move_to(0.5+cos(pi/4)/2,0.5-sin(pi/4)/2)
            ctx.move_to(1,0)
            ctx.line_to(0.5,0.5)
            ctx.line_to(1,1)
            #ctx.line_to(0.5+cos(pi/4)/2,0.5+sin(pi/4)/2)
        case "l":
            ctx.arc(0.5,0.5,0.5-adjustment,0,pi2)
            ctx.line_to(0.5,0-line_width/2)
        case "m":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,0)
            ctx.move_to(0.5,0)
            ctx.line_to(0.5,0.5)
        case "n":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,0)
        case "ñ":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,0)
            ctx.move_to(0.5-cos(pi/6)/2,0.25)
            ctx.line_to(0.5+cos(pi/6)/2,0.25)
        case "o":
            ctx.arc(0.5,0.5,0.5-adjustment,0,tau)
        case "p":
            ctx.arc(0.5,0.5,0.5-adjustment,0,tau)
            ctx.move_to(0.5,0)
            ctx.line_to(0,1)
        case "q":
            ctx.arc(0.5,0.5,0.5-adjustment,0,tau)
            ctx.move_to(0.5,0.5)
            ctx.line_to(1,1)
        case "r":
            ctx.arc(0.5,0.5,0.5-adjustment,0,tau)
            ctx.move_to(0,0.5)
            ctx.line_to(1,1)
        case "s":
            ctx.arc(0.5,0.5,0.5-adjustment,0,pi2)
            ctx.stroke()
            ctx.arc(0.5,0.5,0.5-adjustment,pi,3*pi2)
            ctx.stroke()
            ctx.move_to(0,0.5)
            ctx.line_to(1,0.5)
        case "t":
            ctx.arc(0.5,0.5,0.5-adjustment,pi,0)
            ctx.move_to(0.5,0)
            ctx.line_to(0.5,1+line_width/2)
        case "u":
            ctx.arc(0.5,0.5,0.5-adjustment,0,pi)
        case "v":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,pi)
            ctx.move_to(0.5,1)
            ctx.line_to(0.5,0.5)
            ctx.line_to(1+line_width/2,0.5)
        case "w":
            ctx.arc(0.5,0.5,0.5-adjustment,0,pi)
            ctx.move_to(0.5,0-line_width/2)
            ctx.line_to(0.5,1)
        case "x":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,pi)
            ctx.move_to(0,1)
            ctx.line_to(1,0)
        case "y":
            ctx.arc(0.5,0.5,0.5-adjustment,-pi/4,5/4*pi)
            ctx.move_to(0,0)
            ctx.line_to(0.5,0.5)
            ctx.line_to(1,0)
        case "z":
            ctx.arc(0.5,0.5,0.5-adjustment,pi2,pi)
            ctx.line_to(1,0.5)
            ctx.stroke()
            ctx.arc(0.5,0.5,0.5-adjustment,3*pi2,0)
        case " ":
            pass
        case default:
            pass
    ctx.stroke()
    if mode=="connected": #fix some borders of lines with circles
        match char:
            case "a":
                ctx.rectangle(0-line_width/2,0.5,line_width/2,line_width/2)
            case "d":
                ctx.rectangle(0.5-line_width/2,-line_width/2,line_width/2,line_width/2)
            case "f":
                ctx.rectangle(0-line_width/2,0.5,line_width/2,line_width/2)
            case "g":
                ctx.rectangle(1,0.5-line_width/2,line_width/2,line_width/2)
            case "j":
                ctx.rectangle(0.5,1,line_width/2,line_width/2)
            case "l":
                ctx.rectangle(0.5,1,line_width/2,line_width/2)
            case "s":
                ctx.rectangle(0-line_width/2,0.5,line_width/2,line_width/2)
                ctx.rectangle(1,0.5-line_width/2,line_width/2,line_width/2)
            case "v":
                ctx.rectangle(0.5,1,line_width/2,line_width/2)
            case "z":
                ctx.rectangle(1,0.5,line_width/2,line_width/2)
        ctx.fill()
        
def draw_text(text,file_format='png',file_name="output",line_width=0.1,rows=-1,cols=-1):
    if rows!=-1 and cols==-1: #rows given
        cols=ceil(len(text)/rows)
    elif rows==-1 and cols!=-1: #cols given
        rows=ceil(len(text)/cols)
    elif rows==-1 and cols==-1:
        cols=ceil(sqrt(len(text)))
        rows=ceil(len(text)/cols)
    else:
        assert len(text)<rows*cols

    print(text)
    print(cols, rows)
    # Set up the image surface (width, height)
    cell_width, cell_height = 128, 128
    width=cell_width*cols
    height=cell_height*rows

    if file_format == 'svg':
        # SVG surface for SVG output
        surface = cairo.SVGSurface(file_name+".svg", width, height)
    else:
        # PNG surface for PNG output (default)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    
    ctx = cairo.Context(surface)
    
    ctx.set_source_rgb(1, 1, 1)  # RGB for white
    ctx.rectangle(0, 0, width, height)  # Full canvas
    ctx.fill()
    
    ctx.set_line_width(line_width)
    ctx.scale(cell_width,cell_height)
    
    ctx.set_source_rgb(0, 0, 0)  # Set color for the circles (black)
    
    for idx,char in enumerate(text):
        row,col=divmod(idx,cols)
        ctx.save()
        ctx.translate(col,row)
        draw_char(char,ctx,line_width)
        ctx.restore()

    # Save the output based on the chosen file format
    if file_format == 'svg':
        print(f"SVG saved as '{file_name}.svg'")
    else:
        surface.write_to_png(file_name+".png")
        print(f"PNG saved as '{file_name}.png'")

def draw_connected_text(rows,cols,file_format='png',line_width=0.1):
    with open("connections.txt", "r") as f:
        lines=[line.rstrip() for line in f.readlines()[1:]]
    connections={line[0]:line[2:] for line in lines}
    r=[char for char in connections if connections[char][0]!="0"]
    d=[char for char in connections if connections[char][1]!="0"]
    l=[char for char in connections if connections[char][2]!="0"]
    u=[char for char in connections if connections[char][3]!="0"]
    print(r)
    print(d)
    print(l)
    print(u)
    
    # TO DO
    # I do not see much point in finishing this, because symbols connect well by default
    ...
    
def draw_letters_individually(alphabet,line_width=0.1,file_format="svg"):
    for letter in alphabet:
        draw_text(letter, line_width=line_width, file_format=file_format,file_name="letter_"+letter)


# EXECUTE WITH "python3 CircularFont"

alphabet="abcdefghijklmnñopqrstuvwxyz"
draw_text("".join(random.choices(alphabet,k=400)), line_width=0.1, file_format='png',file_name="random") 
draw_text(alphabet, line_width=0.1, file_format='png',file_name="alphabet")
draw_text(alphabet, line_width=0.1, file_format='svg',file_name="alphabet")

# Uncomment the following line to get an image for each letter
#draw_letters_individually(alphabet)

# You found a playful comment that uses words! It is close enough to a wordplay :)