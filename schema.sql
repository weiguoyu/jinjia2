drop table if exists entries;
create table `entries` (
    `id` bigint(20)  not null auto_increment comment '主键',
    `user_id` int(11) not null default -1 comment 'SSO用户ID',
    `title` varchar(45) not null default '' comment '文章标题',
    `text` text not null default '' comment '文章内容',
    primary key(`id`)
) comment='文章' engine=innodb default charset=utf8;