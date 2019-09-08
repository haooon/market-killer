# How to create a Smart Task with Creep Task





## What is a Smart TASK ?

Health Check
Check Point
Tasks Manager
Application interface

## HOW TO USE

#### 1. Simple Usage

```python
class taskA(Task):
    pass

taskA().init()
```

#### 2. Customized Usage

By overwriting `info` (dictionary type) variable, we can customized a smart task. Customizable values listed in the table below.

```python
class taskA(Task):
    info = {
        "name": "teskA",
        "status": CONSTANT.TASK.RUNNING,
        "health": 100
    }
    pass
```

| value name | value description                             |
| ---------- | --------------------------------------------- |
| name       | customized task name                          |
| status     | customized task status                        |
| health     | customized task health status (in developing) |

#### 3. Nested Usage

By overwriting `mount` function, we can customized some nested smart tasks collection.

```python
class taskA(Task):
    pass

class taskB(Task):
    def mount():
        self.in_class_task_A = taskA().init()
    pass

class taskC(Task):
    def mount():
        self.in_class_task_B = taskB().init()
    pass


taskC().init()
```

The above codes will create a task structure like this.

```python
"""		┌taskC─ ─ ─ ─ ─ ─ ─ ─ ┐
Nested  │	┌taskB─ ─ ─ ─ ─┐  │
Task    │	│	┌ taskA ┐  │  │
Struct  │	│	│		│  │  │
        │   │   └ ─ ─ ─ ┘  │  │ 
        │   └ ─ ─ ─ ─ ─ ─  ┘  │ 
        └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘		"""
```

#### 4. Task Manager Usage

Task manager object is designed to surveillance task collection in the project. Manager help to surveillance task health and project health, reboot project or tasks, check and reboot tasks.

```python
task_manager = TaskManager()
```

#### 5. Task Check Point Usage

```python
class taskA(Task):
	@Task.CheckPoint("get data")
    def get_data():
        pass
```

#### 4. Special Task Usage

```python
class quartzTest(Quartz):
    quartz = {
        # 唯一id
        "key": None,
        # 定时器名（可重复，不建议重复）
        "name": "test quartz",
        # 定时器描述
        "describe": "test quartz test",
        # 定时器是否延时模式
        "delay": False,
        # 定时器运行时间间隔
        "interval": 1
    }
    def loop(self):
        print("logic code here")
        pass

```



##### Quartz

