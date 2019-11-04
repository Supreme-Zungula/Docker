# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yzungula <yzungula@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/11/04 08:58:40 by yzungula          #+#    #+#              #
#    Updated: 2019/11/04 10:37:31 by yzungula         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM debian

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y wget bzip2 tar

WORKDIR /tmp

RUN wget https://files.teamspeak-services.com/releases/server/3.9.1/teamspeak3-server_linux_amd64-3.9.1.tar.bz2
RUN tar -xjf teamspeak3-server_linux_amd64-3.9.1.tar.bz2
RUN mv teamspeak3-server_linux_amd64 teamspeak

# add user
RUN adduser --disabled-password --gecos "" teamspeak
RUN chown -R teamspeak:teamspeak teamspeak
RUN chmod +x teamspeak

ENV TS3SERVER_LICENSE=accept

# expose used ports
EXPOSE 30033
EXPOSE 10011
EXPOSE 9987/udp

WORKDIR /tmp/teamspeak

ENTRYPOINT sh ts3server_minimal_runscript.sh

# docker run -p 9987:9987/udp -p 10011:10011 -p 30033:30033 -e TS3SERVER_LICENSE=accept
