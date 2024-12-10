[English](README.md) | [中文](README.zh.md)

# EasyDependencyCheck

## 概述

EasyDependencyCheck是基于开源项目[Dependency Check](https://github.com/jeremylong/DependencyCheck)的脚本。这个脚本旨在简化Dependency Check的使用，特别是对于那些由于网络限制无法拉取NVD数据库或觉得Dependency Check难以使用的人。

**警告：** 本项目仅用于提高网络安全性和减少漏洞。严禁将本项目用于非法目的。它仅用于学习和交流。任何对本项目的滥用，作者概不负责。

这是一个测试版本，可能存在一些不完善之处。NVD数据库将定期维护，以确保最新的漏洞数据。

## 需求

- Python 3  (如果你使用exe来运行程序，则python环境不是必须的)
- Docker

## 安装和使用

### 加载Dependency Check Docker镜像

你可以从Docker Hub拉取最新的镜像：`docker pull obsidian6362/easy-dependency-check:latest`

### 克隆仓库

1. 克隆仓库：`git clone https://github.com/BunnyPunch-handsome/EasyDependencyCheck.git`
2. 进入克隆的仓库目录：`cd EasyDependencyCheck`

### 运行脚本或可执行文件

你可以使用Python运行脚本，或者使用预构建的可执行文件（适用于Windows）。

#### 使用Python脚本

运行以下命令来运行脚本：`python EasyDependencyCheck.py`

#### 使用可执行文件（Windows）

1. 从releases页面下载预构建的可执行文件。
2. 通过双击运行该可执行文件。

### 脚本界面使用

1. Jar文件：点击“浏览”选择你要扫描的jar文件。
2. 报告路径：点击“浏览”选择你想要保存报告的路径。
3. 漏洞数据库更新：如果你想更新漏洞数据库，选择“是”，并在提示时输入NVD API密钥。
4. 日志：查看扫描过程的日志输出。
5. 扫描按钮：点击“扫描”开始漏洞扫描。

### 文件夹结构

- EasyDependencyCheck.py：用于运行漏洞扫描的主脚本文件。
- README.md：此文档文件。

## 注意事项

- 确保你的系统上已安装并运行Docker。
- 如果更新数据库，本脚本需要网络连接来拉取最新的漏洞数据。

## 免责声明

本项目“按原样”提供，不提供任何形式的担保。作者不对本项目的任何滥用承担责任。风险自负。作者不对因使用本项目引起的任何损害或损失负责。用户需确保遵守当地法律法规。本项目仅供教育和研究用途。严禁将本项目用于任何未经授权的目的。
