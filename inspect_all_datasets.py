"""
Inspect script that includes tasks for ALL of the datasets described in how_to_load_datasets.ipynb
and load_datasets.py. Each task loads the specified dataset (train/test), then constructs
a small, human-readable Inspect dataset from the test set and evaluates it via a
simple prompt → label approach, with provider-level caching turned on.

Possible tasks in this file:
  1) kl_polynomial
  2) schubert
  3) rsk
  4) lattice_path
  5) mheight
  6) quiver
  7) symmetric_group_char
  8) weaving

Usage example:
   inspect eval inspect_all_datasets.py --task=kl_polynomial --model=openai/gpt-4 --cache-prompt=true
   inspect eval inspect_all_datasets.py --task=symmetric_group_char --model=anthropic/claude-2 --cache-prompt=true

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
from inspect_ai.solver import chain, prompt_template, generate
from inspect_ai.scorer import match

# Ensure load_datasets.py is in your PYTHONPATH or the same directory
from load_datasets import get_dataset

def build_inspect_dataset(X, y, max_samples=5):
    """
    Converts arrays X (features) and y (labels) into an Inspect MemoryDataset.
    Each item becomes a Sample with 'input' and 'target'.

    max_samples limits how many samples to demonstrate.
    For more details, see:
      https://inspect.ai-safety-institute.org.uk/datasets.html
    """
    samples = []
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

################################################################################
# 1) KL Polynomial (kl_polynomial data)
################################################################################
@task
def kl_polynomial(n: int = 8, folder: str = "./"):
    """
    Evaluate the 'kl_polynomial' dataset.
    Valid n might be {8, 9, 10}, depending on the contents of load_datasets.py.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="kl_polynomial", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    # IMPORTANT: Use "{prompt}" rather than "{input}", since
    # prompt_template() expects a placeholder named {prompt}.
    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),  # caching turned on
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 2) Schubert
################################################################################
@task
def schubert(n: int = 3, folder: str = "./"):
    """
    Evaluate the 'schubert' dataset.
    Valid n in {3, 4, 5, 6} is supported by load_datasets.py.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="schubert", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    solver_chain = chain(
        # NOTE: changed from "{input}" to "{prompt}"
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 3) RSK
################################################################################
@task
def rsk(n: int = 10, folder: str = "./"):
    """
    Evaluate the 'rsk' dataset.
    n in {8, 9, 10} is typically supported by load_datasets.py.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="rsk", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    solver_chain = chain(
        prompt_template("{prompt}"),  # changed from {input} to {prompt}
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 4) Lattice Path
################################################################################
@task
def lattice_path(n: int = 6, folder: str = "./"):
    """
    Evaluate the 'lattice_path' dataset.
    n in {6, 7, 8} might be supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="lattice_path", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 5) mheight
################################################################################
@task
def mheight(n: int = 10, folder: str = "./"):
    """
    Evaluate the 'mheight' dataset.
    n in {10, 11, 12} might be supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="mheight", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 6) Quiver
################################################################################
@task
def quiver(n: int = 4, folder: str = "./"):
    """
    Evaluate the 'quiver' dataset.
    n in {4, 5, 6} might be supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="quiver", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 7) Symmetric Group Character
################################################################################
@task
def symmetric_group_char(n: int = 18, folder: str = "./"):
    """
    Evaluate the 'symmetric_group_char' dataset.
    n in {18, 20, 22} might be supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="symmetric_group_char", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)
    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# 8) Weaving
################################################################################
@task
def weaving(n: int = 6, folder: str = "./"):
    """
    Evaluate the 'weaving' dataset.
    n in {6, 7, 8} is typically supported.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="weaving", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)
    solver_chain = chain(
        prompt_template("{prompt}"),
        generate(config={"cache-prompt": True}),
    )
    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# Few-Shot Versions of Existing Tasks
#
# Each few-shot version below (X_few_shot) parallels the main tasks
# (kl_polynomial, schubert, etc.), but includes in-context examples
# drawn from the *training* set before presenting the test input to the model.
# 
# Usage examples:
#   inspect eval inspect_all_datasets.py --task=kl_polynomial_few_shot --model=openai/gpt-4 --cache-prompt=true
#   inspect eval inspect_all_datasets.py --task=rsk_few_shot --model=anthropic/claude-2 --cache-prompt=true
#
# Adjust --n, few_shot_count, etc. as desired.
################################################################################

@task
def kl_polynomial_few_shot(n: int = 8, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'kl_polynomial' dataset with a few-shot approach.
    """
    # Load data
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="kl_polynomial", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    # Randomly pick a few examples from the training set
    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))

    # Build a string of examples using an "Input → Output" style
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    # Create solver chain that includes the few-shot examples
    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def schubert_few_shot(n: int = 3, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'schubert' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="schubert", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def rsk_few_shot(n: int = 10, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'rsk' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="rsk", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def lattice_path_few_shot(n: int = 6, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'lattice_path' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="lattice_path", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def mheight_few_shot(n: int = 10, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'mheight' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="mheight", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def quiver_few_shot(n: int = 4, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'quiver' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="quiver", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def symmetric_group_char_few_shot(n: int = 18, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'symmetric_group_char' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="symmetric_group_char", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def weaving_few_shot(n: int = 6, folder: str = "./", few_shot_count: int = 3):
    """
    Evaluate the 'weaving' dataset with a few-shot approach.
    """
    X_train, y_train, X_test, y_test, input_size, output_size, num_tokens = get_dataset(
        data="weaving", n=n, folder=folder
    )

    ds = build_inspect_dataset(X_test, y_test)

    selected_indices = sample(range(len(X_train)), min(few_shot_count, len(X_train)))
    examples_str_list = []
    for idx in selected_indices:
        inp_str = " ".join(str(val) for val in X_train[idx])
        out_str = str(y_train[idx])
        examples_str_list.append(f"Example:\nInput: {inp_str}\nOutput: {out_str}\n")
    examples_str = "\n".join(examples_str_list)

    solver_chain = chain(
        prompt_template(
            f"{examples_str}\n"
            "Now for the next input, provide only the correct output (no explanation):\n\n"
            "{prompt}"
        ),
        generate(config={"cache-prompt": True}),
    )

    return Task(dataset=ds, solver=solver_chain, scorer=match())

################################################################################
# For usage, pick a TASK and model, e.g.:
#   inspect eval inspect_all_datasets.py --task=schubert --model=openai/gpt-4 --cache-prompt=true
#
# Additional references:
#   https://inspect.ai-safety-institute.org.uk/solvers.html
#   https://inspect.ai-safety-institute.org.uk/scorers.html
################################################################################ 