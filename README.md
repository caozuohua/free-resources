# 🎁 全球免费资源聚合

> Free Resources — GPU 算力 · LLM API · VPS/云主机 · 开发工具 · 开源模型 一站式精选目录

[![GitHub Pages](https://img.shields.io/badge/deploy-Pages-2ea44f)](https://caozuohua.github.io/free-resources)
[![Check Status](https://img.shields.io/github/actions/workflow/status/caozuohua/free-resources/check-resources.yml?label=weekly%20check)](https://github.com/caozuohua/free-resources/actions/workflows/check-resources.yml)
[![Resources](https://img.shields.io/badge/resources-97-10b981)](data/resources.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

🌐 在线浏览：https://caozuohua.github.io/free-resources

## 概述

精心搜集整理的全球互联网免费资源目录，涵盖 GPU 算力、LLM API、VPS 云主机、开发者工具和开源本地模型五大类别。所有资源均标注**免费层级、使用限制、评分**，并通过自动化检测持续验证可用性。

### 数据规模

| 类别 | 资源数 |
|------|--------|
| GPU 算力 | Google Colab / Kaggle / Colab Pro 等 |
| LLM API | Gemini / Groq / Claude / OpenAI 等 |
| VPS/云主机 | Oracle / AWS / Azure / GCP 等 |
| 开发工具 | 持续更新中 |
| 开源本地模型 | Ollama / llama.cpp / LM Studio 等 |

总计 **97 条资源**（持续增长），每季度全面审查更新。

## 功能

- 🔍 **搜索** — 按名称、描述、标签即时检索
- 🏷️ **分类筛选** — GPU / LLM API / VPS / DevOps 快速切分
- 📊 **状态标识** — ✅ Active / ⚠️ Limited / ❌ Dead 一目了然
- ⭐ **评分体系** — 1–5 星综合评级，优先推荐高质量资源
- 📱 **响应式设计** — 桌面/移动端友好

## 项目结构

```
free-resources/
├── docs/
│   └── index.html              # 静态站点（暗色主题）
├── data/
│   ├── resources.yaml          # 资源数据（YAML 源）
│   ├── resources.json          # 资源数据（JSON 源）
│   ├── categories.yaml         # 分类定义
│   └── status.json             # 资源状态缓存
├── scripts/
│   ├── yaml_to_json.py         # YAML → JSON 转换
│   └── check_availability.py   # 资源可用性检测脚本
├── free-gpu-compute.md         # 调研文档：GPU 算力
├── free-vps-resources.md       # 调研文档：VPS 云主机
├── llm-api-free-tiers.md       # 调研文档：LLM API
├── local-llm-solutions.md      # 调研文档：本地模型
├── free-compute-and-llm-api-resources.md  # 综合调研
└── .github/workflows/
    └── check-resources.yml     # 每周一自动检查资源可用性
```

## 数据格式

```yaml
- id: "google-colab"
  name: "Google Colab"
  url: "https://colab.research.google.com"
  description: "免费 T4 GPU 笔记本环境，无需信用卡"
  free_tier: "T4 GPU (16GB VRAM), 12hr/session"
  limitations: "高峰期不保证 GPU，不适用于长时间训练"
  rating: 5
  tags: ["gpu", "notebook", "no-credit-card", "python"]
  status: "active"
```

## 本地运行

```bash
python3 -m http.server 8000
# 打开 http://localhost:8000/docs/
```

## 自动化

| 工作流 | 触发 | 说明 |
|--------|------|------|
| `check-resources.yml` | 每周一 UTC 00:00 | 自动检测所有资源可用性，更新 status.json |

## 贡献

欢迎补充或修正：

1. 在 `data/resources.yaml` 中添加新资源
2. 运行 `python3 scripts/check_availability.py` 验证可用性
3. 提交 PR

### 贡献指南

- 只收录**真正免费**的资源（有免费层即可，可含付费升级选项）
- 提供准确的使用限制和评价
- 优先选择无需信用卡或赠金丰厚的资源

## License

MIT
