from tasks.diagnostics.pretty.mlp import PrettyMLP

rrn_4_steps = "../0ac07d0/best"
rrn_1_step = "../b7e022e/best"
mlp = "../8a972eb/best"

m = PrettyMLP()
m.load(mlp)
m.test_batches()