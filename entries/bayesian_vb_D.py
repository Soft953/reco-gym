from recogym.agents import BayesianAgentVB, bayesian_poly_args
bayesian_poly_args['aa'] = 0.2
bayesian_poly_args['bb'] = 0.2
pytorch_banditnet_args['num_products'] = P

agent = build_agent_init('BayesianAgentVB', BayesianAgentVB, {**bayesian_poly_args})