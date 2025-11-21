# Foreign keys management

Foreign keys are an integral part of any SQL database and therefore are their own beasts when it comes to constraints. Each one of these must have the following components

## Constraint creation

As for any constraint creation, you're meant to use something like the following script :

```py
cstr: ForeignKeyConstraint = ForeignKeyConstraint("fk_test")
```

Once created, such constraint will need to be handled via either its own methods, or via the `Constraint` parent class provided methods. This should look something like this :

```py
cstr.set_table("test") # parent method

cstr.points_to("truc").on_field("t2")
cstr.origin("machin")
```

These methods will allow the user to build a satisfying foreign key constraint, but only a call to the `__str__` method will turn it into a script.
