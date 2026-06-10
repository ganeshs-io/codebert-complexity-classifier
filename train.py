import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from torch.optim import AdamW
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

MODEL_NAME = "microsoft/codebert-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

class CodeDataset(Dataset):
    def __init__(self, codes, labels):
        self.encodings = tokenizer(list(codes), padding=True, truncation=True,
                                   max_length=256, return_tensors="pt")
        self.labels = torch.tensor(list(labels), dtype=torch.long)
    def __len__(self): return len(self.labels)
    def __getitem__(self, idx):
        return {"input_ids": self.encodings["input_ids"][idx],
                "attention_mask": self.encodings["attention_mask"][idx],
                "labels": self.labels[idx]}

train_df, test_df = train_test_split(df, test_size=0.2, stratify=df["label"], random_state=42)
train_df, val_df  = train_test_split(train_df, test_size=0.1, stratify=train_df["label"], random_state=42)
print(f"Train: {len(train_df)} | Val: {len(val_df)} | Test: {len(test_df)}")

train_loader = DataLoader(CodeDataset(train_df["code"], train_df["label"]), batch_size=8, shuffle=True)
val_loader   = DataLoader(CodeDataset(val_df["code"],   val_df["label"]),   batch_size=8)
test_loader  = DataLoader(CodeDataset(test_df["code"],  test_df["label"]),  batch_size=8)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Device: {device}")

model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=6).to(device)
optimizer = AdamW(model.parameters(), lr=2e-5)

best_val_acc = 0
for epoch in range(15):
    model.train()
    total_loss = 0
    for batch in train_loader:
        optimizer.zero_grad()
        out = model(input_ids=batch["input_ids"].to(device),
                    attention_mask=batch["attention_mask"].to(device),
                    labels=batch["labels"].to(device))
        out.loss.backward()
        optimizer.step()
        total_loss += out.loss.item()

    model.eval()
    correct = total = 0
    with torch.no_grad():
        for batch in val_loader:
            out = model(input_ids=batch["input_ids"].to(device),
                        attention_mask=batch["attention_mask"].to(device))
            preds = out.logits.argmax(dim=1)
            correct += (preds == batch["labels"].to(device)).sum().item()
            total += batch["labels"].size(0)
    val_acc = correct / total
    print(f"Epoch {epoch+1:2d} | Loss: {total_loss/len(train_loader):.4f} | Val Acc: {val_acc:.4f}")
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        model.save_pretrained("best_model")
        tokenizer.save_pretrained("best_model")
        print(f"  ✅ Saved! Best Val Acc: {val_acc:.4f}")

print("\n=== Final Test Results ===")
model.eval()
all_preds, all_labels = [], []
with torch.no_grad():
    for batch in test_loader:
        out = model(input_ids=batch["input_ids"].to(device),
                    attention_mask=batch["attention_mask"].to(device))
        all_preds.extend(out.logits.argmax(dim=1).cpu().numpy())
        all_labels.extend(batch["labels"].numpy())

print(classification_report(all_labels, all_preds,
      target_names=["O(1)","O(log n)","O(n)","O(n log n)","O(n^2)","O(2^n)"]))
