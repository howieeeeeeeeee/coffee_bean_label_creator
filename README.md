# 咖啡豆標籤生成器 (Coffee Bean Label Generator)

## 專案目標與概述

歡迎來到我的咖啡豆標籤生成器！這個應用程式是專為我的家庭烘焙咖啡事業設計的，旨在幫助我快速、輕鬆地為新烘焙的咖啡豆製作精美的客製化標籤。

透過這個工具，使用者（也就是我！）可以輸入咖啡豆的詳細資訊，例如產地、名稱、處理法、烘焙程度、風味描述，甚至烘焙日期。後端伺服器會將這些資訊整合到預設的標籤模板上，並提供可下載的 PNG 圖片。

## 主要功能

*   **客製化標籤生成**：根據輸入的咖啡豆資訊，即時生成獨特的咖啡標籤。
*   **即時預覽**：在下載前預覽生成的標籤，確保內容和排版符合預期。
*   **多種下載選項**：
    *   直接下載生成的 PNG 標籤。
    *   下載旋轉 90 度後的 PNG 標籤，方便不同包裝需求。
*   **動態產地顯示**：根據選擇的產地，標籤上會顯示對應的中文產地名稱和地圖圖示。
*   **響應式網頁設計 (RWD)**：介面會根據螢幕大小自動調整，無論在桌面或手機上都能提供良好的使用體驗。
*   **多語言支援**：網頁介面已本地化為繁體中文，方便使用。

## 使用技術

*   **後端**：
    *   Python 3
    *   [Flask](https://flask.palletsprojects.com/)：輕量級的 Web 框架。
    *   [Pillow (PIL Fork)](https://python-pillow.org/)：強大的圖像處理庫，用於標籤的圖片合成。
    *   [Gunicorn](https://gunicorn.org/)：Python WSGI HTTP Server，用於生產環境部署。
*   **前端**：
    *   HTML5
    *   CSS3 (響應式設計)
    *   JavaScript
*   **依賴管理**：
    *   [Pipenv](https://pipenv.pypa.io/en/latest/)：用於管理專案的 Python 依賴和虛擬環境。
*   **部署**：
    *   [Render](https://render.com/)：使用 `render.yaml` 進行自動化部署。

## 專案結構

```
/coffee-label-generator/
|-- app.py                  # Flask 應用程式主文件，包含圖片生成邏輯
|-- Pipfile                 # Pipenv 依賴定義
|-- Pipfile.lock            # Pipenv 依賴鎖定文件，確保環境一致性
|-- render.yaml             # Render 部署配置
|-- README.md               # 本文件
|
|-- /static/
|   |-- template.png        # 空白標籤背景模板 (需自行準備)
|   |-- /css/
|   |   |-- style.css       # 前端樣式
|   |-- /js/
|   |   |-- main.js         # 前端表單處理與預覽邏輯
|   |-- /fonts/
|   |   |-- SourceHanSerifTW-Bold.otf # 中文字體 (需自行準備)
|   |   |-- ...             # 其他字體
|   |-- /images/
|       |-- /origins/
|           |-- 肯亞.png      # 產地地圖圖示 (需自行準備)
|           |-- 衣索比亞.png  # 產地地圖圖示 (需自行準備)
|           |-- 哥倫比亞.png  # 產地地圖圖示 (需自行準備)
|           |-- ...         # 其他產地圖示
|
|-- /templates/
    |-- index.html          # 使用者輸入表單頁面
```

## 本地環境設定與運行

請按照以下步驟在您的本地機器上設定並運行應用程式：

1.  **克隆儲存庫**：
    ```bash
    git clone https://github.com/howieeeeeeeeee/coffee_bean_label_creator.git
    cd coffee_bean_label_creator
    ```

2.  **準備圖片與字體資源**：
    *   將您的空白標籤背景圖片命名為 `template.png` 並放置於 `static/` 目錄。
    *   將您使用的字體文件（例如 `SourceHanSerifTW-Bold.otf`）放置於 `static/fonts/` 目錄。
    *   將各產地的地圖圖示（例如 `肯亞.png`, `衣索比亞.png`）放置於 `static/images/origins/` 目錄。
    *   **重要**：請確保 `app.py` 中字體文件的路徑和圖片文件的名稱與您實際放置的檔案相符。

3.  **安裝依賴**：
    使用 Pipenv 安裝所有必要的 Python 依賴。這將會創建一個虛擬環境並安裝 `Flask`, `Pillow`, `gunicorn` 等。
    ```bash
    pipenv install --deploy --system
    ```

4.  **運行應用程式**：
    啟動 Flask 開發伺服器。應用程式將在 `http://127.0.0.1:5001` 上運行。
    ```bash
    pipenv run python app.py
    ```

5.  **訪問應用程式**：
    在您的網頁瀏覽器中打開 `http://127.0.0.1:5001`。

## 部署到 Render

這個專案已經配置了 `render.yaml` 文件，可以輕鬆部署到 Render 平台。

1.  **創建 Render 帳戶**：如果您還沒有帳戶，請前往 [Render.com](https://render.com/) 註冊。
2.  **連接您的 Git 儲存庫**：
    *   登錄 Render 後，點擊 "New" -> "Web Service"。
    *   選擇您的 Git 提供商（例如 GitHub），並連接 `coffee_bean_label_creator` 儲存庫。
3.  **配置 Web Service**：
    *   Render 會自動檢測 `render.yaml` 文件並預填充大部分設定。
    *   確保 **Root Directory** 設置為儲存庫的根目錄。
    *   **Build Command** 應該自動設置為 `pipenv install --deploy --system`。
    *   **Start Command** 應該自動設置為 `gunicorn app:app`。
    *   選擇 **Python 3** 環境。
    *   選擇適合您的 **Instance Type**。
4.  **創建 Web Service**：點擊 "Create Web Service" 開始部署。

Render 將會自動拉取您的代碼，安裝依賴，並啟動應用程式。部署完成後，您將獲得一個公開的 URL，可以從任何地方訪問您的咖啡標籤生成器！
