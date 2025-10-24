# MCD manipulation

MCDs are the bulk of the *merise* method and this doesn't change in `merise_dot`. This means most of the work you'll be doing using this library will require a MCD graph. Such graph can be created using the `merise_dot.model.Graph` class provided as well as its inner types. Remember, a MCD graph can be created using the following instruction :

```py
my_mcd: Graph = Graph('my_mcd')
```

The name of the graph will also determine the name of the file to write it to (in `$PWD` limits), so it needs to be filled in.

## Entities behavior

Entities's definition is pretty simple, anyone who ever did a class diagram will recognize it pretty fast. However, it is discouraged to create them yourself, instead, you should use the provided graph method, like the code that follows :

```py
my_ent: Entity = graph.add_entity('my_ent')
```

Provided you created a graph first. Names in MCD graph will always be lowercased and act as identifiers for Entites and fields, so do not try to edit these manually ! In a similar fashion, entity fetching and entity deletion should be handled only with the provided methods, `graph.get_entity` and `graph.del_entity`.

### Fields

Entities are meant to be descriptors of data, which implies it needs to describe how the data is stored in them. This is where fields come in, like in *merise* or in a class diagram. Field creation should be using one of the following instructions :

```py
# for a regular field
my_ent.add_field('test', 'int', False)
# for a primary key
my_ent.add_field('pk_e1', 'int', True)
# types can change
my_ent.add_field('testing', 'varchar(64)', False)
```

As of now, all fields (except for *PKs*) will be considered *nullable*. This may be an issue in development afterwards if not prepared, so keep that in mind. As of now, due to the absence of any SQL converters, field types are not thoroughly checked. By default, no field is a primary key, which allows for this kind of field creation :

```py
my_ent.add_field('testopommes', 'int')
```

Once a field is created, editing a field will only mean changing one of two things :

- its primary key status (from `True` to `False` or the opposite)
- the field's type

This kind of operation can be performed via the `edit_field` method, provided by the `merise_dot.model.mcd.Entity` class, like this :

```py
graph = Graph('test')
ent = graph.add_entity('test')
ent.add_field('pk_t', 'int')
ent.edit_field('pk_t', prim=True) # we change the primary key status
ent.edit_field('pk_t', f_type='short') # we change the type of the field
```

And finally, the `entity.del_field` method is here to allow field deletion, thus helping with removing useless data descriptions. Please note that, as all methods discussed so far, they will raise an exception in case of aberrant parameters, depending on the following rules :

#### Graph methods

method              |reason for exception
--------------------|-------------------------------------------
`Graph.add_entity`  |the entity exists and can't be overwritten
`Graph.get_entity`  |the entity doesn't exist
`Graph.del_entity`  |the entity doesn't exist

#### Entity methods

method              |reason for exception
--------------------|--------------------------------------------------
`Entity.add_field`  |the field exists and can't be overwritten
`Entity.edit_field` |the field doesn't exist or no change was requested
`Entity.del_field`  |the field doesn't exist


## Links behavior

Links are the other part of the MCD graph manipulation. Unlike Entities, they can't be created in a standalone fashion, which ends up in code like this :

```py
graph = Graph('test')
ent_1 = graph.add_entity('truc')
ent_2 = graph.add_entity('jaaj')
# link creation
graph.add_link('lk', ent_1._name, ent_2._name)
```

### Inner fields

A Link entity in an MCD graph will need to have its own data stored sometimes, which means inner Link fields. As for Entites fields, you'll need to create them via provided methods, like this :

```py
lk = graph.get_link('lk')
lk.add_field('test', 'int')
```

Again, the field's name will be lowercased and will act as an ID for said field. This is made to avoid duplication in the fields and make parsing easier when handling conversions. Unlike what Entities are equipped with, these fields only have the information of their type and their name. In case the field's type should change, please use the following method :

```py
lk.edit_field('test', 'varchar(30)')
```

### Link cardinalities

The entire point of Links is to be... Well... Linked to more classical entities. This means cardinalities on the link node. Cardinality usage should look something like this :

```py
ent_3 = graph.add_entity('machin')
lk.add_card(ent_3, 0, -1) # for a n cardinality
lk.del_card(ent_3)
lk.add_card(ent_3, 0, 1) # for a 1 cardinality
```

A link can have one and only one cardinality on a given Entity. This will be used in two ways :

- during conversion, it will be used to determine the name of a foreign key and where it goes
- during rendering, it will be used to know what to display as a name

## Rendering

For [graphviz] enjoyers, a `MCDBuilder.render(path)` method was added to the library. This will not create the file to dump the graph in, but it will write a complete dotgraph *and* create a `.png` file next to it, containing an image of the rendered graph. Please ignore some... Questionable line placement, thanks [graphviz].

[graphviz]: https://graphviz.org/
