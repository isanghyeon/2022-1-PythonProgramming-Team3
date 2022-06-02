SET GLOBAL general_log = 'ON';
SET GLOBAL general_log_file = '/tmp/general_activity.log';

# -- auto-generated definition
# drop database if exists `chatrooms`;
# create schema `chatrooms` collate utf8mb4_general_ci;

# use chatrooms;

-- auto-generated definition
# drop table if exists `chatroom`;
create table `chatroom`
(
    id                          int auto_increment primary key,
    ChatUniqKey                 varchar(100)                          not null,
    ParticipantUserName         longtext  default 0                   not null,
    ParticipantUserUniqKey      longtext  default 0                   not null,
    ParticipantNewUserTimestamp timestamp default current_timestamp() not null,
    LastChatTimestamp           timestamp default current_timestamp() not null,
    CreateTimestamp             timestamp default current_timestamp() not null,
    constraint uk_chatuniqkey
        unique (ChatUniqKey)
);

