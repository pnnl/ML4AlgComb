"""
Experiment runner for tasks defined in llm_evaluation.py.
"""

from inspect_ai import eval
from llm_evaluation import algcomb_classification, algcomb_program_synthesis
import os
from plot_per_dataset_n import parse_inspect_logs_from_dir


# Define your configuration values below:
dataset_n_values = {
    "schubert": [3, 4, 5],
    # "weaving": [6, 7],
}
few_shot_counts = (0, 10, 30, 50, 100)
models = ["openai/gpt-4o-mini", "openai/gpt-4o", "anthropic/claude-3-5-sonnet-latest", "openai/o1-mini"]
# solver = "algcomb_classification"
solver = "algcomb_program_synthesis"
use_chain_of_thought = [True, False]

tasks_to_eval = []

def was_evaluated(
    dataset: str,
    n_val: int,
    few_shot: int,
    model: str,
    chain_of_thought: bool,
    log_dir: str
) -> bool:
    """
    Returns True if logs in log_dir contain a record matching the given
    (dataset, n, few_shot, model, use_chain_of_thought).
    """
    if not os.path.isdir(log_dir):
        return False

    df = parse_inspect_logs_from_dir(log_dir)
    subset = df[
        (df["dataset"] == dataset)
        & (df["n"] == n_val)
        & (df["few_shot"] == few_shot)
        & (df["model"] == model)
        & (df["use_chain_of_thought"] == chain_of_thought)
    ]
    return not subset.empty

skip_if_existing = True 
log_dir_base = "schubert_logs_algcomb_program_synthesis/"

for dataset, n_list in dataset_n_values.items():
    for model in models:
        for n in n_list:
            for few_shot in few_shot_counts:
                for cot in use_chain_of_thought:
                    if skip_if_existing:
                        if was_evaluated(dataset, n, few_shot, model, cot, log_dir=f"{dataset}_logs_{solver}"):
                            print("Skipping this configuration.")
                            continue

                    if solver == "algcomb_classification":
                        t = algcomb_classification(
                            dataset=dataset,
                            n=n,
                            few_shot_count=few_shot,
                            include_dataset_info=True,
                            max_samples=200,
                            use_chain_of_thought=cot
                        )
                    elif solver == "algcomb_program_synthesis":
                        t = algcomb_program_synthesis(
                            dataset=dataset,
                            n=n,
                            few_shot_count=few_shot,
                            include_dataset_info=True,
                            use_chain_of_thought=cot,
                            epochs=100,
                            max_tokens=15000  # this need to be high for the o1 models because they use a lot of tokens for this task
                        )
                    else:
                        raise ValueError(f"Solver '{solver}' not recognized.")

                    tasks_to_eval.append(t)

        logs = eval(tasks_to_eval, model=model, log_dir=f"{dataset}_logs_{solver}", log_level="warning")

print("Evaluation complete. Logs returned:", logs)