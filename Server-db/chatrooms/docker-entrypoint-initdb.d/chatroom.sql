SET GLOBAL general_log='ON';
SET GLOBAL general_log_file='/tmp/general_activity.log';

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
    ParticipantUName            longtext  default 0                   not null,
    ParticipantUniqKey          longtext  default 0                   not null,
    NewUserParicipatedTimestamp timestamp default '0000-00-00 00:00:00' not null on update current_timestamp(),
    LastChatTimestamp           timestamp default '0000-00-00 00:00:00' not null on update current_timestamp(),
    CreateTimestamp             timestamp default '0000-00-00 00:00:00' not null on update current_timestamp(),
    constraint uk_chatuniqkey
        unique (ChatUniqKey)
);

