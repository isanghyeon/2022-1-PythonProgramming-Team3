SET GLOBAL general_log='ON';
SET GLOBAL general_log_file='/tmp/general_activity.log';

# -- auto-generated definition
# drop database if exists `messages`;
# create schema `messages` collate utf8mb4_general_ci;

# use messages;

-- auto-generated definition
# drop table if exists `message`;
create table `message`
(
    id                          int auto_increment primary key,
    UserUniqKey                 varchar(100)                                not null,
    ChatUniqKey                 varchar(100)                                not null,
    MessageType                 tinyint(4) default 0                        not null,
    MessageData                 text default 0                              not null,
    MediaDataPath               text default 0                              not null,
    MessageTimestamp            timestamp default '0000-00-00 00:00:00'     not null on update current_timestamp()
);

