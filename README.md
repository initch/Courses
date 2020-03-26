# Courses
当前功能：课程信息展示与讨论框架。

## Apps
|app|models|views|说明|
|---|-----|-----|---|
|home||home|主页|
|courses|Course|index,course_details|课程信息，对每门课程设置一个Board讨论区（作为外键）|
|boards|Board,Topic|index,topics|讨论区，Board可以有对应的课程|

待完善的功能：课程信息检索，讨论帖回复……

