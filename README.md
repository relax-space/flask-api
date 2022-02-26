# flask-api

restful风格api

## 开始

1. 本地启动mysql,并创建test1数据库
2. 运行如下命令`python main.py`

### 新增

```
POST
127.0.0.1:8080/fruits
可以多添加几次,多添加几条数据

{
    "price": 1,
    "name":"apple"
}

{
    "price": 2,
    "name":"pear"
}

```

### 删除

```
DELETE
127.0.0.1:8080/fruits/1

```

### 修改

```
POST
127.0.0.1:8080/fruits/2

{
    "price": 40,
}

```


### 查询单个

```
POST
127.0.0.1:8080/fruits/2

{
    "price": 4,
    "name":"pear1"
}

```

### 查询所有

```
POST
127.0.0.1:8080/fruits

127.0.0.1:8080/fruits?limit=1&offset=0


```