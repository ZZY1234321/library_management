<div align="center">

# 圖書館管理系統

**繁體中文**  | [English](readme/README.ENG.md)  | [简体中文](/README.md)

</div>

 

## 一、專案概述

本專案是中國石油大學（北京），即CUPB的2023 - 2024學年第二學期資料庫課程設計作業，採用Python + SQL打造了一個前後端一體化的圖書館管理系統，為圖書館的日常運營與資源管理提供高效數位化解決方案。

 

## 二、功能特性

### （一）圖書管理

- **精準錄入與修改**：細緻錄入圖書名稱、作者、出版社、出版年份、ISBN、庫存等關鍵資訊，確保圖書資料完整精確；同時可靈活修改圖書詳情，即時更新圖書狀態與資訊。

- **智能檢索與篩選**：依據書名、作者、ISBN等多維度快速檢索圖書，支援按類別、出版年份區間精準篩選，助管理員迅速定位目標圖書。

 

### （二）讀者管理

- **資訊登記與維護**：全面登記讀者姓名、性別、年齡、聯絡方式、借閱證號等基礎資料，方便更新讀者資訊，確保資料時效性與準確性。

- **借閱歷史追溯**：清晰記錄讀者借閱圖書的名稱、借閱日期、歸還日期、逾期情況等歷史軌跡，為借閱管理與讀者服務提供有力資料支撐。

 

### （三）借閱歸還流程優化

- **便捷借閱操作**：管理員依讀者借閱證號與圖書ISBN迅速辦理借閱，自動更新圖書庫存與讀者借閱狀態，即時記錄借閱日期，開啟借閱流程無縫對接。

- **智能歸還處理**：歸還圖書時，系統依ISBN精準核對圖書資訊，自動檢查逾期狀況並計算罰金（如有），依實際情況更新圖書庫存與讀者借閱記錄，確保圖書流轉高效透明。

 

### （四）庫存監控與預警

- **即時庫存洞察**：即時呈現各圖書庫存數量，直觀展示庫存動態變化，為採購決策提供即時資料依據。

- **智能預警機制**：當庫存臨近預設閾值，系統自動觸發預警，及時提示管理員補貨，避免圖書缺貨影響讀者借閱體驗。

 

## 三、技術架構

### （一）前端開發

- **HTML5 + CSS3協同布局**：運用HTML5構建穩固頁面結構，CSS3精心雕琢樣式，打造美觀舒適、交互友好的使用者介面，確保跨平台一致性瀏覽體驗。

- **JavaScript交互賦能**：引入JavaScript為頁面注入交互活力，實現表單驗證、動態資料加載、菜單交互等功能，提升使用者操作流暢性與便捷性。

 

### （二）後端開發

- **Python核心驅動**：憑藉Python強大編程能力，編寫高效業務邏輯代碼，實現系統核心功能模組，保障系統運行穩定可靠、性能卓越。

- **SQL資料庫交互**：借助SQL語句與資料庫緊密交互，精心設計圖書表、讀者表、借閱記錄表等多表結構，通過複雜查詢、更新、插入操作實現資料高效存取與管理。

 

### （三）資料庫選型

- **MySQL穩健支撐**：選用MySQL資料庫，憑藉其成熟穩定性、高並發處理能力與豐富功能特性，為系統海量資料存儲、快速檢索、複雜關聯查詢提供堅實底層架構。

 

## 四、文件結構說明

- **`.idea`**：整合開發環境（IDE）配置文件專屬目錄，存儲專案個性化設定與元資料，助力開發環境精準配置。

- **`__pycache__`**：Python位元組碼緩存資料夾，存放編譯生成的位元組碼文件，優化代碼二次加載效率，提升系統運行性能。

- **`models`**：資料模型定義核心區域，封裝資料庫表結構與操作邏輯，實現物件導向程式設計風格資料交互，提升代碼模組化與可維護性。

- **`static/css`**：靜態資源CSS樣式表匯聚地，集中管理頁面布局、樣式設計文件，確保樣式統一改動與高效維護。

- **`templates`**：HTML模板文件存儲庫，採用模板引擎技術實現頁面動態渲染，分離資料與展示邏輯，增強代碼可讀性與複用性。

- **`README.md`**：專案說明文件，即您正在閱讀的文件，為開發者、使用者提供專案全面指引與技術解讀。

- **`app.py`**：後端Flask應用主入口文件，統籌路由定義、請求處理分發、應用啟動配置，構建系統整體運行框架。

- **`mysqlUtils.py`**：MySQL資料庫操作工具模組，封裝資料庫連接建立、查詢執行、事務處理等通用函數，簡化資料庫交互代碼編寫，提升代碼複用性與可測試性。

 

## 五、安裝部署指南

### （一）環境準備

- 安裝Python 3.6官方版本，確保pip套件管理器正常運行，為專案依賴安裝筑牢基礎。

- 下載並安裝MySQL資料庫社區版，依官方文件完成基礎配置，開啟遠端存取權限，保障資料庫服務穩定啟動與監聽。

 

### （二）專案複製與依賴安裝

1. 複製本專案倉庫至本地開發目錄：`git clone https://github.com/ZZY1234321/library_management.git`
2. `library_management\venv\Lib\site-packages`中包括所有本專案需要的核心依賴庫，專案環境完備。

 

### （三）資料庫配置與初始化

1. 依實際環境配置修改`mysqlUtils.py`文件中的資料庫連接參數，精準指向本地或遠端MySQL資料庫實例。
2. 執行專案提供的資料庫初始化腳本（如SQL文件）創建必要資料表及初始資料，或利用Flask應用內建資料庫遷移工具（如Flask-Migrate）依模型定義創建、更新資料庫架構，搭建穩固資料存儲框架。

 

### （四）啟動應用

在專案根目錄下執行啟動命令：`python app.py`，Flask應用將預設監聽本地5000端口（可配置），在瀏覽器訪問`http://localhost:5000`開啟圖書館管理系統之旅。

 

## 六、貢獻指南

歡迎廣大開發者為本專案貢獻智慧與力量！若您期望參與貢獻，請遵循以下流程：

1. **Fork本專案倉庫**：在GitHub平台創建專案個人分支，開啟獨立開發之旅。
2. **複製Fork後倉庫至本地**：`git clone [您的倉庫URL]`，將遠端代碼庫拉取至本地開發環境，搭建工作副本。
3. **創建特性分支**：基於`master`分支創建獨立特性開發分支，如`feature/[分支名稱]`，確保功能開發隔離，避免干擾主代碼流。
4. **開發與提交**：於特性分支中編碼實現新功能或修復缺陷，遵循專案代碼風格規範，提交時撰寫清晰、精準、描述性強的提交資訊，助力團隊理解代碼變更意圖與目的。
5. **推送與Pull Request**：完成開發後將特性分支推送至個人遠端倉庫，在GitHub發起Pull Request至本專案`master`分支，詳述功能、修復內容及測試情況，團隊將及時評審、反饋、合併，共同提升專案品質與功能完整性。

 

## 七、版權聲明

本專案遵循開源協議發布，在合法合規框架下，您可自由使用、修改、分發代碼，但請保留原作者版權聲明與許可