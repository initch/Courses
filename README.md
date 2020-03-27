# Courses
2020.3.27更新：
- 新增表单：NewBoardForm，用户可提交表单创建Board。
- 重构模板：所有html文件使用同一base.html模板，完善了顶部和面包屑导航栏。

当前功能：课程信息展示与讨论框架，创建新讨论区并提交第一个topic。

## Apps
|app|models|views|说明|
|---|-----|-----|---|
|home||home|主页|
|courses|Course|index,course_details|课程信息，对每门课程设置一个Board讨论区（作为外键）|
|boards|Board,Topic|index,topics|讨论区，Board可以有对应的课程|

待完善的功能：课程信息检索，讨论帖回复……

