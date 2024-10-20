from ortools.sat.python import cp_model
from solution_printer import VarArraySolutionPrinter

model = cp_model.CpModel()
integer_factor = 10
lower_bound = -10*integer_factor
upper_bound = 110*integer_factor

x = model.new_int_var(lower_bound, upper_bound, "x")
y = model.new_int_var(lower_bound, upper_bound, "y")
z = model.new_int_var(lower_bound, upper_bound, "z")

model.add(90*integer_factor <= x + y + z)
model.add(x + y + z < 100*integer_factor)
model.add(x < 0)
model.add(0 < y)
model.add(y < 1*integer_factor)
model.add(z > 0)

solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z], integer_factor)
solver.parameters.enumerate_all_solutions = True
status = solver.solve(model, solution_printer)

print(f"Status: {solver.status_name(status)}")
print(f"Number of solutions found: {solution_printer.solution_count}")
