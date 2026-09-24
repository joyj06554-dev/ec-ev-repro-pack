# GitHub + Zenodo 发布步骤

## 一、当前状态

v1.0 的 Creator、ORCID、Affiliation、GitHub 仓库地址和许可证信息均已完成。论文 DOI 尚未分配。Zenodo 已为本版本预留 DOI：`10.5281/zenodo.22941308`；该 DOI 在 Zenodo 正式 Publish 后完成注册。

## 二、Zenodo 草稿

1. 保留当前 Zenodo 草稿，不要删除或重新新建，否则预留 DOI 可能失效。
2. 上传最终文件 `ec-ev-repro-pack-v1.0-zenodo.zip`。
3. Resource type：`Dataset`。
4. Title：`EC-EV Reproducibility Package`。
5. Version：`1.0`。
6. Creator：Honglin Jiang；ORCID：`0000-0001-6012-8071`；Affiliation：`The Second Affiliated Hospital of Chongqing Medical University`。
7. DOI：保留系统已经预留的 `10.5281/zenodo.22941308`。
8. Description、Keywords 与 License 按 `ZENODO_METADATA_TEMPLATE.md` 填写。
9. Files visibility 保持 `Public`。
10. 保存草稿并 Preview，确认文件和元数据无误后再 Publish。

## 三、GitHub

仓库：`https://github.com/joyj06554-dev/ec-ev-repro-pack`。

Zenodo 正式发布后：
1. 确认 DOI `10.5281/zenodo.22941308` 可解析；
2. 创建 GitHub tag：`v1.0`；
3. 创建 GitHub Release，标题：`EC-EV Reproducibility Package v1.0`；
4. Release 后不要静默替换核心文件；实质性修改应发布 v1.1 或更高版本。

## 四、论文回填

在论文 Data Availability 或 Supplementary Methods 中引用：
- Zenodo DOI：`https://doi.org/10.5281/zenodo.22941308`
- GitHub：`https://github.com/joyj06554-dev/ec-ev-repro-pack`

如后续找到原始 5,367 条记录或补充原始分析参数，应发布新版本，而不是静默修改 v1.0。
