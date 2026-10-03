# quantization-lab

Experiment tooling for comparing local model quantization variants as multi-dimensional systems trade-offs.

A quantized model is not simply "smaller" or "faster." Different variants can move model load time, memory use, prompt-processing speed, generation throughput and task quality in different directions. This repository stores those dimensions together and provides utilities for building comparison tables and Pareto frontiers.

The intended workflow is local and repeatable: define a model family, register several local variants, run the same workload against each one, keep the raw measurements, then compare.

## Dimensions recorded

- model family and variant label
- quantization label
- on-disk size
- local runtime
- model load latency
- prompt-evaluation latency
- decode throughput
- total request latency
- process memory observations
- context size
- prompt/output token counts
- task score from a separate evaluation set

## Why a Pareto frontier?

A single weighted score makes hidden assumptions about what matters. The frontier instead keeps every configuration that is not strictly worse across all selected dimensions.

One deployment-shaped workload may prefer the lowest memory variant above a quality floor. Another may prefer the fastest decode rate. A batch workflow may care more about throughput than first-token latency.

## Workflow

```text
variants.json
     |
     v
experiment planner
     |
     +--> Q4 variant
     +--> Q5 variant
     +--> Q6 variant
     +--> Q8 variant
     |
     v
local runtime measurements
     |
     v
raw JSONL
     |
     +--> per-family tables
     +--> Pareto frontier
     +--> quality-floor filtering
     +--> normalized trade-off report
```

## CLI

```bash
python -m quantization_lab inspect models/
python -m quantization_lab frontier runs.jsonl
python -m quantization_lab table runs.jsonl --quality-floor 0.80
```

The repository does not ship model weights or a universal quantization ranking. Comparisons are meaningful only within a documented model family and workload.

Maintained by **Aarnav Saboo**.
