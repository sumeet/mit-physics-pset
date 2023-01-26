# links:
# problem sets
# https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/96231b21bccffc0c17c7d98629a52eb2_MIT8_01F16_pset1_new.pdf

# answer keys:
# - https://github.com/goepigen/8.01SC-Classical-Mechanics/blob/main/8.01%20Problem%20Sets/Pset%201%20-%20Kinematics.pdf
# - https://renrenthehamster.files.wordpress.com/2017/08/pset1.pdf
# (from https://renrenthehamster.wordpress.com/science/)


#
# bike (17m behind car)  | t = 0
#                        |
#                        | car speed is constant at v[0]
#                        |
#                        | t = 1 car starts to decelerate
#                        |
#                        |
#                        |
# bike reaches car       | t = 2 car stops


from sympy import Symbol, init_printing, pprint, Piecewise, symbols, sympify, solve, simplify, factor


def p(*args):
    for arg in args:
        pprint(arg, use_unicode=True)

init_printing()

t, t1, c, v0 = symbols('t t1 c v0')

ac = -c * (t - t1)
p(sympify('a_c(t)'))
p(ac)

vc = v0 - ac.integrate(t)
xc = vc.integrate(t)

print('problem 1 (a)')
p(sympify('v_c(t)'))
p(vc)
p(sympify('x_c(t)'))
p(xc)

print('problem 1 (b)')
inner = vc.subs(v0, 12).subs(t1, 1).subs(c, 6)
print(solve(inner))
exit()
#t2 = solve(inner)
#print(t2)
#exit()
#print(sympify((t2)))
#print('t2', float(t2))

x_t2 = xc.subs(v0, 12).subs(t1, 1).subs(c, 6).subs(t, t2)
print('x_t2', float(x_t2))
print(float(17.0 + x_t2 / t2))
