from recogym import build_agent_init
from recogym.agents import LogregPolyAgent, logreg_poly_args

agent = build_agent_init('likelihood', LogregPolyAgent, {**logreg_poly_args, })
