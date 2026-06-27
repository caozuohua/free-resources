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
