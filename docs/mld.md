# MLD manipulation

Another aspect of the *merise* method is the *MLD* graphs. These are made to be a bridge between direct SQL and an MCD and they will be used here in the same principles. Please keep in mind they are not meant to be used directly when editing.

## MLDBuilder

Enter the `MLDBuilder` class. It provides a structure to turn an [MCD](mcd.md) graph into a MLD graph, provided no aberrations were slotted into the [MCD](mcd.md) graph. Turning an MCD graph this way starts like this :

```py
gr = Graph('trucos')
gr.add_entity('e')

# building the MLD
mld = MLDBuilder()
mld.mk_mld(gr)

# fetching back our built MLD
mld_gr = mld.get()
```

In case of error during MLD building, the `mld_gr` variable will have `None` as a value, so it may cause problems later. During MLD build, any error will raise an exception and set the built graph back to `None`.

Like for [MCD](mcd.md)s, dot graph enjoyers will also find the `MLDBuilder.render(path)` method. It will also not create the required file, but dump the MLD as a `.png` file next to the generated dotgraph.

## Expected usage

Once built, these MLD graphs are mostly meant to be use for displaying purposes, not data manipulation. They are also used as intermediates for SQL conversion (detailed later), but as of now, there is little manipulation prepared for these.

### Entities

The MLD version of an Entity has the classic field behavior, but with a twist : *Foreign Keys* do exist. Creating a new field is done via these instructions :

```py
mld = MLDGraph('test')
mld.add_ent('ent')
ent: MLDEntity = mld.get_ent('ent')
```

Once an `MLDEntity` created and fetched, you can access creation operations in there. However, please keep in mind there is no deletion or edition operations in there since all MLD-related classes are meant to be used as conversion tools. If you really need to add an entity field manually, it should look like this :

```py
ent.add_field('test', 'int', _REGULAR_CODE)
ent.add_field('some', 'varchar(40)', _PK_CODE)
ent.add_field('field', 'boolean', _FK_CODE)
```

The different codes are used to distinguish between the different types of fields an MLD Entity can have. For any further conversion, any entity will need to have either at least one primary or one foreign key to avoid logic problems.

### Links

Links are handled differently in an `MLDGraph` than they are in an `MCDGraph`. In an `MLDGraph`, links are handled mostly through foreign keys, with some cases of extra entities to ensure the existence of link fields and not lose that information. This is also where cardinalities will enter the fray. Depending on what they are, they will determine what type of foreign key will be used and on which entity the key will be placed.
