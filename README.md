# quantization-lab

A small analysis toolkit for local-model quantization experiments.

The repository keeps runtime measurements and task scores in the same record so 4-bit, 6-bit, 8-bit and higher-precision variants can be compared as a trade-off rather than by speed alone.

## Compare

- model file size
- peak memory observation
- model load latency
- prompt evaluation latency
- decode tokens/second
- task score
- context length
- quantization label

The analysis code can build a Pareto frontier: variants that are not simultaneously worse in memory, latency and quality.

```bash
python -m quantization_lab frontier runs.jsonl
```

No model weights or claimed universal rankings are stored here. Results only mean something together with the model family, runtime, hardware and task set that produced them.

Maintained by **Aarnav Saboo**.
