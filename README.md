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
        self.in_class_task = taskA().init()
    pass

taskB().init()
```

#### 4. Task Manager Usage

Task manager object is designed to surveillance task collection in the project. Manager help to surveillance task health and project health, reboot project or tasks, check tasks and help to them 



#### 4. Special Task Usage

##### Quartz

