from tqdm import tqdm
from transformers import (
    AutoModelForCausalLM,
    PreTrainedTokenizerFast,
    HfArgumentParser,
)

import torch
import statistics

from dataclasses import dataclass, field
from typing import Optional
from peft import PeftModel
from prompt import *


@dataclass
class ScriptArguments:
    model_path : Optional[str] = field(default=None, metadata={'help': 'Please write model name'})
    query : Optional[str] = field(default='./', metadata={'help': 'Please write your question'})

parser = HfArgumentParser(ScriptArguments)
args = parser.parse_args_into_dataclasses()[0]

PROMPT = eval_prompt()

def do_generate(model, tokenizer, prompt):
    tokens = tokenizer(prompt, return_tensors = 'pt')
    tokens = {key: tensor.to(model.device) for key, tensor in tokens.items()}
    with torch.no_grad():
        outputs = model.generate(**tokens, max_new_tokens=2048, pad_token_id = tokenizer.eos_token_id)
    decoded_output = tokenizer.decode(outputs[0][tokens['input_ids'].size(1):], skip_special_tokens=True)

    return decoded_output

if __name__ == '__main__':

    print('=====Loading SPEED-TE=====')

    tokenizer = PreTrainedTokenizerFast.from_pretrained(
        args.model_path,
        local_files_only=True,
        model_max_length = 2048,
        padding_side = 'right',
        use_fast = False,
        device_map = 'auto',
    )
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})

    model = AutoModelForCausalLM.from_pretrained(
        args.base_model_path,
        device_map='auto',
        torch_dtype=torch.float32,
    )
    model.resize_token_embeddings(len(tokenizer))
    model = PeftModel.from_pretrained(model=model, model_id = args.model_path)
    model.eval()

    print(f'Your query: \n{args.query}')

    prompt = PROMPT.format_map(args.query)
    result = do_generate(model, tokenizer, prompt)

    print('===========================')
    print(f'SPEED-TE Answer: \n{result}')