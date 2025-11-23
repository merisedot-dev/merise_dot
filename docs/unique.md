# Unique constraints

The second main constraint type we rely on in SQL variants is the *Unique* constraint. As a reminder, this constraint is made to ensure we do not have more than one copy of a key (or a key tuple) in a given table. The important detail is, it often presents itself as following :

```sql
alter table t
    add constraint unq_test
        unique(truc, bidule);
```

Following this logic, using such a constraint with `merise_dot` should look something like this, provided the table `t` and some keys are already created (please look at [SQL Tables](sql_tables.md) if you need to know how to make some) :

```py
# constraint definition
cst = UniqueConstraint("unq_test")
cst.add_field(t.get_field("truc"))
cst.add_field(t.get_field("bidule"))

# script conversion
cst_script = str(cst)
```
