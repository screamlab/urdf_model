# 成果圖
## 二輪自走車
![二輪自走車](https://github.com/alianlbj23/urdf_model/blob/main/pic/%E4%BA%8C%E8%BC%AA%E8%87%AA%E8%B5%B0%E8%BB%8A(%E6%9C%89lidar).png?raw=true)
## 麥克納姆倫自走車
![麥克納姆倫自走車](https://github.com/alianlbj23/urdf_model/blob/main/pic/%E9%BA%A5%E5%85%8B%E7%B4%8D%E5%A7%86%E5%80%AB%E8%BB%8A(%E6%9C%89lidar).png?raw=true)
## 機械手臂
![機械手臂](https://github.com/alianlbj23/urdf_model/blob/main/pic/%E6%A9%9F%E6%A2%B0%E6%89%8B%E8%87%82.png?raw=true)

## 上銀機械手臂
![上銀機械手臂](https://github.com/alianlbj23/urdf_model/blob/main/pic/hiwin%E6%A9%9F%E6%A2%B0%E6%89%8B%E8%87%82.png?raw=true)
# 需先具備工具
* https://github.com/syuntoku14/fusion2urdf (將fusion轉成urdf)
* https://github.com/doctorsrn/xacro2urdf (將xacro轉成urdf)
* https://github.com/Unity-Technologies/URDF-Importer (將urdf匯入unity)
* fusion360
* https://www.youtube.com/watch?v=080UAkOeeUM&t=479s (完整製作教學影片)
# urdf車體製作
1. 先將fusion轉乘urdf的套件裝好
2. 用fusion繪製出車體(下面有車體製作注意)
3. fusion上方工具bar的UTILITIES->ADD-INS點Scripts and Add-ins的urdf exporter進行匯出
4. 進入匯出的urdf內的xacro點進去有個mesh filename後面有個名稱，在同個資料夾創同名資料夾後將上一層mesh檔案丟入剛剛創的資料夾，好讓他找他材料檔
5. 照著xacro轉成urdf的程式碼教學轉成urdf
## 車體製作注意
* 一定要有基準的零件取名叫base_link
* 零件下面不能有零件
* join時下面的數字絕對都要是0
* 若想將零件join時改變join位置，可先改變零件body的角度再去join(改變body不會造成影響)
* 盡可能的將零件越少越好(可將其他零件的body底下的東西拖拉到其他零件的body做組合，藉此減少零件量)