drop table if exists entries;
create table `entries` (
    `id` bigint(20)  not null auto_increment comment '����',
    `user_id` int(11) not null default -1 comment 'SSO�û�ID',
    `title` varchar(45) not null default '' comment '���±���',
    `text` text not null default '' comment '��������',
    primary key(`id`)
) comment='����' engine=innodb default charset=utf8;