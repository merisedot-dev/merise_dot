alter table msql_t
    add constraint MySQL_test_fk
        foreign key(truc)
        references trg.pk_trg;
