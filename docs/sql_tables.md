# SQL tables

The heart of any SQL database, a table will be used only to hold informations and some very basic constraints, such as `primary key` or `unique` constraints. Due to their rather universal structure (outside of the NoSQL world), specialised tables should not be necessary, except for some specific cases down the road. Tables usually use the same syntax everywhere.

These will mostly be created using a conversion tool such as the `Script` class, but there is options to make one yourself. Creating a table requires a name to use, it will act as its id. This will look like the following code :

```py
tab = SQLTable("test")
```

## Fields

Once created, a `SQLTable` is meant to be used as an information descriptor. Therefore, some semantic checks are in order to ensure there will be no messing up with these. These checks will be handled via the `TableField` class (which can be imported the same way you import `SQLTable`), while you create the fields. This will also be used to format fields so tables won't have to it themselves.

Creating a SQL field should look something like this :

```py
field = TableField("tf", TableFieldType.INTEGER)
f2 = TableField("tf2", TableFieldType.BOOLEAN)
f3 = TableField("tf3", TableFieldType.UUID)
```

In most cases, you may want to hide this step behind your conversion kernel or anything keeping track of your database's available types to avoid slotting in an unkown type (for instance, `TableFieldType.UUID` in a script dedicated to SQLite). This is only to avoid errors down the road.
