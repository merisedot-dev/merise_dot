-- Generated with merise_dot

drop database mgraph;

create database mgraph;

create table e_0 (
    pk_e_o int primary key not null
);

create table e_1 (
    pk_e_1 int primary key not null
);

create table e_2 (
    pk_e_2 int primary key not null
);

create table e_3 (
    pk_e_3 int primary key not null
);

create table e_4 (
    pk_e_4 int primary key not null
);

alter table e_1
    add column fk_e2 int;

alter table e_1
    add constraint fk_e_1_e_2
        foreign key(fk_e2)
        references e_2.pk_e_2;

alter table e_2
    add column fk_e1 int not null;

alter table e_2
    add constraint fk_e_2_e_1
        foreign key(fk_e1)
        references e_1.pk_e_1;

-- vim: ft=mysql
