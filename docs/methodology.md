# Methodology

Quantization comparisons are easiest to misread when several unrelated variables change together.

For useful within-family experiments:

1. keep the base model family constant;
2. keep the prompt and output budget constant;
3. use the same runtime build and command options;
4. separate model load from prompt evaluation and decode;
5. repeat each cell several times;
6. store task scores next to systems measurements;
7. keep raw observations rather than only averages.

A lower-bit variant can win on memory and still lose on task quality. A higher-bit variant can preserve quality but reduce the number of models that fit simultaneously in memory. The frontier helpers preserve these trade-offs rather than collapsing them into one arbitrary score.
