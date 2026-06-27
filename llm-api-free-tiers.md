# 全球免费 LLM API 额度/层级综合调研 (2024-2025)

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
