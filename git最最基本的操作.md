### 1.首先克隆前人的库,或者创建一个库
```shell
git clone 地址
git init
```

### 2.初始化用户名
```shell
git config --global user.name "用户名"
```

### 3.设置用户邮箱
```shell
git config --global user.email "邮箱地址"

```

### 4.修改文件（夹） mkdir/cd/ls/vim...

### 5.添加文件到缓存区
```shell
git add main.py(文件名)
```

### 6.把缓存区的文件添加到本地库
```shell
git commit -m '这里面是描述信息'
```

### 7.把本地库的内容更新到github
```shell
git push
```


基本完成

**注意**: 20年七月之后 github 放弃在git上使用用户密码的方式执行操作
```shell
ssh-keygen -t ed25519 -C "用户邮箱"
```

**注意**：如果使用的旧系统不支持Ed25519算法，请使用：
```shell
$ ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

当提示您“输入要在其中保存密钥的文件”时，请按Enter。这接受默认文件位置。
```shell
> Enter a file in which to save the key (/c/Users/you/.ssh/id_ed25519):[Press enter]
```


在提示符下，键入一个安全的密码短语。
```shell
> Enter passphrase (empty for no passphrase): [Type a passphrase]
> Enter same passphrase again: [Type passphrase again]
```















