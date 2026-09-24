# GitHub + Zenodo 发布步骤

## 一、发布前元数据

v1.0 的 Creator、ORCID、Affiliation 和许可证信息已经完成。论文 DOI 尚未分配；Zenodo DOI 待归档后生成。

## 二、GitHub

1. 仓库：`joyj06554-dev/ec-ev-repro-pack`。
2. 仓库根目录应包含正式 `CITATION.cff`。
3. 正式混合许可证文件已加入：`LICENSE`、`LICENSE-CODE`、`LICENSE-DATA-DOCS`。
4. 创建标签 `v1.0`。
5. 以 `v1.0` 创建 GitHub Release，标题建议：`EC-EV Reproducibility Package v1.0`。
6. Release 后不要静默替换核心文件；实质性修改应发布 v1.1/v2.0。

## 三、Zenodo：推荐使用 GitHub 集成

1. 登录 Zenodo 并连接 GitHub 账户。
2. 在 Zenodo 的 GitHub 页面同步仓库。
3. 找到 `ec-ev-repro-pack` 并启用归档。
4. GitHub 侧创建新 Release 后，由 Zenodo 归档相应版本。
5. 核对 Zenodo 记录中的 Title、Creator、ORCID、Affiliation、Description、Version、Keywords、License 和 GitHub repository。
6. Zenodo DOI 生成后，将 DOI 回填到主分支 README、Data Availability 和 Citation metadata；不要改写已冻结的 GitHub Release 内容。

## 四、Zenodo：手工上传备选方案

如果不使用 GitHub 自动集成：
1. 在 Zenodo 创建新 upload；
2. 上传最终的 `ec-ev-repro-pack-v1.0-final.zip`；
3. Resource type 选择 Dataset；
4. 按 `ZENODO_METADATA_TEMPLATE.md` 填写元数据；
5. 发布后获取 DOI。

## 五、论文回填

将正式 Zenodo DOI 填入：
- `README.md`
- `09_docs/DATA_AVAILABILITY_STATEMENT.md`
- 论文正文或 Supplementary Methods 的 Data Availability 部分

如后续找到原始 5,367 条记录或补充原始分析参数，应发布新版本而不是静默修改 v1.0。
