# DebateCV
[![arXiv](https://img.shields.io/badge/arXiv-2508.06059-B31B1B.svg)](https://arxiv.org/abs/2507.19090)
[![GitHub](https://img.shields.io/badge/GitHub-Fact2Fiction-181717.svg)](https://github.com/TrustworthyComp/DebatingTruth)

This repository contains the implementation of the debate-driven claim verification framework presented in the WWW-2026 paper, "Debating Truth: Debate-driven Claim Verification with Multiple Large Language Model Agents." The framework features two Debaters (Affirmative and Negative) who argue opposing stances, while a Moderator synthesizes the debates into a final verdict.

## News 🔥
- 2026-01 🎉 – Accepted by Special Track on Web4Good of the ACM Web Conference 2026 (WWW-2026); see you in Dubai, UAE! 🇦🇪
- 2025-07 📄 – Preprint released on arXiv.

## Key Components

- `scripts/run_debate.py`: Main runner for orchestrating multi-round debates with configurable models and prompt templates.
- `config/default.json`: Default configuration for models, prompts, and API endpoints.
- `src/`: Core implementation (agents, debate logic, utilities, data models).

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Prepare the data:
   - **Claims data**: Download the AVeriTeC dataset from [Hugging Face](https://huggingface.co/chenxwh/AVeriTeC) and place the `train.json` and `dev.json` files in `./data/AVeriTeC/` (or set `DATA_BASE_DIR` environment variable to your data directory).
   - **Evidence data**: Download the HerO evidence files from the [HerO repository](https://github.com/ssu-humane/HerO/tree/main/data_store/baseline) and place them in `./data/HerO/data_store/baseline/`:
     - `dev_veracity_prediction_8b.json`
   
   The expected directory structure:
   ```
   ./data/
   ├── AVeriTeC/
   │   ├── train.json
   │   └── dev.json
   └── HerO/
       └── data_store/
           └── baseline/
               └── dev_veracity_prediction_8b.json
   ```

3. Provide API credentials:
   - Edit `config/default.json` with your OpenAI API key and base URL before running.

4. Run a debate:
   ```bash
   python scripts/run_debate.py \
     --config config/default.json \
     --dataset dev \
     --evidence hero \
     --workers 1
   ```

## Configuration

The `config/default.json` file controls:
- `models`: Debate and Moderator models plus generation settings.
- `api_settings`: API endpoints and sleep intervals.
- `prompts`: Prompt templates for each role.
- `debate_settings`: Debate length and verbosity.

## Outputs

`scripts/run_debate.py` writes debate results and metadata into `output/` (one JSON file per claim).



## Citation

If you find this work useful, please cite our paper:

```bibtex
@inproceedings{he2026debatecv,
  title={Debating Truth: Debate-driven Claim Verification with Multiple Large Language Model Agents},
  author={He, Haorui and Li, Yupeng and Wen, Dacheng and Chen, Yang and Cheng, Reynold and Chen, Donglong and Lau, Francis C. M.},
  booktitle={Proc.~of WWW, 2026},
  year={2026}
}
```

## Acknowledgments

- This project uses the [AVeriTeC](https://huggingface.co/chenxwh/AVeriTeC) dataset. We thank the creators for making it publicly accessible.
- The debate implementation refers to [MAD](https://github.com/Skytliang/Multi-Agents-Debate).
- Retrieved evidence using code from [HerO](https://github.com/ssu-humane/HerO) and [InFact](https://github.com/multimodal-ai-lab/DEFAME/tree/infact).
- For Debate-SFT post-training, we used [TRL](https://github.com/huggingface/trl) with LoRA.
- For evaluation metrics (Accuracy and AVeriTeC Score), please refer to the evaluation scripts in [HerO](https://github.com/ssu-humane/HerO).
