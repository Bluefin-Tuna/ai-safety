from datasets import load_dataset

load_hf_prompts = lambda : load_dataset("declare-lab/HarmfulQA", split="train")
load_constitution = lambda : open("constitution.txt").readlines()
