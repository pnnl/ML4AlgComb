# LLM Evaluations for Combinatorics Datasets

This directory contains evaluation scripts for testing language models on the algebraic combinatorics datasets using the inspect-ai framework. The evaluations consist of an in-context learning task and a program synthesis task.

## Overview

The evaluation suite provides two main tasks:

1. **In-Context Classification** (`algcomb_classification`):
   - Tests direct classification, ie simple prompt → label evaluation.
   - Optionally uses few-shot examples (pretty necessary to get good results) and chain-of-thought.

2. **Program Synthesis** (`algcomb_program_synthesis`):
   - The language model is given the task of generating a Python function to solve the classification task.
   - Evaluates generated code in a sandboxed Docker environment (gives the LM the option to use numpy, sympy, and sage-- see Dockerfile).
   - Optionally uses few-shot examples and chain-of-thought.

## Usage Examples

### In-Context Classification 
On the weaving patterns dataset, with chain-of-thought reasoning and 25 few-shot examples:
```
inspect eval llm_evaluation.py@algcomb_classification -T --dataset=weaving -T --n=6 -T --few_shot_count=25 -T --use_chain_of_thought=true --cache-prompt=true --model=openai/gpt-4
```

### Program Synthesis
On the weaving patterns dataset, with chain-of-thought reasoning and 25 few-shot examples:
```
inspect eval llm_evaluation.py@algcomb_program_synthesis -T --dataset=weaving -T --n=6 -T --model=anthropic/claude-2 --cache-prompt=true --few_shot_count=25 --use_chain_of_thought=true
```

#### Notes:
- You can control the number of programs generated in two ways: either by varying the number of epochs or by varying the number of test samples. Either way, the solver will evaluate the program on the entire test set (this is cheap because it is just a python program!). The difference is that varying the test samples will prompt the model with a different test sample for each program call. However, the scoring is a max over the epochs, so the scoring displayed when you run `inspect view --log-dir logs` in you command line will only be correct if you run with max_test_samples=1 (the default) and varying the number of epochs. You can recover the correct scoring when you run with different test samples by just examining the logs (either sorting by sample when running `inspect view` or by parsing the csv). Hopefully, this will be fixed in the future.
- For the o1-series of models, you will probably want to increase max_tokens.

## Task Options

- Few-shot learning support (configurable number of training examples)
- Chain-of-thought prompting
- Sample size for testing
- (Very high-level) dataset information included in the prompts
- Provider-level caching (very useful when using a large number of in-context examples).

## Requirements

- inspect-ai (https://inspect.ai-safety-institute.org.uk/)
- Docker (for program synthesis evaluation)
- Access keys for LLM providers (e.g., OpenAI, Anthropic)
- The downloaded datasets (see load_datasets.py and how_to_load_datasets.ipynb)