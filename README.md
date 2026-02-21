## SPEED-TE (Toxicity Expert)
[Toxicity expert (TE)](https://arxiv.org/abs/2509.20097)  evaluates model-generated responses for harmful or offensive language and provides explicit justifications for its evaluations.
<br>
<br>

* Response Generation Phase: it actively guides the domain model to revise potentially harmful expressions.

* Evaluation Phase: it identifies toxic language within candidate responses.

<br>

## 🌈 Dataset Information

| Dataset | Train | Test |
| --- | --- | --- |
| [Latent Hatred](https://arxiv.org/abs/2109.05322)  | 23,281 | 2,587 |
| [ToxiGen](https://arxiv.org/abs/2203.09509) | 225,855 | 25,096 |
| [Hate Speech Offen.](https://aclanthology.org/S19-2007/) | 30,762 | 3,419 |
| [Wiki Toxic](https://kaggle.com/competitions/jigsaw-toxic-comment-classification-challenge) | 22,304 | 2,479 |

<br>



## 🏗️ Model Architecture
TE is built upon the Llama 3.1 8B framework and fine-tuned using Parameter-Efficient Fine-Tuning (PEFT) techniques.
<br>
<br>

**Training Methodology**<br>

The model was trained using Low-Rank Adaptation (LoRA) on tasks divided into toxicity detection and explanation generation.


**Inference Pipeline**<br>

1. Persona-Based Guidance: Employs a "Language Guardian" persona to ensure consistent and deep analysis of generated text.

2. Adaptive Task Stages: Dynamically adjusts its reasoning steps.

<br>

## 🔥 Performance of TE

#### Detection Accuracy on Test set (%)

| Dataset | Llama3-70B | TE-8B |
| --- | --- | --- |
| Latent Hatred | 72.28 | **82.58** |
| ToxiGen | 77.67 | **89.39** |
| Hate Speech Offen. | 91.26 | **94.79** |
| WikiToxic | 84.06 | **91.25** |

<Br>

#### Detection Accuracy on Zero-Shot dataset (%)

| Dataset | Llama3-70B | TE-8B |
| --- | --- | --- |
| HatEval | 44.60 | **53.86** |
| ParadeTox | 57.15 | **65.95** |
| MultiToxic | 84.85 | **91.22** |
| ToxicChat | 87.55 | **92.05** |

<br>

#### LLM judge scores for toxicity explanations on test set

* Latent Hatred

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | **2.673** | 2.567 |
| Clarity(3) | **2.869** | 2.829 |

* ToxiGen

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | 2.467 | **2.482** |
| Clarity(3) | **2.884** | 2.394 |

* Hate Speech Offen.

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | 2.827 | **2.878** |
| Clarity(3) | 2.951 | **2.961** |

* WikiToxic

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | **2.677** | 2.488 |
| Clarity(3) | **2.938** | 2.732 |

<br>

#### LLM judge scores for toxicity explanations on Zero-Shot dataset

* HatEval

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | **2.877** | 2.830 |
| Clarity(3) | **2.96** | 2.873 |

* ParadeTox

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | **2.497** | 2.219 |
| Clarity(3) | **2.912** | 2.620 |

* MultiToxic

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | 2.518 | **2.561** |
| Clarity(3) | **2.923** | 2.824 |

* ToxicChat

| | Llama3-70B | TE-8B |
| --- | --- | --- |
| Analysis(3) | **2.592** | 2.179 |
| Clarity(3) | **2.946** | 2.661 |

<br>

## 🚀 Getting Started

🎁 Our Model [TE](https://huggingface.co/SeoSaMo/SPEED-TE-8B)

```
in preparation ...
```


<br>

## 📜 Citation


```
@misc{lee2025integratedframeworkllmevaluation,
      title={Integrated Framework for LLM Evaluation with Answer Generation}, 
      author={Sujeong Lee and Hayoung Lee and Seongsoo Heo and Wonik Choi},
      year={2025},
      eprint={2509.20097},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.20097}, 
}
```

