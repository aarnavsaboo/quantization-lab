# Result record

Each JSONL row represents one measured run.

Important fields include the model family, exact variant, runtime, on-disk size, observed memory, model load time, prompt evaluation time, decode throughput and task score.

The task score is intentionally external to this package. It can come from exact match, retrieval metrics, a labelled classification set or another deterministic workload-specific measure. Keeping that choice outside the quantization code makes the systems comparison reusable.
