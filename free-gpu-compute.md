# 全球免费 GPU 算力资源调研 (2024-2025)

> 调研时间：2026年6月27日
> 范围：提供真正免费 GPU 算力的平台（含大幅赠金的云厂商免费层）

---

## 一、完全免费层（无需付费/信用卡）

### 1. Google Colab（免费版）
- **网址**: https://colab.research.google.com
- **免费GPU**: T4 (16GB VRAM) / 偶尔 P100 (16GB)
- **免费时长**: 无固定上限，单次会话最长 12 小时（断线需重连）；每日/每周有隐性配额限制，重度使用会被暂时限速
- **注册**: Google 账号
- **主要限制**: 不保证 GPU 可用性，高峰时段可能分配不到；不适合长时间训练；TPU v2-8 也免费但需排队
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 免费GPU首选，生态最成熟

### 2. Kaggle Notebooks
- **网址**: https://kaggle.com
- **免费GPU**: T4 (16GB VRAM)
- **免费时长**: 每周 30 小时 GPU（TPU v3-8 每周 20 小时）
- **注册**: Google 账号 / 邮箱
- **主要限制**: 每周重置；不能后台运行；需每 90 分钟交互一次
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 稳定可预测，适合学习和实验

### 3. Hugging Face Spaces
- **网址**: https://huggingface.co/spaces
- **免费GPU**: T4 (16GB VRAM) — 需申请（Spaces GPU 赞助计划）
- **免费时长**: 按需分配，休眠后唤醒
- **注册**: HF 账号 + 申请 GPU 赞助
- **主要限制**: GPU 需申请，审批排队；休眠后需重新唤醒；不适合持续训练
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 部署 Demo/应用最佳

### 4. Lightning AI Studio
- **网址**: https://lightning.ai
- **免费GPU**: T4 (16GB VRAM)
- **免费时长**: 每月一定免费时长（通常 20-50 小时）；新用户有额外 credits
- **注册**: 邮箱或 GitHub
- **主要限制**: 用完即止；不可累积
- **推荐度**: ⭐⭐⭐⭐ (4/5) — PyTorch Lightning 生态整合好

### 5. Google Colab Pro ($10/月)
- **网址**: https://colab.research.google.com/signup
- **免费/付费GPU**: A100 (40GB VRAM) 优先分配；T4 不限时长
- **额度**: 约 100 计算单元/月（约 50-100 小时 A100 或更多 T4）
- **注册**: Google 账号 + 信用卡（$10/月）
- **主要限制**: 月度订阅；用完需等下月重置
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 性价比极高，A100 40GB

### 6. Google Colab Pro+ ($50/月)
- **网址**: https://colab.research.google.com/signup
- **免费/付费GPU**: A100 (40GB) 优先 / 后台运行
- **额度**: 约 500 计算单元/月
- **主要限制**: 价格较高；后台运行最长 24 小时
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 重度用户适用

---

## 二、新用户赠金/免费额度（需信用卡）

### 7. Google Cloud Vertex AI
- **网址**: https://cloud.google.com/vertex-ai
- **免费额度**: 新用户 $300 赠金（90天有效）
- **可用GPU**: T4 / A100 / L4 / H100（按区域）
- **注册**: Google 账号 + 信用卡（不自动扣费）
- **主要限制**: 90天后余额清零；需手动控制用量避免超额
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — $300 赠金最慷慨

### 8. RunPod Community Cloud
- **网址**: https://runpod.io
- **免费额度**: 社区共享 GPU，新用户有免费 credits（约 $5-10）
- **可用GPU**: RTX 3090/4090/A4000/A5000/A6000（社区共享）
- **注册**: 邮箱 + 信用卡（社区免费层可不绑卡）
- **主要限制**: 社区 GPU 随时被抢占；稳定性一般
- **推荐度**: ⭐⭐⭐ (3/5) — 便宜但不可靠

### 9. Modal
- **网址**: https://modal.com
- **免费额度**: 新用户 $5/月免费 credits（持续 3 个月）；学生/开源贡献者可申请额外
- **可用GPU**: T4 / L4 / A100
- **注册**: GitHub 账号
- **主要限制**: 额度有限；用完即止
- **推荐度**: ⭐⭐⭐⭐ (4/5) — Serverless GPU 体验好

### 10. Lambda Cloud
- **网址**: https://lambdalabs.com/service/gpu-cloud
- **免费额度**: 新用户 $5-10 赠金（限时活动）
- **可用GPU**: RTX 4090 / A100 / A10
- **注册**: 邮箱 + 信用卡
- **主要限制**: 赠金活动不稳定；用完后按小时付费较贵
- **推荐度**: ⭐⭐⭐ (3/5)

### 11. Vast.ai
- **网址**: https://vast.ai
- **免费额度**: 新用户赠 $5-10 credits（限时活动）
- **可用GPU**: 各种（社区市场，RTX 3090 ~ H100）
- **注册**: 邮箱 + 信用卡
- **主要限制**: 二手/社区 GPU，可靠性参差；价格波动大
- **推荐度**: ⭐⭐⭐ (3/5)

---

## 三、开源/学术免费 GPU

### 12. TPU Research Cloud (Google)
- **网址**: https://sites.research.google/trc/
- **免费额度**: TPU v3-8 Pod（约 $5-10K 等值算力）
- **可用GPU**: TPU v3-8 (128GB HBM)
- **注册**: 学术机构申请（需提案）
- **主要限制**: 需学术背景；审批严格；仅 TPU 不支持 CUDA
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 学术用户专属

### 13. AWS Activate / AWS Educate
- **网址**: https://aws.amazon.com/activate
- **免费额度**: 新用户 $100-200 赠金（Activate 计划）；Educate $30-100
- **可用GPU**: T4 / A10G / A100（按区域）
- **注册**: 信用卡 + 验证
- **主要限制**: 赠金有效期 1 年；需控制用量
- **推荐度**: ⭐⭐⭐⭐ (4/5)

### 14. Azure for Students / Azure Free Account
- **网址**: https://azure.microsoft.com/free
- **免费额度**: 新用户 $200 赠金（30天）；学生免费 $100
- **可用GPU**: T4 / A10 / NC 系列
- **注册**: Microsoft 账号 + 信用卡（学生可免卡）
- **主要限制**: 30天后需付费；GPU 配额需申请
- **推荐度**: ⭐⭐⭐ (3/5)

---

## 四、其他值得关注的

### 15. Gradient by Paperspace (现 DigitalOcean)
- **网址**: https://www.digitalocean.com/products/paperspace
- **免费额度**: 新用户 $5-10 赠金
- **可用GPU**: P4000 / A100 / A5000
- **注册**: 邮箱 + 信用卡
- **推荐度**: ⭐⭐⭐ (3/5)

### 16. Noteable
- **网址**: https://noteable.io
- **免费额度**: 免费层含有限 GPU 时长
- **可用GPU**: T4
- **推荐度**: ⭐⭐⭐ (3/5)

### 17. Deepnote
- **网址**: https://deepnote.com
- **免费额度**: 免费层含有限 GPU
- **可用GPU**: T4（需申请）
- **推荐度**: ⭐⭐⭐ (3/5)

### 18. Saturn Cloud
- **网址**: https://saturncloud.io
- **免费额度**: 免费层含有限 CPU/GPU
- **推荐度**: ⭐⭐ (2/5)

---

## 五、综合对比表

| 平台 | 免费GPU | VRAM | 免费时长 | 需信用卡 | 推荐度 |
|------|---------|------|----------|:--------:|:------:|
| **Google Colab** | T4 / P100 | 16GB | 12h/会话，隐性日配额 | ❌ | ⭐⭐⭐⭐⭐ |
| **Kaggle** | T4 | 16GB | 30h/周 | ❌ | ⭐⭐⭐⭐⭐ |
| **HF Spaces** | T4 | 16GB | 按需（需申请） | ❌ | ⭐⭐⭐⭐ |
| **Lightning AI** | T4 | 16GB | 月 20-50h | ❌ | ⭐⭐⭐⭐ |
| **Colab Pro** | A100 | 40GB | ~50-100h/月 | ✅$10/月 | ⭐⭐⭐⭐⭐ |
| **GCP $300** | T4/A100/L4 | 16-80GB | $300/90天 | ✅ | ⭐⭐⭐⭐⭐ |
| **Modal** | T4/L4/A100 | 16-40GB | $5×3月 | ❌ | ⭐⭐⭐⭐ |
| **RunPod** | 3090~A6000 | 24-48GB | $5-10 credits | ❌ | ⭐⭐⭐ |
| **Vast.ai** | 各种 | 各种 | $5-10 credits | ✅ | ⭐⭐⭐ |
| **Lambda** | 4090/A100 | 24-40GB | $5-10 credits | ✅ | ⭐⭐⭐ |
| **AWS Activate** | T4/A10G | 16-24GB | $100-200/年 | ✅ | ⭐⭐⭐⭐ |
| **Azure Free** | T4/NC | 16GB | $200/30天 | ✅ | ⭐⭐⭐ |
| **TPU Research** | TPU v3-8 | 128GB HBM | 大量（学术） | ❌ | ⭐⭐⭐⭐ |

---

## 六、推荐策略

| 场景 | 最佳组合 |
|------|----------|
| **日常学习/实验** | Colab 免费版 + Kaggle（每周 30h T4） |
| **需要 A100 大显存** | Colab Pro ($10) 或 GCP $300 赠金 |
| **部署 Demo/应用** | HuggingFace Spaces（免费 T4） |
| **长期稳定使用** | GCP $300 + RunPod 社区 |
| **学术用户** | TPU Research Cloud + GCP 赠金 |
| **零预算最大化** | Colab + Kaggle + HF Spaces + Modal（$5×3） |
