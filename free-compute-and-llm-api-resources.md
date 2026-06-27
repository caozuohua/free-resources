# 全球免费计算资源大搜罗

> 调研时间：2026年6月27日
> 范围：GPU 算力 + VPS/云主机 + LLM API 额度 + 开源本地模型

---

# 一、免费 GPU 算力

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
# 海外免费 VPS/云资源调研 (2024-2025)

> 调研时间：2026年6月27日
> 范围：真正永久免费或大幅赠金的云服务器/VPS 平台

---

## 一、永久免费（Always Free，无需信用卡）

### 1. Oracle Cloud Always Free
- **网址**: https://oracle.com/cloud/free
- **免费额度（ARM）**: 4 OCPU + 24GB RAM（可拆分为最多4台VM）
- **免费额度（x86）**: 2 台 AMD 1/8 OCPU + 1GB RAM 每台
- **额外**: 10TB 出站流量/月、10TB 对象存储、$300 赠金（30天，需信用卡）
- **注册**: 邮箱 + 信用卡（不自动扣费，仅验证身份）
- **主要限制**: ARM 实例需等区域有容量；信用卡验证但免费层不扣费；出站流量超 10TB 后计费
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 免费层最慷慨，4 OCPU ARM 可跑轻量服务

### 2. Google Cloud e2-micro Free Tier
- **网址**: https://cloud.google.com/free
- **免费额度**: 1 台 e2-micro (0.25 vCPU, 1GB RAM) — 美国区域永久免费
- **额外**: 30GB 标准磁盘、5GB 快照、1GB 出站流量/月（北美→中国不限）
- **注册**: Google 账号 + 信用卡（不自动扣费）
- **主要限制**: 仅 us-west1/us-central1/us-east1 区域；CPU 很弱仅 0.25 vCPU；出站流量限制严
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 永久免费，但配置太弱仅适合轻量代理/隧道

### 3. Azure B1s Free Tier
- **网址**: https://azure.microsoft.com/free
- **免费额度**: 1 台 B1s (1 vCPU, 1GB RAM) — 12 个月免费
- **额外**: 64GB x2 标准 SSD、15GB 出站流量/月
- **注册**: Microsoft 账号 + 信用卡
- **主要限制**: 12 个月后自动转为付费（需手动关闭）；需绑信用卡
- **推荐度**: ⭐⭐⭐ (3/5) — 非永久，12个月后需付费

### 4. AWS Free Tier (t2.micro)
- **网址**: https://aws.amazon.com/free
- **免费额度**: 1 台 t2.micro (1 vCPU, 1GB RAM) — 12 个月免费，750 小时/月
- **额外**: 30GB EBS 存储、100GB 出站流量
- **注册**: AWS 账号 + 信用卡 + 电话验证
- **主要限制**: 12 个月；超量易扣费（需设告警）；部分区域 t3.micro
- **推荐度**: ⭐⭐⭐ (3/5) — 同 Azure，非永久且有扣费风险

---

## 二、永久免费（无需信用卡）

### 5. Deno Deploy
- **网址**: https://deno.com/deploy
- **免费额度**: 每天 100,000 请求、100GB 带宽、全球 CDN
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 仅支持 Deno/TypeScript/JavaScript；非传统 VPS（Serverless）；冷启动延迟
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 适合部署 API/边缘函数

### 6. Vercel
- **网址**: https://vercel.com
- **免费额度**: 100GB 带宽/月、6000 分钟构建、Serverless 函数 100GB-hours
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 仅前端/Serverless；非持久化 VPS；超过限制需升级
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 前端部署首选

### 7. Render
- **网址**: https://render.com
- **免费额度**: 1 个 Web Service (512MB RAM, 0.1 CPU) — 15 分钟不活跃后休眠
- **额外**: 100GB 出站流量/月、PostgreSQL 90天免费
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 免费 Web Service 会休眠（15分钟无请求后冷启约30秒）；750 小时/月
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 适合轻量 API/Demo

### 8. Fly.io
- **网址**: https://fly.io
- **免费额度**: 3 个共享 CPU VM (256MB RAM 每个) + 3GB 持久化存储
- **注册**: 信用卡（不自动扣费）或 GitHub
- **主要限制**: 每个 VM 仅 256MB RAM；共享 CPU；需信用卡验证
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 多 VM 适合微服务

### 9. Railway
- **网址**: https://railway.app
- **免费额度**: $5 赠金/月（持续，非试用）、500 小时运行/月
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: $5/月用完需等下月；无永久免费存储（需持久化卷则付费）
- **推荐度**: ⭐⭐⭐⭐ (4/5) — 月 $5 赠金够轻量服务

### 10. Cyclic.sh
- **网址**: https://cyclic.sh
- **免费额度**: 1 个 Full Stack App（256MB RAM、1GB 存储、100GB 带宽/月）
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 免费层会休眠；不支持长时间运行的服务
- **推荐度**: ⭐⭐⭐ (3/5)

### 11. Glitch
- **网址**: https://glitch.com
- **免费额度**: 无限项目、128MB RAM、200MB 存储、4000 小时/月
- **注册**: 邮箱（无需信用卡）
- **主要限制**: 5 分钟不活跃后休眠；RAM 仅 128MB；不适合生产
- **推荐度**: ⭐⭐⭐ (3/5)

### 12. Replit
- **网址**: https://replit.com
- **免费额度**: 1 个 Always-On 需付费；免费层 500MB RAM、0.5 vCPU、1GB 存储
- **注册**: 邮箱（无需信用卡）
- **主要限制**: 免费层会休眠；Always-On 需付费 $7/月
- **推荐度**: ⭐⭐⭐ (3/5)

### 13. Koyeb
- **网址**: https://koyeb.com
- **免费额度**: 1 个 Nano 实例 (256MB RAM)、1GB 存储
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 单实例；冷启动延迟；欧洲/美国/新加坡三区域
- **推荐度**: ⭐⭐⭐ (3/5)

### 14. Northflank
- **网址**: https://northflank.com
- **免费额度**: 1 个服务 (0.5 vCPU, 512MB RAM) + 1 个数据库
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 免费层有限制；冷启动
- **推荐度**: ⭐⭐⭐ (3/5)

### 15. Zeabur
- **网址**: https://zeabur.com
- **免费额度**: 约 $5 赠金/月
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 赠金有限；非永久
- **推荐度**: ⭐⭐⭐ (3/5)

### 16. Alwaysdata
- **网址**: https://alwaysdata.com
- **免费额度**: 1 个免费 profile（100MB 存储、1 个数据库、1 个域名）
- **注册**: 邮箱（无需信用卡）
- **主要限制**: 存储极小 (100MB)；仅适合极轻量网站/API
- **推荐度**: ⭐⭐⭐ (3/5)

### 17. InfinityFree
- **网址**: https://infinityfree.com
- **免费额度**: 无限网站托管、无限磁盘、无限带宽、400+ MySQL 数据库
- **注册**: 邮箱（无需信用卡）
- **主要限制**: 仅 PHP/MySQL 传统托管；无 SSH；不支持 Node.js/Python 直接运行
- **推荐度**: ⭐⭐ (2/5) — 传统 PHP 托管，不适合现代应用

---

## 三、开发平台免费层（Serverless/边缘）

### 18. Cloudflare Workers
- **网址**: https://workers.cloudflare.com
- **免费额度**: 每天 100,000 请求、10GB 带宽、10GB KV 存储
- **注册**: 邮箱（无需信用卡）
- **主要限制**: 仅 JavaScript/TypeScript/WebAssembly；Worker 有 CPU 时间限制（10ms）
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 边缘计算首选

### 19. Supabase
- **网址**: https://supabase.com
- **免费额度**: 500MB 数据库、5GB 存储、2GB 带宽、50万 Auth 用户
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 数据库 500MB 用完需付费；休眠后冷启
- **推荐度**: ⭐⭐⭐⭐⭐ (5/5) — 开源 Firebase 替代

### 20. PlanetScale
- **网址**: https://planetscale.com
- **免费额度**: 5GB 存储、10亿 行/月读取、1000 万 行/月写入
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 无免费计算层（需配合 Serverless 平台）；已取消免费计划（2024年改为 $35/月起）
- **推荐度**: ⭐⭐ (2/5) — 已取消免费

### 21. TiDB Cloud (PingCAP)
- **网址**: https://pingcap.com/tidb-cloud
- **免费额度**: TiDB Serverless — 5GB 存储、50M Request Units/月
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 仅数据库层；Request Units 用完后限速
- **推荐度**: ⭐⭐⭐⭐ (4/5)

### 22. Neon (Serverless Postgres)
- **网址**: https://neon.tech
- **免费额度**: 512MB 存储、10GB 数据传输、按需伸缩（不活跃时缩到 0）
- **注册**: GitHub 账号（无需信用卡）
- **主要限制**: 仅数据库；缩到 0 后冷启延迟
- **推荐度**: ⭐⭐⭐⭐ (4/5)

---

## 四、综合对比表

| 平台 | CPU | RAM | 存储 | 流量 | 永久? | 需信用卡 | 推荐度 |
|------|-----|-----|------|------|:-----:|:--------:|:------:|
| **Oracle Cloud** | 4 OCPU ARM | 24GB | 100GB | 10TB/月 | ✅ | ✅(不扣) | ⭐⭐⭐⭐⭐ |
| **GCP e2-micro** | 0.25 vCPU | 1GB | 30GB | 1GB/月 | ✅ | ✅(不扣) | ⭐⭐⭐⭐ |
| **Azure B1s** | 1 vCPU | 1GB | 128GB | 15GB/月 | ❌12月 | ✅ | ⭐⭐⭐ |
| **AWS t2.micro** | 1 vCPU | 1GB | 30GB | 100GB/月 | ❌12月 | ✅ | ⭐⭐⭐ |
| **Render** | 0.1 CPU | 512MB | 1GB | 100GB/月 | ✅ | ❌ | ⭐⭐⭐⭐ |
| **Railway** | 共享 | 512MB | — | — | ✅$5/月 | ❌ | ⭐⭐⭐⭐ |
| **Fly.io** | 共享×3 | 256MB×3 | 3GB | — | ✅ | ✅ | ⭐⭐⭐⭐ |
| **Cloudflare Workers** | 共享 | 128MB | 10GB KV | 10GB/月 | ✅ | ❌ | ⭐⭐⭐⭐⭐ |
| **Supabase** | — | — | 500MB+5GB | 2GB/月 | ✅ | ❌ | ⭐⭐⭐⭐⭐ |
| **Neon** | — | — | 512MB | 10GB/月 | ✅ | ❌ | ⭐⭐⭐⭐ |
| **Deno Deploy** | 共享 | — | — | 100GB/月 | ✅ | ❌ | ⭐⭐⭐⭐ |
| **Vercel** | 共享 | — | — | 100GB/月 | ✅ | ❌ | ⭐⭐⭐⭐ |

---

## 五、推荐策略

| 场景 | 最佳选择 |
|------|----------|
| **跑代理/隧道（如 x-ui）** | Oracle Cloud ARM (4 OCPU/24GB) 或 GCP e2-micro |
| **部署 API 服务** | Render / Railway / Fly.io |
| **前端+Serverless** | Vercel + Cloudflare Workers |
| **数据库** | Supabase + Neon + PlanetScale |
| **开发环境/IDE** | Replit / Gitpod |
| **边缘计算** | Cloudflare Workers |
| **多服务微服务** | Fly.io (3 VM) 或 Oracle Cloud (4 VM) |
| **零信用卡全免费** | Render + Vercel + Supabase + Cloudflare Workers |

---

## 六、注意事项

1. **Oracle Cloud 最值** — 4 OCPU ARM + 24GB RAM 永久免费，跑 newapi/x-ui 绰绰有余
2. **信用卡风险** — AWS/Azure/GCP 免费层需绑卡，务必设预算告警
3. **冷启动问题** — Render/Railway/Glitch 免费层会休眠，不适合需要 24/7 在线的服务
4. **流量限制** — 大部分免费层出站流量有限（1-10TB/月），跑代理需注意
5. **组合使用** — 最佳实践是 Oracle Cloud 跑主服务 + Cloudflare Workers 做边缘 + Supabase 做数据库

---

*最后更新：2026-06-27*
# 二、免费 LLM API 额度

> 调研时间：2026年6月27日
> 范围：提供持续免费额度或大额赠金的 LLM API 提供商

---

## 一、国际提供商

### 1. OpenRouter
- **网址**: https://openrouter.ai
- **免费层级**: 聚合平台，标注"Free"的模型无请求费用（Llama 3.1 8B、Mistral 7B、Gemma 2 9B、Qwen 2 7B 等）
- **速率限制**: 免费模型约 20 RPM
- **注册**: 邮箱或 GitHub/Google OAuth
- **评级**: ⭐⭐⭐⭐ (4/5) — 模型选择多，免费额度丰富

### 2. DeepSeek
- **网址**: https://platform.deepseek.com
- **免费层级**: 注册送 500 万 tokens；DeepSeek-V3 定价极低（输入 ¥1/百万，输出 ¥2/百万）
- **包含模型**: DeepSeek-V3、DeepSeek-R1、DeepSeek-Chat
- **速率限制**: 免费约 1-5 RPM
- **注册**: 邮箱+手机号
- **评级**: ⭐⭐⭐⭐⭐ (5/5) — 顶级推理能力，价格极低

### 3. Google Gemini
- **网址**: https://ai.google.dev
- **免费层级**:
  - Gemini 2.0 Flash: 15 RPM, 100万 TPD, 1500 RPD
  - Gemini 2.0 Flash-Lite: 30 RPM, 100万 TPD, 1500 RPD
  - Gemini 1.5 Flash: 15 RPM, 100万 TPD, 1500 RPD
  - Gemini 1.5 Pro: 2 RPM, 50 RPD
- **注册**: Google 账号
- **评级**: ⭐⭐⭐⭐⭐ (5/5) — 免费额度极其慷慨

### 4. OpenAI
- **网址**: https://platform.openai.com
- **免费层级**: 已取消新用户免费额度（2024年4月起）；ChatGPT Free 可用 GPT-4o-mini
- **评级**: ⭐⭐ (2/5) — 无持续免费 API 额度

### 5. Cohere
- **网址**: https://cohere.com
- **免费层级**: Trial Key 每60秒 20 次调用/1000次/月；Command R/R+、Embed/Rerank
- **注册**: 邮箱
- **评级**: ⭐⭐⭐⭐ (4/5) — RAG 专用模型实用

### 6. Mistral AI
- **网址**: https://console.mistral.ai
- **免费层级**: 试用额度（约 €8 已结束）；当前免费层仅限 La Plateforme 试用
- **评级**: ⭐⭐⭐ (3/5) — 无持续月度免费

### 7. Together AI
- **网址**: https://together.ai
- **免费层级**: 新用户注册送 $5 额度；部分免费模型（Llama 3.1 8B Instruct Turbo）
- **速率限制**: 免费模型约 60 RPM；$5 约 500-1000万 tokens
- **注册**: 邮箱或 GitHub
- **评级**: ⭐⭐⭐⭐ (4/5)

### 8. Groq
- **网址**: https://console.groq.com
- **免费层级**: 开发者免费层，每月限额
- **包含模型**: Llama 3.1/3.2/3.3、Mixtral 8x7B、Gemma 2
- **速率限制**: 30 RPM, 14400 RPD, 约 6000 TPM
- **注册**: 邮箱或 GitHub/Google
- **评级**: ⭐⭐⭐⭐⭐ (5/5) — 速度极快，免费额度慷慨

### 9. Hugging Face Inference API
- **网址**: https://huggingface.co/docs/api-inference
- **免费层级**: 免费层有限调用；PRO $9/月更高配额
- **包含模型**: 20万+ 开源模型
- **速率限制**: 无 Token: 1-3 RPM；有 Token: 10-30 RPM
- **评级**: ⭐⭐⭐⭐ (4/5) — 模型最全

### 10. Fireworks AI
- **网址**: https://fireworks.ai
- **免费层级**: 免费开源模型端点（Llama 3.1 8B、Mixtral 等）
- **速率限制**: 约 30-60 RPM
- **注册**: 邮箱或 GitHub/Google
- **评级**: ⭐⭐⭐⭐ (4/5)

### 11. Perplexity
- **网址**: https://docs.perplexity.ai
- **免费层级**: API 新用户赠 $5 额度
- **评级**: ⭐⭐⭐ (3/5) — 专注搜索，赠金有限

### 12. AnyScale
- **网址**: https://anyscale.com
- **免费层级**: 已取消免费层
- **评级**: ⭐⭐ (2/5)

### 13. Replicate
- **网址**: https://replicate.com
- **免费层级**: 无持续免费额度，按秒计费
- **评级**: ⭐⭐ (2/5)

### 14. Deepinfra
- **网址**: https://deepinfra.com
- **免费层级**: 新用户赠 $1.8 额度；部分免费端点
- **包含模型**: Llama 3.1/3.2/3.3、Mixtral、Qwen 2.5、DeepSeek、FLUX
- **评级**: ⭐⭐⭐ (3/5)

### 15. Novita AI
- **网址**: https://novita.ai
- **免费层级**: 新用户赠 $0.5-1 额度
- **评级**: ⭐⭐⭐ (3/5)

### 16. Cerebras
- **网址**: https://cloud.cerebras.ai
- **免费层级**: 开发者免费层，极速推理
- **包含模型**: Llama 3.1 8B/70B、Llama 3.3 70B
- **速率限制**: 约 10-30 RPM，>1000 tok/s
- **评级**: ⭐⭐⭐⭐ (4/5)

### 17. SambaNova
- **网址**: https://sambanova.ai
- **免费层级**: 免费 API 层，极速推理
- **包含模型**: Llama 3.1/3.2/3.3
- **评级**: ⭐⭐⭐⭐ (4/5)

### 18. Silicon Flow (硅基流动)
- **网址**: https://siliconflow.cn
- **免费层级**: 多个开源模型永久免费（Qwen 2.5 7B、GLM-4 9B、SDXL 等）
- **速率限制**: 约 10-30 RPM
- **注册**: 邮箱或手机号
- **评级**: ⭐⭐⭐⭐⭐ (5/5) — 中文友好，免费模型丰富

### 19. Cloudflare Workers AI
- **网址**: https://ai.cloudflare.com
- **免费层级**: 每天 10,000 次神经元推理（Workers Free 层）
- **包含模型**: Llama 3.1/3.2、Mistral、Qwen、Gemma
- **评级**: ⭐⭐⭐⭐ (4/5)

---

## 二、中国提供商

### 20. 智谱 GLM (BigModel)
- **网址**: https://open.bigmodel.cn
- **免费层级**: 注册送 2500 万 tokens；GLM-4-Flash 永久免费
- **包含模型**: GLM-4-Flash（免费）、GLM-4-Plus、GLM-4V
- **注册**: 手机号实名认证
- **评级**: ⭐⭐⭐⭐⭐ (5/5)

### 21. 月之暗面 Moonshot (Kimi)
- **网址**: https://platform.moonshot.cn
- **免费层级**: 注册送 15 元人民币额度
- **包含模型**: Moonshot-v1-8K/32K/128K
- **评级**: ⭐⭐⭐⭐ (4/5)

### 22. 阿里巴巴 DashScope (通义千问)
- **网址**: https://dashscope.console.aliyun.com
- **免费层级**: 新用户送 100-800 万 tokens；阿里云新用户 3000 元代金券
- **包含模型**: Qwen-Max/Plus/Turbo/VL/Audio
- **注册**: 阿里云账号+实名认证
- **评级**: ⭐⭐⭐⭐⭐ (5/5)

### 23. 字节跳动火山引擎 (豆包)
- **网址**: https://www.volcengine.com/product/doubao
- **免费层级**: Doubao-lite 免费；新用户赠 50-500 万 tokens
- **评级**: ⭐⭐⭐⭐ (4/5)

### 24. 百度千帆 (文心一言)
- **网址**: https://qianfan.baidubce.com
- **免费层级**: 新用户赠 100-500 万 tokens；ERNIE-Lite 免费
- **评级**: ⭐⭐⭐⭐ (4/5)

### 25. 腾讯混元
- **网址**: https://cloud.tencent.com/product/hunyuan
- **免费层级**: 腾讯云新用户赠 100 万 tokens；Hunyuan-Lite 免费
- **评级**: ⭐⭐⭐⭐ (4/5)

### 26. 讯飞星火
- **网址**: https://xinghuo.xfyun.cn
- **免费层级**: 新用户赠 200-500 万 tokens；Spark-Lite 免费
- **评级**: ⭐⭐⭐ (3/5)

### 27. MiniMax
- **网址**: https://www.minimaxi.com
- **免费层级**: 新用户赠送额度
- **评级**: ⭐⭐⭐ (3/5)

### 28. 零一万物 Yi (01.AI)
- **网址**: https://platform.01.ai
- **免费层级**: Yi-Lightning 免费；注册赠 tokens
- **评级**: ⭐⭐⭐⭐ (4/5)

### 29. 百川智能
- **网址**: https://platform.baichuan-ai.com
- **免费层级**: 新用户赠送 tokens
- **评级**: ⭐⭐⭐ (3/5)

### 30. 阶跃星辰 StepFun
- **网址**: https://platform.stepfun.com
- **免费层级**: 新用户赠送额度；Step-1 部分免费
- **评级**: ⭐⭐⭐ (3/5)

---

## 三、云服务商免费层

### 31. Google Vertex AI
- **网址**: https://cloud.google.com/vertex-ai
- **免费层级**: 新用户 $300 赠金（90天）；需信用卡
- **评级**: ⭐⭐⭐ (3/5)

### 32. AWS Bedrock
- **网址**: https://aws.amazon.com/bedrock
- **免费层级**: 无持续免费 LLM 层
- **评级**: ⭐ (1/5)

### 33. Azure AI
- **网址**: https://azure.microsoft.com/products/ai-services
- **免费层级**: 新用户 $200 赠金（30天）；OpenAI Service 需单独申请
- **评级**: ⭐⭐ (2/5)

---

## 四、综合推荐排名

| 排名 | 提供商 | 免费价值 | 推荐理由 |
|------|--------|----------|----------|
| 1 | Google Gemini | ★★★★★ | 每日100万tokens免费，顶级模型 |
| 2 | Groq | ★★★★★ | 极速推理，持续免费 |
| 3 | Silicon Flow | ★★★★★ | 永久免费模型多，中文友好 |
| 4 | 智谱 GLM | ★★★★★ | 2500万tokens赠金+免费模型 |
| 5 | 阿里 DashScope | ★★★★★ | 赠金丰富，模型全面 |
| 6 | DeepSeek | ★★★★☆ | 极低价格等效免费 |
| 7 | OpenRouter | ★★★★☆ | 多免费模型可选 |
| 8 | Cerebras | ★★★★☆ | 极速推理免费 |
| 9 | Cloudflare Workers AI | ★★★★☆ | 每日1万次免费 |
| 10 | 字节豆包 | ★★★★☆ | Lite免费，价格极低 |

---

## 五、注意事项

1. **免费层级经常变动** — 各提供商随时调整
2. **中国平台需实名认证** — 必须绑定手机号
3. **云服务商需绑信用卡** — 可能产生意外费用
4. **免费层通常禁止商业使用** — Google Gemini 免费层明确限制
5. **速率限制是主要瓶颈** — 大规模应用需多家组合
# 三、开源本地模型方案

> 调研时间：2026年6月27日
> 范围：无需API调用、可本地运行大语言模型的开源解决方案

---

## 一、核心推理引擎

### 1. Ollama
- **网址**: https://ollama.com
- **GitHub**: https://github.com/ollama/ollama
- **支持模型**: Llama 3/3.1/3.2, Mistral/Mixtral, Gemma 2, Phi-3/3.5, Qwen2/2.5, DeepSeek-R1, CodeLlama, LLaVA, StarCoder2, Command R 等 100+ GGUF 模型
- **硬件要求**: 最低8GB RAM(7B)；16GB(13B)；32GB+(70B)；支持CPU/GPU(NVIDIA/AMD/Apple Silicon)
- **易用性**: ⭐⭐⭐⭐⭐ 极简安装，一行命令拉取运行
- **评级**: 5/5

### 2. llama.cpp
- **网址**: https://github.com/ggerganov/llama.cpp
- **支持模型**: 几乎所有GGUF模型（Llama, Mistral, Gemma, Phi, Qwen, DeepSeek, Yi, Command R 等）
- **硬件要求**: 纯CPU即可；支持AVX2/AVX-512/Metal/CUDA/ROCm/Vulkan；4GB RAM可跑量化7B
- **易用性**: ⭐⭐⭐ 需编译或下载预编译二进制，命令行操作
- **评级**: 5/5

### 3. vLLM
- **网址**: https://github.com/vllm-project/vllm
- **支持模型**: Llama, Mistral/Mixtral, Qwen, Gemma, Phi, DeepSeek, Yi, InternLM 等主流Transformer模型
- **硬件要求**: **必须GPU**；最低1×A100/4090(24GB VRAM)；生产级推荐多卡A100/H100
- **易用性**: ⭐⭐⭐⭐ pip安装，OpenAI兼容API服务
- **评级**: 5/5（生产级推理性能最优）

### 4. LocalAI
- **网址**: https://github.com/mudler/LocalAI
- **支持模型**: GGUF格式模型；Stable Diffusion/Whisper/Piper TTS；LLaVA 多模态
- **硬件要求**: CPU/GPU均可；8GB RAM起步；支持CUDA加速
- **易用性**: ⭐⭐⭐⭐ Docker一键部署，OpenAI API兼容
- **评级**: 4/5

---

## 二、桌面GUI应用

### 5. LM Studio
- **网址**: https://lmstudio.ai
- **支持模型**: 所有GGUF格式模型；内置模型搜索下载
- **硬件要求**: 8GB RAM最低；16GB推荐；支持NVIDIA GPU/Apple Silicon/Metal
- **易用性**: ⭐⭐⭐⭐⭐ 图形界面精美，内置模型搜索/下载/对话
- **评级**: 5/5（桌面应用体验最佳）

### 6. GPT4All
- **网址**: https://gpt4all.io
- **GitHub**: https://github.com/nomic-ai/gpt4all
- **支持模型**: Llama 3, Mistral, Phi-3, Qwen2, Orca, Hermes 等精选GGUF模型
- **硬件要求**: **主打CPU推理**；4GB RAM可运行小模型；8GB+推荐
- **易用性**: ⭐⭐⭐⭐⭐ 一键安装，内置模型下载
- **评级**: 3/5（模型选择有限，CPU性能一般）

### 7. Jan
- **网址**: https://jan.ai
- **GitHub**: https://github.com/janhq/jan
- **支持模型**: Llama 3/3.1, Mistral, Gemma, Qwen, DeepSeek, Phi 等；支持远程API连接
- **硬件要求**: CPU/GPU均支持；8GB RAM最低
- **易用性**: ⭐⭐⭐⭐⭐ 现代化UI，本地优先设计
- **评级**: 4/5

### 8. KoboldCPP
- **网址**: https://github.com/LostRuins/koboldcpp
- **支持模型**: 所有GGUF/GGML模型；偏向创意写作/角色扮演
- **硬件要求**: CPU推理为主；支持CUDA/Metal；4GB RAM可跑小模型
- **易用性**: ⭐⭐⭐⭐ 单文件下载运行，内置Web GUI
- **评级**: 4/5

---

## 三、Web界面 / 综合平台

### 9. text-generation-webui (Oobabooga)
- **网址**: https://github.com/oobabooga/text-generation-webui
- **支持模型**: 极广泛：GGUF, GPTQ, AWQ, EXL2, HF Transformers 等几乎所有格式
- **硬件要求**: CPU/GPU灵活；8GB RAM最低；GPU推理推荐8GB+ VRAM
- **易用性**: ⭐⭐⭐ 功能强大但界面复杂，参数众多
- **评级**: 4/5

### 10. Open WebUI (原Ollama Web UI)
- **网址**: https://github.com/open-webui/open-webui
- **支持模型**: 依赖Ollama后端 → 所有Ollama支持的模型；也可连接OpenAI兼容API
- **硬件要求**: 与Ollama相同；额外需2GB+ RAM运行Web服务
- **易用性**: ⭐⭐⭐⭐⭐ ChatGPT风格界面，RAG/文档上传/代码高亮/多模态
- **评级**: 5/5（Web UI体验最佳）

### 11. ComfyUI（LLM扩展）
- **网址**: https://github.com/comfyanonymous/ComfyUI
- **支持模型**: 主要为图像模型；通过自定义节点支持Ollama/llama.cpp/GPT4All后端
- **硬件要求**: 图像生成：8GB+ VRAM；LLM节点：依赖后端；总体16GB+ VRAM
- **易用性**: ⭐⭐ 节点式工作流，LLM支持需额外配置
- **评级**: 3/5（LLM支持为附加功能）

---

## 四、其他值得关注的方案

### 12. Llamafile
- **网址**: https://github.com/Mozilla-Ocho/llamafile
- **支持模型**: 将模型+llama.cpp打包为单一可执行文件
- **硬件要求**: 跨平台单文件运行；CPU/GPU均支持；8GB+ RAM
- **易用性**: ⭐⭐⭐⭐⭐ 下载一个文件直接运行
- **评级**: 4/5

### 13. TabbyML / Tabby
- **网址**: https://github.com/TabbyML/tabby
- **支持模型**: 代码补全专用：StarCoder, CodeLlama, DeepSeek-Coder, Qwen2.5-Coder
- **硬件要求**: 极低；2-4GB VRAM可运行1-3B编码模型
- **易用性**: ⭐⭐⭐⭐ Docker部署，IDE插件一键配对
- **评级**: 4/5

### 14. Aphrodite Engine
- **网址**: https://github.com/aphrodite-engine/aphrodite
- **支持模型**: 基于vLLM扩展，支持更多模型格式和RoPE缩放
- **硬件要求**: 与vLLM类似，必须GPU；24GB+ VRAM推荐
- **易用性**: ⭐⭐⭐ 面向高级用户
- **评级**: 3/5

### 15. ExLlamaV2
- **网址**: https://github.com/turboderp/exllamav2
- **支持模型**: EXL2格式量化模型（Llama/Mistral/Qwen等）
- **硬件要求**: 仅NVIDIA GPU；24GB VRAM推荐运行70B量化
- **易用性**: ⭐⭐ 命令行工具，需手动转换模型格式
- **评级**: 4/5（速度和质量在GPU推理中顶尖）

---

## 五、综合对比表

| 方案 | 类型 | CPU | GPU | 易用性 | 质量 | 最适合场景 |
|------|------|:---:|:---:|:------:|:----:|-----------|
| **Ollama** | CLI/服务 | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 5 | 快速上手、开发集成 |
| **llama.cpp** | CLI/库 | ✅ | ✅ | ⭐⭐⭐ | 5 | 嵌入式集成、极致兼容 |
| **vLLM** | 服务 | ❌ | ✅ | ⭐⭐⭐⭐ | 5 | 生产部署、高并发 |
| **LocalAI** | 服务 | ✅ | ✅ | ⭐⭐⭐⭐ | 4 | API兼容替换、Docker |
| **LM Studio** | 桌面应用 | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 5 | 个人使用、图形界面 |
| **GPT4All** | 桌面应用 | ✅ | 🔺 | ⭐⭐⭐⭐⭐ | 3 | 低配电脑、入门用户 |
| **Jan** | 桌面应用 | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 4 | 隐私优先、现代UI |
| **KoboldCPP** | CLI+Web | ✅ | ✅ | ⭐⭐⭐⭐ | 4 | 创意写作、角色扮演 |
| **text-generation-webui** | Web UI | ✅ | ✅ | ⭐⭐⭐ | 4 | 高级调参、模型对比 |
| **Open WebUI** | Web UI | 依赖Ollama | 依赖Ollama | ⭐⭐⭐⭐⭐ | 5 | ChatGPT替代、团队使用 |
| **ComfyUI** | 节点式UI | 🔺 | ✅ | ⭐⭐ | 3 | 图像+LLM工作流 |
| **Llamafile** | 单文件 | ✅ | ✅ | ⭐⭐⭐⭐⭐ | 4 | 模型分发、零安装 |
| **Tabby** | 服务 | ✅ | ✅ | ⭐⭐⭐⭐ | 4 | 代码补全、开发工具 |
| **ExLlamaV2** | CLI/库 | ❌ | ✅(NVIDIA) | ⭐⭐ | 4 | 极致GPU速度 |

> ✅ = 完整支持 | 🔺 = 有限支持 | ❌ = 不支持

---

## 六、推荐建议

1. **新手入门**: Ollama + Open WebUI（最佳组合体验）
2. **桌面用户**: LM Studio 或 Jan（图形界面最友好）
3. **低配电脑**: GPT4All 或 KoboldCPP（CPU优化最好）
4. **生产部署**: vLLM（吞吐量最优、OpenAI兼容）
5. **深度调参**: text-generation-webui（参数最全面）
6. **模型分发**: Llamafile（单文件零依赖）
7. **代码补全**: Tabby（专注编码场景）
8. **创意写作**: KoboldCPP（内置故事引擎）
9. **极致性能**: ExLlamaV2（GPU推理速度之王）

---

# 四、免费 VPS/云主机
---
