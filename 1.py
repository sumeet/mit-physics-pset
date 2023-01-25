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


from sympy import Symbol, init_printing, pprint, Piecewise, symbols, sympify, solve


def p(*args):
    for arg in args:
        pprint(arg, use_unicode=True)

init_printing()

t, t1, c, v0 = symbols('t t1 c, v0')

ac = v0 - c * (t - t1)
p(ac)

vc = ac.integrate(t)
xc = vc.integrate(t)

print('problem 1 (a)')
p(sympify('v_c(t)'))
p(vc)
p(sympify('x_c(t)'))
p(xc)

print('problem 1 (b)')
p(solve(vc.subs(v0, 12).subs(t1, 1).subs(c, 6), t))