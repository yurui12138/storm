# IG-Finder 仓库清理计划

## 目标
保留 IG-Finder 相关内容，删除 STORM 和 Co-STORM 的原有代码和文档。

## 保留内容

### 核心代码
- ✅ `knowledge_storm/ig_finder/` - IG-Finder 核心实现
- ✅ `knowledge_storm/__init__.py` - 包初始化（需修改）
- ✅ `knowledge_storm/interface.py` - 基础接口（IG-Finder依赖）
- ✅ `knowledge_storm/dataclass.py` - 数据类（IG-Finder依赖）
- ✅ `knowledge_storm/lm.py` - 语言模型（IG-Finder依赖）
- ✅ `knowledge_storm/rm.py` - 检索模块（IG-Finder依赖）
- ✅ `knowledge_storm/encoder.py` - 编码器（IG-Finder依赖）
- ✅ `knowledge_storm/logging_wrapper.py` - 日志包装器（IG-Finder依赖）
- ✅ `knowledge_storm/utils.py` - 工具函数（IG-Finder依赖）

### 示例代码
- ✅ `examples/ig_finder_examples/` - IG-Finder 示例

### 文档
- ✅ `IG_FINDER_DESIGN.md` - 设计文档
- ✅ `IG_FINDER_IMPLEMENTATION_SUMMARY.md` - 实现总结
- ✅ `IG_FINDER_使用指南.md` - 使用指南
- ✅ `YUNWU_OPTIMIZATION_README.md` - 优化说明
- ✅ `PROJECT_DELIVERY.md` - 交付文档
- ✅ `README.md` - 主README（需重写）
- ✅ `LICENSE` - 许可证
- ✅ `requirements.txt` - 依赖（需精简）
- ✅ `setup.py` - 安装脚本（需修改）

### 配置文件
- ✅ `.gitignore` - Git忽略规则
- ✅ `MANIFEST.in` - 打包清单（需修改）

## 删除内容

### STORM相关代码
- ❌ `knowledge_storm/storm_wiki/` - STORM Wiki模块
- ❌ `knowledge_storm/collaborative_storm/` - Co-STORM模块

### STORM示例
- ❌ `examples/storm_examples/` - STORM示例
- ❌ `examples/costorm_examples/` - Co-STORM示例

### STORM文档和资源
- ❌ `assets/` - STORM相关资源文件
- ❌ `frontend/` - STORM前端

### STORM配置
- ❌ `.pre-commit-config.yaml` - Pre-commit配置
- ❌ `CONTRIBUTING.md` - 贡献指南（STORM项目的）

## 执行步骤

1. 删除不需要的目录
2. 删除不需要的文件
3. 更新 README.md
4. 更新 setup.py
5. 更新 requirements.txt
6. 更新 __init__.py
7. 提交更改
