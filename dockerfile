# 使用 From osrf/ros:humble-desktop-full作为基础镜像
FROM osrf/ros:humble-desktop-full

# 定义用户和用户组
ARG USERNAME=jiao
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# 更新包列表并安装必要软件
RUN apt-get update \
    && apt-get install -y net-tools nautilus bash-completion gdb sudo
# 创建用户组和用户
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    # 配置用户密码
    && echo "$USERNAME:'" | chpasswd \
    # 允许用户使用 sudo
    && usermod -aG sudo $USERNAME \
    && echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
    && echo 'source /opt/ros/humble/setup.bash' >> /home/$USERNAME/.bashrc \
    # 使新用户的 `.bashrc` 文件生效
    && chown $USERNAME:$USERNAME /home/$USERNAME/.bashrc


# 切换到新用户
USER $USERNAME
WORKDIR /home/$USERNAME/opencv

# 切换回 root 用户
USER root

# 安装 GitKraken
COPY ./111.jpg /home/jiao/opencv/111.jpg
COPY ./show_pic.py /home/jiao/opencv/show_pic.py
COPY ./gitkraken-amd64.deb /home/jiao/opencv/packages/gitkraken-amd64.deb
RUN DEBIAN_FRONTEND=noninteractive apt install -y /home/jiao/opencv/packages/gitkraken-amd64.deb


# 切换回 nagisa 用户并设置命令
USER $USERNAME

# 默认命令运行 show_pic.py
CMD ["/bin/bash"]
