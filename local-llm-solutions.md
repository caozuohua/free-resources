# 开源本地大模型运行方案调研 (2024-2025)

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
