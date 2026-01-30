# Qodo PR-Agent 竞品调研报告

## 一、产品概述

| 项目 | 信息 |
| --- | --- |
| 产品名称 | PR-Agent（原CodiumAI PR-Agent） |
| 官网 | https://www.qodo.ai |
| GitHub | https://github.com/qodo-ai/pr-agent |
| 公司背景 | Qodo（原CodiumAI）开源项目 |
| 定位 | 开源的AI驱动Pull Request分析工具 |
| 支持平台 | GitHub、GitLab、Bitbucket、Azure DevOps、Gitea |
| 开源协议 | AGPL-3.0 |
| 调研日期 | 2026-01-30 |

---

## 二、核心功能

### 2.1 核心工具命令

| 命令 | 功能 | 描述 |
| --- | --- | --- |
| `/describe` | 自动描述 | 自动生成PR摘要和概述 |
| `/review` | 代码审查 | 全面审查代码，识别潜在问题 |
| `/improve` | 代码改进 | 提供具体优化建议，可直接修改代码 |
| `/ask` | 智能问答 | 针对PR或特定代码行提问 |
| `/update_changelog` | 更新日志 | 根据代码变更自动更新CHANGELOG |
| `/help` | 帮助文档 | 提供相关文档辅助 |

### 2.2 核心能力

| 能力 | 描述 |
| --- | --- |
| PR压缩策略 | 智能处理大型PR，在有限上下文窗口内分析大量代码变更 |
| 动态上下文 | 根据需要获取相关代码库背景信息 |
| 工单上下文获取 | 关联并获取Jira/GitHub Issue等工单信息 |
| 代码建议交互 | 可针对AI建议进行进一步对话和修改 |
| RAG上下文增强 | 利用检索增强生成技术提升分析准确性 |
| 增量更新 | 只分析PR中最新变更，提高效率 |

### 2.3 多模型支持

| 模型 | 支持情况 |
| --- | --- |
| OpenAI GPT | ✓ |
| Anthropic Claude | ✓ |
| Deepseek | ✓ |
| 其他兼容API | ✓ |

---

## 三、GitHub集成方式

### 3.1 方式一：快速体验（无需设置）

在任何**公共**GitHub仓库的PR评论中：
```
@CodiumAI-Agent /review
@CodiumAI-Agent /improve
@CodiumAI-Agent /describe
```

**限制**：
- 仅支持公共仓库
- 无法修改仓库内容（如更新PR描述）
- 宣传性质机器人

### 3.2 方式二：GitHub Actions（推荐）

```yaml
# .github/workflows/pr-agent.yml
name: PR Agent
on:
  pull_request:
    types: [opened, synchronize]
jobs:
  pr_agent_job:
    runs-on: ubuntu-latest
    steps:
    - name: PR Agent action step
      uses: Codium-ai/pr-agent@main
      env:
        OPENAI_KEY: ${{ secrets.OPENAI_KEY }}
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 3.3 方式三：CLI本地运行

```bash
# 安装
pip install pr-agent

# 配置Key
export OPENAI_KEY=your_key_here

# 运行审查
pr-agent --pr_url <PR链接> review
```

### 3.4 方式四：Docker部署

支持容器化部署，方便在各种环境中隔离运行。

### 3.5 方式五：Webhook自托管

通过Webhook接收Git平台事件触发，实现完全自主控制。

---

## 四、技术架构

| 方面 | 说明 |
| --- | --- |
| 编程语言 | Python（99.9%） |
| 运行环境 | CLI / Docker / GitHub Actions / Webhook |
| AI交互模式 | 基于LLM的智能体模式 |
| 提示词控制 | JSON-based prompting，可深度定制 |
| 数据流向 | 自托管时数据直接在用户和LLM提供商之间传输 |

---

## 五、开源特性

### 5.1 许可证

- **AGPL-3.0 License**
- 如对软件修改并作为网络服务提供，需开源源代码

### 5.2 自托管优势

| 优势 | 说明 |
| --- | --- |
| 完全控制 | 可在自己基础设施上托管 |
| 数据安全 | 使用自托管OpenAI Key，数据不经第三方 |
| 无供应商锁定 | 可自由迁移和修改 |
| 深度定制 | 可定制提示词和配置文件 |

### 5.3 社区状态

| 指标 | 数据 |
| --- | --- |
| GitHub Stars | 10,000+ |
| GitHub Forks | 1,300+ |
| 维护状态 | 社区维护，计划捐赠给开源基金会 |

**注意**：该仓库是Qodo商业产品的遗留开源项目，与Qodo付费/免费服务不同。

---

## 六、定价方案

### 6.1 开源版（Self-hosted）

| 项目 | 说明 |
| --- | --- |
| 费用 | **免费** |
| LLM成本 | 需自行承担（OpenAI API等） |
| 功能 | 完整核心功能 |
| 支持 | 社区支持 |

### 6.2 Qodo商业版

Qodo提供基于PR-Agent的商业SaaS服务，具体定价需访问Qodo官网。

---

## 七、竞争优势分析

### 7.1 优势

| 优势 | 说明 |
| --- | --- |
| **完全开源** | AGPL-3.0许可，可自由使用和修改 |
| **自托管** | 完全控制数据，满足安全合规需求 |
| **多平台支持** | 支持GitHub/GitLab/Bitbucket/Azure DevOps/Gitea |
| **多模型支持** | 可切换使用不同LLM提供商 |
| **无使用限制** | 自托管无审查次数限制 |
| **高度可定制** | 可深度定制提示词和规则 |
| **部署灵活** | CLI/Docker/Actions/Webhook多种部署方式 |

### 7.2 劣势

| 劣势 | 说明 |
| --- | --- |
| **部署成本** | 需自行搭建和维护基础设施 |
| **技术门槛** | 需要一定技术能力进行配置 |
| **LLM成本** | 需自行承担API调用费用 |
| **官方支持有限** | 社区维护，商业支持需购买Qodo服务 |
| **AGPL限制** | 修改后提供服务需开源 |

---

## 八、差异化机会

针对我们的AICR产品，从PR-Agent的成功中可借鉴和差异化：

| 差异化方向 | 说明 |
| --- | --- |
| **更友好的许可证** | 考虑使用MIT/Apache等更宽松许可 |
| **托管SaaS服务** | 提供免运维的托管服务 |
| **更好的UI/UX** | 提供更美观的审查结果展示 |
| **中文优化** | 针对中文代码和注释的特殊优化 |
| **国产平台集成** | 支持Gitee、Coding等国产Git平台 |
| **企业级支持** | 提供专业的企业级技术支持 |
| **更简单的配置** | 降低配置和部署门槛 |

---

## 九、技术实现参考

PR-Agent的技术实现对我们有重要参考价值：

### 9.1 命令机制

```python
# 支持的命令格式
@BotName /command [options]

# 示例
@CodiumAI-Agent /review
@CodiumAI-Agent /improve --extended
@CodiumAI-Agent /ask "这段代码的作用是什么？"
```

### 9.2 配置文件结构

```yaml
# 配置示例
pr_agent:
  model: "gpt-4"
  auto_review: true
  review_categories:
    - bug
    - security
    - performance
    - style
```

---

## 十、信息来源

- GitHub仓库：https://github.com/qodo-ai/pr-agent
- Qodo官网：https://www.qodo.ai
- GitHub README文档
- CSDN技术文章
