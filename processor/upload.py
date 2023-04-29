'''
Author: Macielyoung
Date: 2023-04-28 13:29:56
Description: 生成指令数据集
'''
import pandas as pd
from datasets import Dataset, DatasetDict
    

train_file = "../datasets/train_finance.csv"
eval_file = "../datasets/eval_finance.csv"

train_df = pd.read_csv(train_file)
train_df = train_df.fillna("")
eval_df = pd.read_csv(eval_file)
eval_df = eval_df.fillna("")


train_dataset = Dataset.from_pandas(train_df)
eval_dataset = Dataset.from_pandas(eval_df)

instruction_dataset = DatasetDict({'train': train_dataset, 'eval': eval_dataset})
instruction_dataset = instruction_dataset.remove_columns(['Unnamed: 0'])
# instruction_dataset = instruction_dataset.remove_columns(['Unnamed: 0', 'task', 'desc'])
# instruction_dataset = instruction_dataset.filter(lambda x: len(x['instruction']) + len(x['input']) + len(x['output']) <= 250)
print(instruction_dataset)

instruction_dataset.push_to_hub("Maciel/FinCUGE-Instruction")
print("upload successfully!")