```shell
创建本地持久化
mkdir -p /docker/mongodb
mkdir -p /docker/mysql

docker 创建mongodb
docker run --name mongodb-server -v /docker/mongodb:/data/db -d -p 27017:27017 mongo --auth

mongodb创建用户
db.createUser({ user: 'root', pwd: '1141135276Shr', roles: [ { role: "root", db: "admin" } ] });
db.createUser({ user: 'haooon', pwd: '1141135276Shr', roles: [ { role: "readWrite", db: "app" } ] });

docker 创建mysql
docker run -d -p 33060:3306 --privileged=true -v /docker/mysql/conf/my.cnf:/etc/mysql/my.cnf -v /docker/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=1141135276Shr --name mysql mysql/mysql-server

docker 代理ip池
docker run -d -p 8899:8899 -p 8081:8081 -v /var/www/scylla:/var/www/scylla --name scylla wildcat/scylla:latest

docker 跑项目
docker build -t market-killer:1.0 .
docker run -d -p 8888:8888 --name market-killer -v /docker/steam:/market-killer market-killer:1.0 python /market-killer/market-killer/main.py

mkdir -p /docker/neo4j/data
mkdir -p /docker/neo4j/logs
mkdir -p /docker/neo4j/conf

docker run \
    --detach \
    --publish=7474:7474 --publish=7687:7687 \
    --volume=/docker/neo4j/data:/data \
    --volume=/docker/neo4j/logs:/logs \
    --volume=/docker/neo4j/conf:/conf \
    --env=NEO4J_AUTH=neo4j/1141135276Shr \
    neo4j

```



线程池越多越好吗（test对比测试）

责任链模式接口（）

cache缓冲Task（生产者，消费者）（数据持久（系统数据库））

neo4j图数据库（python接口支持）

mongodb和neo4j 于 elasticsearch混用（数据是否重复是否可以直接加载）

elasticsearch（python接口支持）

示例代码（buff爬虫，多购物平台比价系统）

主节点子节点任务模式（分布式（任务注册，任务分配））

模式识别，学习功能。

bob project

smart city


