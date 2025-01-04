"""
Inspect script that includes tasks for ALL of the datasets described in how_to_load_datasets.ipynb
and load_datasets.py. Each task loads the specified dataset (train/test), then constructs
a small, human-readable Inspect dataset from the test set and evaluates it via a
simple prompt → label approach, with provider-level caching turned on.

Now, each task includes optional arguments:
 - few_shot_count (int): If > 0, uses that many few-shot examples from training data.
 - use_chain_of_thought (bool): If True, inserts a meta-instruction requesting step-by-step reasoning.

Usage example:
   inspect eval inspect_all_datasets.py@combinatorics_classification -T --dataset=weaving -T --n=6 --model=openai/gpt-4 --cache-prompt=true
   inspect eval inspect_all_datasets.py@weaving_program_synthesis -T --dataset=weaving -T --n=6 -T --model=anthropic/claude-2 --cache-prompt=true

   # To enable few-shot:
   inspect eval inspect_all_datasets.py@combinatorics_classification -T --few_shot_count=3
   # To enable chain-of-thought:
   inspect eval inspect_all_datasets.py@combinatorics_classification -T --use_chain_of_thought=true
   # Use both:
   inspect eval inspect_all_datasets.py@combinatorics_classification -T --few_shot_count=3 --use_chain_of_thought=true

Adjust --n (and/or other parameters) to pick valid values for each dataset. For instance:
   inspect eval inspect_all_datasets.py@combinatorics_classification --n=10
   inspect eval inspect_all_datasets.py@mheight --n=11
   inspect eval inspect_all_datasets.py@weaving --n=7
etc.

Refer to:
 - https://inspect.ai-safety-institute.org.uk/datasets.html
 - https://inspect.ai-safety-institute.org.uk/solvers.html
 - https://inspect.ai-safety-institute.org.uk/scorers.html
 - https://inspect.ai-safety-institute.org.uk/caching.html
"""

from inspect_ai.scorer import scorer
from random import sample

from inspect_ai import Epochs, Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.solver import TaskState, chain, prompt_template, generate, chain_of_thought, system_message
from inspect_ai.scorer import Score, Target, match, mean, stderr

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


@task
def combinatorics_classification(
    dataset: str = "kl_polynomial",
    n: int = 8,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1,
    include_dataset_info: bool = False
):
    """
    A single task entry point that evaluates one of several datasets
    (non-program-synthesis) by specifying which dataset to load via a string.

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
        n (int): Dataset size parameter (varies per dataset).
        folder (str): Folder path.
        few_shot_count (int): Number of few-shot training examples (0 = none).
        use_chain_of_thought (bool): Whether to add chain-of-thought meta-prompt.
        max_samples (int): # of samples from test set.
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

    # Obtain the dataset and optionally the info string
    result = get_dataset(data=dataset, n=n, folder=folder, info_str=include_dataset_info)
    if include_dataset_info:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens), dataset_info = result
    else:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens) = result
        dataset_info = ""

    # Build the Inspect dataset
    ds = build_inspect_dataset(X_test, y_test, max_samples=max_samples)

    # Build optional few-shot examples
    few_shot_str = build_few_shot_examples_str(X_train, y_train, few_shot_count)

    # Add dataset info to the prompt if requested
    prompt_with_info = (
        (f"Here is information about the dataset:\n{dataset_info}\n\n" if dataset_info else "") +
        f"{few_shot_str}"
        "Now for the next input, please provide your answer (no extra explanation):\n\n"
        "{prompt}"
    )

    # Build the solver with or without chain-of-thought
    solver_chain = build_solver_chain(prompt_with_info, use_chain_of_thought)

    # Return the Inspect Task
    return Task(dataset=ds, solver=solver_chain, scorer=match())


################################################################################
# Weaving Program Synthesis
################################################################################
@task
def weaving_program_synthesis(
    n: int = 6,
    folder: str = "./",
    few_shot_count: int = 0,
    use_chain_of_thought: bool = False,
    max_samples: int = -1,
    epochs: int = 1,
    timeout: int = 30,
    include_dataset_info: bool = False,
):
    """
    Demonstration of program-synthesis style solver for the 'weaving' dataset
    using the python() tool. In each epoch, the model attempts to generate a
    single Python function that solves the 'weaving' classification problem.
    We then score the program by actually running it within a sandboxed python()
    environment on the given test samples.

    Args:
        n (int): Parameter for the weaving dataset (e.g. 6).
        folder (str): Location of dataset files.
        few_shot_count (int): If >0, number of training examples to show inline.
        use_chain_of_thought (bool): Whether or not to request chain-of-thought.
        max_samples (int): -1 => no limit, else cap the test set size.
        epochs (int): Number of times to re-run the generation process
                      (each epoch tries a single new program).
        timeout (int): Timeout for the program call.
        include_dataset_info (bool): Whether to include dataset information in the prompt.
    """
    # 1) Obtain dataset and optionally the info string
    result = get_dataset(data="weaving", n=n, folder=folder, info_str=include_dataset_info)
    if include_dataset_info:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens), dataset_info = result
    else:
        (X_train, y_train, X_test, y_test, input_size, output_size, num_tokens) = result
        dataset_info = ""

    if max_samples > 0:
        X_test = X_test[:max_samples]
        y_test = y_test[:max_samples]

    # 2) Build a minimal prompt from few-shot examples
    #    We embed the training examples as commented code or docstring,
    #    ensuring the model sees a small "training set".
    training_examples = ""
    few_shot_indices = range(min(few_shot_count, len(X_train)))
    for i in few_shot_indices:
        training_examples += (
            f"\n# Input: {X_train[i]},  Expected Output: {y_train[i]}"
        )

    # You may optionally include instructions for chain-of-thought
    # if use_chain_of_thought is set. For brevity we omit more details here.
    instructions = (
        "Explain your reasoning step-by-step.\n\n"
        if use_chain_of_thought
        else ""
    )

    system_msg = f"""You are a Python code synthesizer. 
You will be given some examples of a classification problem from the 'weaving' dataset.
Write a function 'predict' that takes an input in a Python list (e.g. [3,1,2,2]) 
and returns an integer (0 or 1) as the classification result.

{f"Here is information about the dataset:\n{dataset_info}\n" if dataset_info else ""}
Avoid using machine learning or model calls; rather, embed the logic in Python code.
You may want to use numpy or sympy for math operations, however this is optional.

Below are a few examples from the training set:
{training_examples}

{instructions}
Your final answer should be valid Python code enclosed in triple backticks.
"""

    # 3) Define a custom scorer that:
    #    (a) Extracts function text from the model's generation
    #    (b) Runs the function on test set using the sandboxed python() tool
    #    (c) Compares predictions to the test labels y_test
    #    (d) Returns the accuracy across the test set as a float

    @scorer(metrics=[mean(), stderr()])
    def program_synthesis_scorer():
        # We can do string pattern search or other parse logic below
        # for the function. Then we run the code using the python() tool
        # on each sample. If the function is invalid, we gracefully handle it.
        # We'll measure accuracy, store it in Score.value.
        async def score(state: TaskState, target: Target) -> Score:
            import re

            completion = state.output.completion or ""
            # A simple extraction for code within triple backticks.
            # Real-world usage might use a more robust parse:
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

            # Next, run this code in the sandboxed python environment:
            try:
                from inspect_ai.tool import ToolError
                from inspect_ai.tool import python as py_tool

                # We'll call the python() tool with a dynamic param "code"
                # that is the test harness.
                # If success, parse JSON output. If error, handle gracefully.
                result = await py_tool(timeout=timeout)(code=python_test_code)
                # result is the stdout from the tool call
                import json
                try:
                    preds = json.loads(result)
                except json.JSONDecodeError:
                    return Score(value=0.0, explanation=f"Failed to parse JSON output: {result}")
                if len(preds) != len(y_test):
                    # Something went wrong or user code is incomplete
                    return Score(
                        value=0.0,
                        explanation="Returned predictions have wrong length",
                    )

                # Compute accuracy
                correct_count = sum(1 for p, gold in zip(preds, y_test) if p == gold)
                acc = correct_count / len(y_test)
                return Score(
                    value=acc,
                    answer=str(preds),
                    explanation=f"Ran program in sandbox. Acc={acc:.3f}"
                )
            except ToolError as te:
                return Score(value=0.0, explanation=f"ToolError: {te}")
            except Exception as ex:
                return Score(value=0.0, explanation=f"Exception: {ex}")

        return score

    # 4) Build the test set as an Inspect dataset
    samples = []
    for x, y in zip(X_test, y_test):
        samples.append(Sample(input="", target=str(y)))

    # Wrap the samples directly in a MemoryDataset (instead of build_inspect_dataset)
    ds = MemoryDataset(samples)

    # 5) Define the solver pipeline
    #    We'll do: system_msg(...) => generate(...) => (the code is safe in the model output)
    #    We do not use the python() tool here at generation-time,
    #    because we just want the model to produce code.
    #    The python() calls happen inside the custom scorer above.
    solver_chain = [
        system_message(system_msg),
        generate(
            max_tokens=1000,
            stop=["```", "def predict", "# End of code"],
        ),
    ]

    # 6) Return the Inspect Task
    #    We pass in our dataset, solver, and custom scorer that executes code on X_test.
    return Task(
        dataset=ds,
        solver=solver_chain,
        scorer=program_synthesis_scorer(),
        sandbox="docker",
        epochs=Epochs(epochs=epochs, reducer="max")
    )

################################################################################
# For usage, pick a TASK and model, e.g.:
#   inspect eval inspect_all_datasets.py --task=schubert --model=openai/gpt-4 --cache-prompt=true
#   inspect eval inspect_all_datasets.py --task=schubert --few_shot_count=3 --use_chain_of_thought=true
#
# Additional references:
#   https://inspect.ai-safety-institute.org.uk/solvers.html
#   https://inspect.ai-safety-institute.org.uk/scorers.html
################################################################################ 