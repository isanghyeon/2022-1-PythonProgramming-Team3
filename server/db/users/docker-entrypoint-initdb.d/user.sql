SET GLOBAL general_log = 'ON';
SET GLOBAL general_log_file = '/tmp/general_activity.log';

# -- auto-generated definition
# drop database if exists `users`;
# create schema `users` collate utf8mb4_general_ci;

# use users;

-- auto-generated definition
# drop table if exists `user`;
create table `user`
(
    id                 int auto_increment primary key,
    UserUniqKey        varchar(100)                          null,
    UserName           varchar(50)                           null,
    UserAccountPW      varchar(88)                           not null,
    LastLoginTimestamp timestamp default current_timestamp() not null on update current_timestamp(),
    CreateTimestamp    timestamp default current_timestamp() not null,
    constraint uk_username
        unique (UserName),
    constraint uk_useruniqkey
        unique (UserUniqKey)
);
