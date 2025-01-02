"""
Inspect script that includes tasks for ALL of the datasets described in how_to_load_datasets.ipynb
and load_datasets.py. Each task loads the specified dataset (train/test), then constructs
a small, human-readable Inspect dataset from the test set and evaluates it via a
simple prompt → label approach, with provider-level caching turned on.

Now, each task includes optional arguments:
 - few_shot_count (int): If > 0, uses that many few-shot examples from training data.
 - use_chain_of_thought (bool): If True, inserts a meta-instruction requesting step-by-step reasoning.

Usage example:
   inspect eval inspect_all_datasets.py --task=kl_polynomial --model=openai/gpt-4 --cache-prompt=true
   inspect eval inspect_all_datasets.py --task=symmetric_group_char --model=anthropic/claude-2 --cache-prompt=true

   # To enable few-shot:
   --task=schubert --few_shot_count=3
   # To enable chain-of-thought:
   --task=schubert --use_chain_of_thought=true
   # Use both:
   --task=schubert --few_shot_count=3 --use_chain_of_thought=true

Adjust --n (and/or other parameters) to pick valid values for each dataset. For instance:
   --task=rsk --n=10
   --task=mheight --n=11
   --task=weaving --n=7
etc.

Refer to:
 - https://inspect.ai-safety-institute.org.uk/datasets.html
 - https://inspect.ai-safety-institute.org.uk/solvers.html
 - https://inspect.ai-safety-institute.org.uk/scorers.html
 - https://inspect.ai-safety-institute.org.uk/caching.html
"""

import numpy as np
import os
from random import sample

from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.solver import chain, prompt_template, generate, chain_of_thought
from inspect_ai.scorer import match

# Ensure load_datasets.py is in your PYTHONPATH or the same directory
from load_datasets import get_dataset

def build_inspect_dataset(X, y, max_samples=-1):
    """
    Converts arrays X (features) and y (labels) into an Inspect MemoryDataset.
    Each item becomes a Sample with 'input' and 'target'.

    max_samples limits how many samples to demonstrate.
    For more details, see:
      https://inspect.ai-safety-institute.org.uk/datasets.html
    """
    samples = []
    if max_samples == -1:
        max_samples = len(X)
    N = min(len(X), max_samples)
    for i in range(N):
        # Turn X[i] into a string
        xi_str = " ".join(map(str, X[i]))
        # Turn y[i] into a string
        yi_str = str(y[i])

        # Construct a prompt that requests only the label
        prompt_text = (
            "Here is an input sequence:\n"
            f"{xi_str}\n\n"
            "Which label best applies? (Please provide only the label with no extra text.)"
        )

        samples.append(
            Sample(
                input=prompt_text,
                target=yi_str
            )
        )
    return MemoryDataset(samples)


def build_solver_chain(
    few_shot_examples_str: str,
    use_chain_thought: bool
):
    """
    Helper function to build a solver chain with optional chain-of-thought.
    few_shot_examples_str is either "" (empty) or a few-shot prompt block.
    use_chain_thought indicates if chain_of_thought() should be inserted.
    """
    # If we have few-shot examples, incorporate them. If not, just use "{prompt}" directly.
    if few_shot_examples_str:
        prompt_str = (
            f"{few_shot_examples_str}\n"
            "Now for the next input, please provide your answer (no extra explanation):\n\n"
            "{prompt}"
        )
    else:
        # No few-shot examples
        prompt_str = "{prompt}"

    steps = [prompt_template(prompt_str)]
    if use_chain_thought:
        steps.append(chain_of_thought())

    steps.append(generate(config={"cache-prompt": True}))
    return chain(*steps)


def build_few_shot_examples_str(X_train, y_train, few_shot_count: int):
    """
    Build a few-shot examples string, or return an empty string if few_shot_count <= 0.
    """
    if few_shot_count <= 0:
        return ""
    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    return "\n".join(examples_str_list)


################################################################################
# 1) KL Polynomial
################################################################################
@task
def kl_polynomial(
    n: int = 8,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'kl_polynomial' dataset, with optional few-shot examples and/or chain-of-thought.

    Args:
      n (int): Dataset size parameter
      folder (str): Folder path
      few_shot_count (int): Number of few-shot training examples (0 = none).
      use_chain_of_thought (bool): Whether to add chain-of-thought meta-prompt.
      max_samples (int): # of samples from test set.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="kl_polynomial", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 2) Schubert
################################################################################
@task
def schubert(
    n: int = 3,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'schubert' dataset, with optional few-shot examples and/or chain-of-thought.

    Args:
      n (int): Typically 3, 4, 5, or 6
      folder (str): Folder path
      few_shot_count (int): # of few-shot examples. 0 = none.
      use_chain_of_thought (bool): If True, embed chain-of-thought prompt.
      max_samples (int): # of test samples to evaluate.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="schubert", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 3) RSK
################################################################################
@task
def rsk(
    n: int = 10,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'rsk' dataset, with optional few-shot examples and/or chain-of-thought.
    Valid n often in {8, 9, 10}.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="rsk", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 4) Lattice Path
################################################################################
@task
def lattice_path(
    n: int = 6,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'lattice_path' dataset, with optional few-shot and/or chain-of-thought.
    n often in {6, 7, 8}.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="lattice_path", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 5) mheight
################################################################################
@task
def mheight(
    n: int = 10,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'mheight' dataset, with optional few-shot and/or chain-of-thought.
    n often in {10, 11, 12}.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="mheight", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 6) Quiver
################################################################################
@task
def quiver(
    n: int = 4,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'quiver' dataset, with optional few-shot and/or chain-of-thought.
    n often in {4, 5, 6}.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="quiver", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 7) Symmetric Group Character
################################################################################
@task
def symmetric_group_char(
    n: int = 18,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'symmetric_group_char' dataset, with optional few-shot and/or chain-of-thought.
    n in {18, 20, 22} might be supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="symmetric_group_char", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# 8) Weaving
################################################################################
@task
def weaving(
    n: int = 6,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1
):
    """
    Evaluate 'weaving' dataset, with optional few-shot and/or chain-of-thought.
    n in {6, 7, 8} typically.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="weaving", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    solver_chain = build_solver_chain(few_shot_str, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# For usage, pick a TASK and model, e.g.:
#   inspect eval inspect_all_datasets.py --task=schubert --model=openai/gpt-4 --cache-prompt=true
#   inspect eval inspect_all_datasets.py --task=schubert --few_shot_count=3 --use_chain_of_thought=true
#
# Additional references:
#   https://inspect.ai-safety-institute.org.uk/solvers.html
#   https://inspect.ai-safety-institute.org.uk/scorers.html
################################################################################ 