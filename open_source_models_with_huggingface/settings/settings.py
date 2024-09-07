import environ

env = environ.Env()
environ.Env.read_env()

HF_KEY = env("HF_KEY")