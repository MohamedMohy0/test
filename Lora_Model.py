import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset
from peft import get_peft_model, LoraConfig, TaskType

import time
start_time = time.time()

# Load and preprocess data
def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return [{"text": f"Q: {item['question']} A: {item['answer']}"} for item in data]

# Load datasets
probability_data = load_json(r"D:\Gradution\Final project\preprocissing\train_data\probability.json")
geometry_data = load_json(r"D:\Gradution\Final project\preprocissing\train_data\geometry.json")
algebra_data = load_json(r"D:\Gradution\Final project\preprocissing\train_data\algebra.json")
number_theory_data=load_json(r"D:\Gradution\Final project\preprocissing\train_data\number_theory.json")
intermediate_algebra_data=load_json(r"D:\Gradution\Final project\preprocissing\train_data\intermediate_algebra.json")
prealgebra_data=load_json(r"D:\Gradution\Final project\preprocissing\train_data\prealgebra.json")
precalculas_data=load_json(r"D:\Gradution\Final project\preprocissing\train_data\precalculus.json")

# Combine datasets
full_data = probability_data + geometry_data + algebra_data+number_theory_data+intermediate_algebra_data+prealgebra_data+precalculas_data

# Convert to Hugging Face dataset format
dataset = Dataset.from_list(full_data)

# Load GPT-2 Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

# Tokenize dataset
def tokenize_function(example):
    return tokenizer(example["text"], padding="max_length", truncation=True, max_length=512)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Load GPT-2 Model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Apply LoRA (Low-Rank Adaptation)
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,  # Low-rank parameter
    lora_alpha=32,
    lora_dropout=0.05,
    target_modules=["c_attn", "c_proj"]  # Apply LoRA to attention layers
)
model = get_peft_model(model, lora_config)

# Training arguments with optimizations
training_args = TrainingArguments(
    output_dir="./math_model",
    eval_strategy="steps",
    save_steps=500,
    logging_steps=50,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    learning_rate=5e-5,
    warmup_steps=500,
    weight_decay=0.01,
    gradient_accumulation_steps=2,
    fp16=True,  # Enable mixed precision training
    save_total_limit=3,  # Keep only the latest 3 checkpoints
    logging_dir="./logs",
    report_to="none",  # Disable online logging services
)

# Data Collator
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Trainer Setup
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Train Model
trainer.train()

# Save Model
trainer.save_model("math_model")
tokenizer.save_pretrained("math_model")

end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")