"""
Inspect script that includes tasks for ALL of the datasets described in how_to_load_datasets.ipynb
and load_datasets.py. Each task loads the specified dataset (train/test), then constructs
a small, human-readable Inspect dataset from the test set and evaluates it via a
simple prompt → label approach, with provider-level caching turned on.

Now, each task includes optional arguments:
 - few_shot_count (int): If > 0, uses that many few-shot examples from training data.
 - use_chain_of_thought (bool): If True, inserts a meta-instruction requesting step-by-step reasoning.
 - max_samples (int): If > 0, uses that many samples from the test set. Otherwise, uses all of the test set.
 - include_dataset_info (bool): If True, includes dataset information in the prompt. This is very high-level (see load_datasets.py)

Usage example for in-context classification, using both few-shot and chain-of-thought:
   inspect eval llm_evaluation.py@algcomb_classification -T --dataset=weaving -T --n=6 -T --few_shot_count=25 -T --use_chain_of_thought=true --cache-prompt=true --model=openai/gpt-4 

Usage example for program synthesis, using both few-shot and chain-of-thought:
   inspect eval llm_evaluation.py@algcomb_program_synthesis -T --dataset=weaving -T --n=6 -T --model=anthropic/claude-2 --cache-prompt=true --few_shot_count=25 --use_chain_of_thought=true
"""


import json
import sys
sys.path.append('..')
from load_datasets import get_dataset

from inspect_ai.scorer import scorer
from random import sample

from inspect_ai import Epochs, Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.solver import TaskState, chain, prompt_template, generate, chain_of_thought, system_message
from inspect_ai.scorer import Score, Target, match, mean, stderr

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
        xi_str = " ".join(map(str, X[i]))
        yi_str = str(y[i])

        prompt_text = (
            "\n\nHere is an input sequence:\n"
            f"{xi_str}\n"
            "Which label best applies?"
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
    if few_shot_examples_str:
        prompt_str = (
            f"{few_shot_examples_str}\n"
        )
    else:
        # no few-shot examples
        prompt_str = ""

    steps = [prompt_template(prompt_str)]
    if use_chain_thought:
        steps.append(chain_of_thought())
    else:
        prompt_str = "{prompt} Do not provide any additional reasoning or explanation. Just provide your answer at the end on its own line in the form 'ANSWER: $ANSWER' (without quotes) where $ANSWER is the answer to the question."
        steps.append(prompt_template(prompt_str))

    steps.append(generate(config={"cache-prompt": True}))
    return chain(*steps)


def build_few_shot_examples_str(X_train, y_train, few_shot_count: int):
    """
    Builds a few-shot examples string from the train set.
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


@task
def algcomb_classification(
    dataset: str = "schubert",
    n: int = 6,
    folder: str = "../",
    few_shot_count: int = 0,
    max_samples: int = -1,
    use_chain_of_thought: bool = False,
    include_dataset_info: bool = True
):
    """
    A single task that evaluates a LM on one of the ML4AlgComb datasets.

    Args:
        dataset (str): Must be either "weaving", "rsk", "schubert", "quiver", "mheight", "symmetric_group_char", "grassmannian_cluster_algebras", "kl_polynomial", or "lattice_path"
        n (int): 
            - n = 6, 7, or 8 for "weaving"
            - n = 8, 9, or 10 for "rsk"
            - n = 3, 4, 5, or 6 for "schubert"
            - n = 10, 11, or 12 for "mheight"
            - n = 18, 20, 22 for "symmetric_group_char"
            - n = 8 or 9 for "kl_polynomial"
            - n = 10, 11, 12, or 13 for "lattice_path"
            - There are not multiple values of n for the "quiver" and "grassmannian_cluster_algebras" datasetes
        folder (str): path to the dataset files.
        few_shot_count (int): Number of few-shot training examples (0 = none).
        use_chain_of_thought (bool): Use chain-of-thought meta-prompt.
        max_samples (int): # of samples from test set.
        include_dataset_info (bool): Include dataset information in the prompt.
    """
    allowed_datasets = [
        "weaving",
        # "kl_polynomial",
        "schubert",
        "rsk",
        "lattice_path",
        "mheight",
        "quiver",
        "symmetric_group_char",
    ]
    if dataset not in allowed_datasets:
        raise ValueError(
            f"Invalid dataset: '{dataset}'. Must be one of: {', '.join(allowed_datasets)}"
        )

    result = get_dataset(data=dataset, n=n, folder=folder, info_str=include_dataset_info)
    if include_dataset_info:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens), dataset_info = result
    else:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens) = result
        dataset_info = ""

    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)

    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)
    prompt_with_info = (
        (f"You are tasked with solving a classification problem. Here is high-level information about the dataset:\n{dataset_info}\n\n" if dataset_info else "") +
        f"{few_shot_str}"
        "{prompt}"
    )
    solver_chain = build_solver_chain(prompt_with_info, use_chain_of_thought)

    return Task(dataset=ds, solver=solver_chain, scorer=match())


@task
def algcomb_program_synthesis(
    dataset: str = "schubert",
    n: int = 6,
    folder: str = "../",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = 1,
    max_test_samples: int = -1,
    epochs: int = 1,
    timeout: int = 30,
    max_tokens: int = 10000,
    include_dataset_info: bool = True,
):
    """
    Program synthesis solver that works for all ML4AlgComb datasets.
    In each epoch, the model attempts to generate a single Python function 
    that solves the classification problem. We then score the program by 
    running it within a sandboxed python() environment on the test samples.

    See the README for more details. Requires Docker and the Dockerfile in the same directory as this script.

    Args:
        dataset (str): Must be one of: "weaving", "rsk", "schubert", "quiver", 
                      "mheight", "symmetric_group_char", "grassmannian_cluster_algebras", 
                      "kl_polynomial", or "lattice_path"
        n (int): Dataset size parameter (varies per dataset).
        folder (str): Location of dataset files.
        few_shot_count (int): If >0, number of training examples to show inline.
        use_chain_of_thought (bool): Whether or not to request chain-of-thought.
        max_samples (int): -1 => no limit, else cap the test set size.
        epochs (int): Number of times to re-run the generation process.
        timeout (int): Timeout for the program call.
        include_dataset_info (bool): Whether to include dataset information in the prompt.
    """
    allowed_datasets = [
        "kl_polynomial",
        "schubert",
        "rsk",
        "lattice_path",
        "mheight",
        "quiver",
        "symmetric_group_char",
        "weaving"
    ]
    if dataset not in allowed_datasets:
        raise ValueError(
            f"Invalid dataset: '{dataset}'. Must be one of: {', '.join(allowed_datasets)}"
        )

    result = get_dataset(data=dataset, n=n, folder=folder, info_str=include_dataset_info)
    if include_dataset_info:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens), dataset_info = result
    else:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens) = result
        dataset_info = ""

    if max_test_samples > 0:
        X_test = X_test[:max_test_samples]
        y_test = y_test[:max_test_samples]

    training_examples = ""
    few_shot_indices = range(min(few_shot_count, len(X_train)))
    for i in few_shot_indices:
        training_examples += (
            f"\n# Input: {X_train[i]},  Expected Output: {y_train[i]}"
        )

    instructions = (
        "Before answering with your Python code, reason in a step-by-step manner as to get the right answer.\n\n"
        if use_chain_of_thought
        else ""
    )

    system_msg = f"""Your job is to write a Python function that solves the classification problem. 
You will be given some examples of a classification problem from the '{dataset}' dataset.
Write a function 'predict' that takes an input in a Python list and returns an integer  as the classification result.

Here is information about the dataset:
{dataset_info}

Avoid using machine learning or model calls; rather, embed the logic in Python code.
Rather than use shallow pattern matching or using simple patterns, try to analyze the underlying combinatorial logic of the examples. Note that the datagenerating process for this dataset is a combinatorial algorithm.
You may want to use numpy and sympy for math operations or sage for cominatorics, however this is optional. If you do use them, *make sure to import them within your function*.

Below are a few examples from the training set:
{training_examples}

{instructions}
Your final answer should be valid Python code enclosed in triple backticks. This program will be evaluated on the test set.
"""


    @scorer(metrics=[mean(), stderr()])
    def program_synthesis_scorer():
        async def score(state: TaskState, target: Target) -> Score:
            import re

            completion = state.output.completion or ""
            pattern = r"```(?:python)?\n(.*?)```"
            match = re.search(pattern, completion, re.DOTALL)
            function_body = match.group(1) if match else None

            if not function_body:
                # If we can't find code, mark as 0.0
                return Score(value=0.0, explanation="No code block found")

            # Insert a test harness that: 
            # 1) defines the predict(...) function from user code
            # 2) runs predict(...) on all X_test
            # 3) returns predictions as JSON (so we can parse them in python)
            python_test_code = f"""
import json

{function_body}

test_inputs = {X_test.tolist()}
preds = []
for x in test_inputs:
    preds.append(predict(x))

print(json.dumps(preds))
"""

            try:
                from inspect_ai.tool import ToolError
                from inspect_ai.tool import python as py_tool

                result = await py_tool(timeout=timeout)(code=python_test_code)
                try:
                    preds = json.loads(result)
                except json.JSONDecodeError:
                    return Score(value=0.0, explanation=f"Failed to parse JSON output: {result}")
                if len(preds) != len(y_test):
                    return Score(
                        value=0.0,
                        explanation="Returned predictions have wrong length",
                    )

                correct_count = sum(1 for p, gold in zip(preds, y_test) if p == gold)
                acc = correct_count / len(y_test)
                return Score(
                    value=acc,
                    answer=str(preds),
                    explanation=f"Ran program in sandbox. Acc={acc:.3f}, {correct_count} correct out of {len(y_test)}"
                )
            except ToolError as te:
                return Score(value=0.0, explanation=f"ToolError: {te}")
            except Exception as ex:
                return Score(value=0.0, explanation=f"Exception: {ex}")

        return score

    samples = []
    for x, y in zip(X_train[:max_samples], y_train[:max_samples]):
        samples.append(Sample(input="", target=str(y)))

    ds = MemoryDataset(samples)

    solver_chain = [
        system_message(system_msg),
        generate(
            max_tokens=max_tokens,
            stop=["```", "def predict", "# End of code"],
            config={"cache-prompt": True}
        ),
    ]

    return Task(
        dataset=ds,
        solver=solver_chain,
        scorer=program_synthesis_scorer(),
        sandbox="docker",
        epochs=Epochs(epochs=epochs, reducer="max")
    )
