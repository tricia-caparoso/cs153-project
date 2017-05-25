from operator import xor
from operator import mod

def checkInput(a):
    for i in a:
        if not str(i).isdigit():
            print "Improper input. Must be an integer."
            exit()

ax = raw_input("Enter A(x): ")
ax = [a for a in ax.split(" ")]
checkInput(ax)
ax = map(int, ax)
bx = raw_input("Enter B(x): ")
bx = [b for b in bx.split(" ")]
checkInput(bx)
bx = map(int, bx)
px = raw_input("Enter P(x): ")
px = [p for p in px.split(" ")]
checkInput(px)
px = map(int, px)
op = raw_input("Enter operation [+,-,*,/]: ")

pip = ''.join(str(e) for e in px)
m = len(px)-1

def mulrep(num):
    if num >= (2**m):
        temp = pip+('0'*(len(bin(num).replace('0b',''))-len(pip)))
        num^=int(temp,2)
        return mulrep(num)
    else: return num

def mul(p, q):
    ret = []
    for k in range(len(p)+len(q)-1):
        cell = []
        for i in range(max([0,k-len(q)+1]), 1+min([k,len(p)-1])):
            su = p[i]*q[k-i]
            if su >= 2**m:
                su = mulrep(su)
            cell.append(su)
        old = 0
        for c in cell:
            old = old^c
        ret.append(old)
    return ret

def div(p, q):
    out = list(p)
    norm = q[0]
    for i in xrange(len(p)-(len(q)-1)):
        out[i] /= norm
        cf = out[i]
        if cf != 0:
            for j in xrange(1, len(q)):
                out[i + j] ^= q[j] * cf
                if q[j] * cf >= 2**m:
                    out[i+j] = mulrep(q[j] * cf)
    sep = -(len(q)-1)
    return out[:sep], out[sep:]

if (op == '+'):
    if len(ax) > len(bx):
        bx = bx[::-1]+[0]*(len(ax)-len(bx))
        bx = bx[::-1]
    c = map(xor, ax, bx)
    print ax
    print '+', bx
    print '-------'
    print c
elif (op == '-'):
    if len(ax) > len(bx):
        bx = bx[::-1]+[0]*(len(ax)-len(bx))
        bx = bx[::-1]
    c = map(xor, ax, bx)
    print ax
    print '+', bx
    print '-------'
    print c
elif (op == '*'):
    c = mul(ax, bx)
elif (op == '/'):
    c, cr = div(ax, bx)

print "\nA(x):", ax
print "B(x):", bx
if op == '/':
    print "A(x)", op, "B(x): (qou)" , c
    print "A(x)", op, "B(x): (rem)" , cr
else: print "A(x)", op, "B(x):", c
