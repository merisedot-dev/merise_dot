-- Generated with merise_dot

drop database mgraph;

create database mgraph;

create table e_0 (
    pk_e_o int primary key not null,
    fk_l_4_5 int not null
);

create table e_1 (
    pk_e_1 int primary key not null,
    fk_e_2 int,

    constraint fk_e_1_e_2
        foreign key(fk_e_2)
        references e_2.pk_e_2
);

create table e_2 (
    pk_e_2 int primary key not null,
    fk_e1 int not null,

    constraint fk_e_2_e_1
        foreign key(fk_e_1)
        references e_1.pk_e_1
);

create table e_3 (
    pk_e_3 int primary key not null
);

create table e_4 (
    pk_e_4 int primary key not null
);

create table l_4_5 (
    pk_l_4_5 int primary key not null,
    fk_e_2 int not null,
    fk_e_3 int not null,

    constraint fk_l_45_e_2
        foreign key(fk_e_2)
        references e_2.pk_e_2,
    constraint fk_l_45_e_3
        foreign key(fk_e_3)
        references e_3.pk_e_3
);

alter table e_0
    add constraint fk_e0_l_45
        foreign key(fk_l_45)
        references l_4_5.pk_l_4_5;

-- vim: ft=mysql
