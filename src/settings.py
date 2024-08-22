from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
RESULTS_DIR = ROOT_DIR / 'results'
MODEL_RESULTS_DIR = RESULTS_DIR / 'per_model'
INPUTS_DIR = ROOT_DIR / 'inputs'