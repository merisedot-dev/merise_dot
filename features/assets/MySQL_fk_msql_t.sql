alter table msql_t
    constraint MySQL_test_fk
        foreign key(truc)
        references t2.pk_trg
