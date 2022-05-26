-- auto-generated definition
create table user
(
    id                 int auto_increment primary key,
    UserUniqKey        varchar(100)                           not null,
    UserName           varchar(50)                            not null,
    UserAccountID      varchar(50)                            not null,
    UserAccountPW      varchar(88)                            not null,
    LastLoginTimestamp datetime default '1970-01-01 00:00:00' not null on update current_timestamp(),
    CreateTimestamp    datetime default '1970-01-01 00:00:00' null on update current_timestamp(),
    constraint user_uk
        unique (UserUniqKey, UserAccountID)
);

