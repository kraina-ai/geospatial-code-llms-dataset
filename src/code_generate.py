import json

import torch
import transformers
from models import MODELS
from test_cases import test_cases
from tqdm import tqdm
import ray
import datetime

from settings import RESULTS_DIR
from utils import sanitize_single
from pydantic import BaseModel

class RunConfig(BaseModel):
    # temperature: float
    # top_p: float
    max_tokens: int
    # n_samples: int
    do_sample: bool

CONFIGS = [
    # RunConfig(
    #     temperature=0.8,
    #     top_p=0.95,
    #     max_tokens=200,
    #     n_samples=5,
    #     do_sample=False,
    # ),
    RunConfig(
        # temperature=0.2,
        # top_p=0.95,
        max_tokens=200,
        # n_samples=1,
        do_sample=False,
    ),
]


quantization_config = transformers.BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
)


@ray.remote(num_gpus=0.25, max_calls=1)
def generate_code(prompts: list[str], model_name: str, generation_config: RunConfig) -> list[str]:
    if model_name == "meta-llama/Meta-Llama-3-8B":
        extra_params = {"padding_side": "left"}
    else:
        extra_params = {}

    tokenizer = transformers.AutoTokenizer.from_pretrained(
        model_name, token=True, **extra_params
    )
    model = transformers.AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=quantization_config,
        device_map="auto",
        token=True,
    )

    code_for_prompts = []

    for prompt in tqdm(prompts, desc="Samples"):
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        outputs = model.generate(
            **inputs,
            max_new_tokens=generation_config.max_tokens,
            do_sample=generation_config.do_sample,
            # top_p=generation_config.top_p,
            # temperature=generation_config.temperature,
            pad_token_id=tokenizer.pad_token_id,
        )
        code_for_prompts.append(tokenizer.decode(outputs[0].to("cpu"), skip_special_tokens=True))

    # (generate_code pid=16518) A decoder-only architecture is being used, but right-padding was detected! For correct generation results, please set `padding_side='left'` when initializing the tokenizer.

    return code_for_prompts


def main():
    prompts = [case["prompt"] for case in test_cases]

    save_dir = RESULTS_DIR / "run_all_v2"
    save_dir.mkdir(parents=True, exist_ok=True)


    for run_config in CONFIGS:
        stats = {}

        run_save_dir = save_dir
        run_save_dir.mkdir(parents=True, exist_ok=True)
        
        stats["start_time"] = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        with open(run_save_dir / "config.json", "w") as f:
            json.dump(run_config.model_dump(), f)

        for model in MODELS:
            model_save_dir = run_save_dir / f"{model.replace(r'/', r'_')}"
            model_save_dir.mkdir(parents=True, exist_ok=True)

            print(f"Using model: {model}")

            stats[model] = {}

            generated_code = ray.get(
                generate_code.remote(prompts, model, run_config)
            )

            for prompt_idx, code_for_prompt in enumerate(generated_code):
                stats[model][f"{test_cases[prompt_idx]['id']}_prompt"] = prompts[prompt_idx]
                stats[model][f"{test_cases[prompt_idx]['id']}_generated"] = code_for_prompt
                
                entrypoint = test_cases[prompt_idx]["entrypoint"]

                stats[model][f"{test_cases[prompt_idx]['id']}_sanitized"] = sanitize_single(code_for_prompt, entrypoint)

            with open(
                model_save_dir / "generated.json", "w"
            ) as f:
                json.dump(stats[model], f)

        stats["end_time"] = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        print(stats)

        with open(run_save_dir / "generated.json", "w") as f:
            json.dump(stats, f)


if __name__ == "__main__":
    main()
