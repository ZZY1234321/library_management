<div align="center">

# 图书馆管理系统

**简体中文** | [English](/readme/README.ENG.md) | [繁體中文](/readme/README.zh_TW.md)

</div>

## 一、项目概述
本项目是中国石油大学（北京）2023-2024学年第二学期数据库课程设计作业，采用 Python + SQL 打造了一个前后端一体化的图书馆管理系统，为图书馆的日常运营与资源管理提供高效数字化解决方案。

## 二、功能特性
### （一）图书管理
- **精准录入与修改**：细致录入图书名称、作者、出版社、出版年份、ISBN、库存等关键信息，确保图书数据完整精确；同时可灵活修改图书详情，实时更新图书状态与信息。
- **智能检索与筛选**：依据书名、作者、ISBN 等多维度快速检索图书，支持按类别、出版年份区间精准筛选，助管理员迅速定位目标图书。

### （二）读者管理
- **信息登记与维护**：全面登记读者姓名、性别、年龄、联系方式、借阅证号等基础资料，方便更新读者信息，确保数据时效性与准确性。
- **借阅历史追溯**：清晰记录读者借阅图书的名称、借阅日期、归还日期、逾期情况等历史轨迹，为借阅管理与读者服务提供有力数据支撑。

### （三）借阅归还流程优化
- **便捷借阅操作**：管理员依读者借阅证号与图书 ISBN 迅速办理借阅，自动更新图书库存与读者借阅状态，实时记录借阅日期，开启借阅流程无缝对接。
- **智能归还处理**：归还图书时，系统依 ISBN 精准核对图书信息，自动检查逾期状况并计算罚金（如有），依实际情况更新图书库存与读者借阅记录，确保图书流转高效透明。

### （四）库存监控与预警
- **实时库存洞察**：实时呈现各图书库存数量，直观展示库存动态变化，为采购决策提供即时数据依据。
- **智能预警机制**：当库存临近预设阈值，系统自动触发预警，及时提示管理员补货，避免图书缺货影响读者借阅体验。

## 三、技术架构
### （一）前端开发
- **HTML5 + CSS3 协同布局**：运用 HTML5 构建稳固页面结构，CSS3 精心雕琢样式，打造美观舒适、交互友好的用户界面，确保跨平台一致性浏览体验。
- **JavaScript 交互赋能**：引入 JavaScript 为页面注入交互活力，实现表单验证、动态数据加载、菜单交互等功能，提升用户操作流畅性与便捷性。

### （二）后端开发
- **Python 核心驱动**：凭借 Python 强大编程能力，编写高效业务逻辑代码，实现系统核心功能模块，保障系统运行稳定可靠、性能卓越。
- **SQL 数据库交互**：借助 SQL 语句与数据库紧密交互，精心设计图书表、读者表、借阅记录表等多表结构，通过复杂查询、更新、插入操作实现数据高效存取与管理。

### （三）数据库选型
- **MySQL 稳健支撑**：选用 MySQL 数据库，凭借其成熟稳定性、高并发处理能力与丰富功能特性，为系统海量数据存储、快速检索、复杂关联查询提供坚实底层架构。

## 四、文件结构说明
- **`.idea`**：集成开发环境（IDE）配置文件专属目录，存储项目个性化设置与元数据，助力开发环境精准配置。
- **`__pycache__`**：Python 字节码缓存文件夹，存放编译生成的字节码文件，优化代码二次加载效率，提升系统运行性能。
- **`models`**：数据模型定义核心区域，封装数据库表结构与操作逻辑，实现面向对象编程风格数据交互，提升代码模块化与可维护性。
- **`static/css`**：静态资源 CSS 样式表汇聚地，集中管理页面布局、样式设计文件，确保样式统一修改与高效维护。
- **`templates`**：HTML 模板文件存储库，采用模板引擎技术实现页面动态渲染，分离数据与展示逻辑，增强代码可读性与复用性。
- **`README.md`**：项目说明文档，即您正在阅读的文件，为开发者、使用者提供项目全面指引与技术解读。
- **`app.py`**：后端 Flask 应用主入口文件，统筹路由定义、请求处理分发、应用启动配置，构建系统整体运行框架。
- **`mysqlUtils.py`**：MySQL 数据库操作工具模块，封装数据库连接建立、查询执行、事务处理等通用函数，简化数据库交互代码编写，提升代码复用性与可测试性。

## 五、安装部署指南
### （一）环境准备
- 安装 Python 3.6 官方版本，确保 pip 包管理器正常运行，为项目依赖安装筑牢基础。
- 下载并安装 MySQL 数据库社区版，依官方文档完成基础配置，开启远程访问权限，保障数据库服务稳定启动与监听。

### （二）项目克隆与依赖安装
1. 克隆本项目仓库至本地开发目录：`git clone https://github.com/ZZY1234321/library_management.git`
2. `library_management\venv\Lib\site-packages` 中包括所有本项目需要的核心依赖库，项目环境完备。

### （三）数据库配置与初始化
1. 依实际环境配置修改`mysqlUtils.py`文件中的数据库连接参数，精准指向本地或远程 MySQL 数据库实例。
2. 执行项目提供的数据库初始化脚本（如 SQL 文件）创建必要数据表及初始数据，或利用 Flask 应用内建数据库迁移工具（如 Flask-Migrate）依模型定义创建、更新数据库架构，搭建稳固数据存储框架。

### （四）启动应用
在项目根目录下执行启动命令：`python app.py`，Flask 应用将默认监听本地 5000 端口（可配置），在浏览器访问`http://localhost:5000`开启图书馆管理系统之旅。

## 六、贡献指南
欢迎广大开发者为本项目贡献智慧与力量！若您期望参与贡献，请遵循以下流程：
1. **Fork 本项目仓库**：在 GitHub 平台创建项目个人分支，开启独立开发之旅。
2. **克隆 Fork 后仓库至本地**：`git clone [您的仓库 URL]`，将远程代码库拉取至本地开发环境，搭建工作副本。
3. **创建特性分支**：基于`master`分支创建独立特性开发分支，如`feature/[分支名称]`，确保功能开发隔离，避免干扰主代码流。
4. **开发与提交**：于特性分支中编码实现新功能或修复缺陷，遵循项目代码风格规范，提交时撰写清晰、精准、描述性强的提交信息，助力团队理解代码变更意图与目的。
5. **推送与 Pull Request**：完成开发后将特性分支推送至个人远程仓库，在 GitHub 发起 Pull Request 至本项目`master`分支，详述功能、修复内容及测试情况，团队将及时评审、反馈、合并，携手提升项目品质与功能完整性。

## 七、版权声明
本项目遵循开源协议发布，在合法合规框架下，您可自由使用、修改、分发代码，但请保留原作者版权声明与许可信息，共同维护开源生态健康发展。

## 八、联系作者
若您于项目使用、开发过程遇技术难题、功能建议或期望深度合作交流，请通过以下方式联系作者：
- **GitHub 账号**：[ZZY1234321](https://github.com/ZZY1234321)
- **电子邮箱**：ZSDZZY2022@163.com
