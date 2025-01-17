
The paper introduces **Transformer2**, a novel framework for self-adaptive large language models (LLMs). Transformer2 addresses the limitations of traditional fine-tuning methods by dynamically adapting model behavior during inference. Here's an overview:

#### Key Innovations:
1. **Singular Value Fine-tuning (SVF):**
   - A parameter-efficient fine-tuning (PEFT) technique.
   - Fine-tunes only the singular values in the model's weight matrices, making the process computationally efficient and less prone to overfitting.
   - SVF produces "expert vectors" that are task-specific and composable.

2. **Two-Pass Inference Mechanism:**
   - In the first pass, the model identifies task properties.
   - In the second pass, it applies task-specific expert vectors to adjust the base model weights dynamically.

3. **Adaptation Strategies:**
   - **Prompt-based Adaptation:** Uses prompts to categorize tasks and select appropriate expert vectors.
   - **Job Classifier-based Adaptation:** Employs a classification module to identify task types.
   - **Mixture-based Adaptation:** Combines multiple expert vectors for complex or multi-domain tasks.

4. **Reinforcement Learning (RL):**
   - The expert vectors are trained using RL to optimize task performance, with additional regularization to prevent overfitting.

#### Applications and Advantages:
- Adaptable across diverse tasks, including unseen ones, without extensive re-training.
- Efficient use of resources, requiring fewer parameters compared to methods like LoRA.
- Demonstrates strong performance on vision-language tasks and out-of-distribution applications.

#### Theoretical Foundations:
- The framework is inspired by neuroscience principles, where specific brain regions activate based on tasks.
- The SVF technique builds on Singular Value Decomposition (SVD), focusing on tuning significant components of the model weights while preserving overall model stability.

Paper : [TRANSFORMER2 SELF-ADAPTIVE LLMS 2501.06252v2.pdf](https://github.com/user-attachments/files/18454428/TRANSFORMER2.SELF-ADAPTIVE.LLMS.2501.06252v2.pdf)

notion link: https://uttam-patel.notion.site/Transformer2-17e07c3870758026ac02e3d41df28965?pvs=74 
