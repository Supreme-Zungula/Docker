# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yzungula <yzungula@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/10/28 17:17:44 by yzungula          #+#    #+#              #
#    Updated: 2019/10/30 17:04:41 by yzungula         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

FROM debian

RUN apt-get update && apt-get update
RUN apt-get install wget -y
RUN apt-get install bzip2 -y
RUN apt-get install tar -y
CMD ["su", "--shell", "/bin/bash", "ts"]
RUN wget -P /tmp/ https://files.teamspeak-services.com/releases/server/3.6.1/teamspeak3-server_linux_amd64-3.6.1.tar.bz2
WORKDIR /home/ts

RUN bunzip2 /tmp/teamspeak3-server_linux_amd64-3.6.1.tar.bz2
RUN tar -xf /tmp/teamspeak3-server_linux_amd64-3.6.1.tar -C /home/ts

# CMD ["touch", "/home/ts/.ts3server_license_accepted"]
ENV TS3SERVER_LICENSE=accept
RUN sh teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh

# -d /home/ts
# RUN tar --help
