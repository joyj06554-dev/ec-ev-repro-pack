# GitHub + Zenodo 发布步骤

## 一、发布前只需补齐的账户/作者元数据

在公开发布前完成 `RELEASE_METADATA_REQUIRED.md` 中的项目：
1. 作者姓名及顺序；
2. ORCID（如有）；
3. GitHub 仓库地址；
4. 关联论文 DOI（如已有）；
5. 许可证选择；
6. Zenodo DOI（可在 Zenodo 草稿中预留后再回填）。

这些属于发布元数据，不影响 v1.0 数据与方法学内容本身。

## 二、GitHub

1. 新建公开仓库，建议名称：`ec-ev-repro-pack`。
2. 将本压缩包内 `ec-ev-repro-pack-v1.0/` 的**内部文件和文件夹**上传到仓库根目录。
3. 作者信息已补齐，仓库应包含正式 `CITATION.cff`。
4. 正式混合许可证文件已加入：`LICENSE`、`LICENSE-CODE`、`LICENSE-DATA-DOCS`。
5. 提交全部文件。
6. 创建标签 `v1.0`。
7. 以 `v1.0` 创建 GitHub Release。Release 标题可用：`EC-EV Reproducibility Package v1.0`。
8. Release 后不要静默替换核心文件；实质性修改应发布 v1.1/v2.0。

## 三、Zenodo：推荐使用 GitHub 集成

1. 登录 Zenodo 并连接 GitHub 账户。
2. 在 Zenodo 的 GitHub 页面执行同步。
3. 找到 `ec-ev-repro-pack` 仓库并启用。
4. GitHub 侧创建新 Release 后，Zenodo 会归档相应版本。
5. 核对 Zenodo 记录中的标题、Creators、Description、Version、Keywords、License 和关联论文信息。
6. 如果需要在正式文件中提前写入 DOI，可在 Zenodo 草稿中先预留 DOI，再回填到 README/Data Availability 后完成最终发布。

## 四、Zenodo：手工上传备选方案

如果不使用 GitHub 自动集成：
1. 在 Zenodo 创建新的 upload；
2. 上传 `ec-ev-repro-pack-v1.0.zip`；
3. Resource type 建议选择 Dataset 或 Software/Other research output，按你的期刊和实际内容选择；
4. 填写 `ZENODO_METADATA_TEMPLATE.md` 中整理好的元数据；
5. 选择文件公开可见；
6. 预览后发布，获取正式 DOI。

## 五、发布后的论文回填

将正式 Zenodo DOI 与 GitHub 地址填入：
- `README.md`
- `09_docs/DATA_AVAILABILITY_STATEMENT.md`
- 论文正文或 Supplementary Methods 的 Data Availability 部分

若 Zenodo 发布后的文件需要实质性修改，优先创建新版本，不要用新文件覆盖已被引用的旧版本。
