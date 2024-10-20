from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):

    def __init__(self, variables: list[cp_model.IntVar], integer_factor):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.integer_factor = integer_factor

    def on_solution_callback(self) -> None:
        self.__solution_count += 1
        for v in self.__variables:
            print(f"{v}={self.value(v)/self.integer_factor}", end=" ")
        print()

    @property
    def solution_count(self) -> int:
        return self.__solution_count