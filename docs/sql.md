# SQL conversion

Once you get a functionning MLD graph, you may want to turn this into a SQL database script. This is where the SQL conversion function enters the fray.

## Pre-requisites

As of now, this feature isn't available, but is planned for a future release. This section aims to be a rundown of what is to come, once the implementation of `merise_gtk` will have reached a self-sufficient stage (meaning mostly MCD usage).

## Conversion kernels

SQL has... A lot of variants. To account for all of those, an interface will be provided, by the name of `merise_dot.sql.SQLKernel`. This interface will be useful since your conversion utility (`merise_dot.sql.Script`) will take one to ensure the conversion. Converting your MLD graph should look something like this, assuming the MLD graph is already created :

```py
md_script = Script()
md_script.convert(MSQLCore())
with open('/tmp/test') as file:
    md_script.write(file)
```

In case of wrongful conversion, the call to `md_script.write` will throw an exception. Sames goes with `md_script.convert`, which means unless you're a madman, you will have an exception to handle before you can call `md_script.write`. Keep in mind this will also reset the already written parts of the script to `None`.

After conversion, the script is meant to be used via a tool like [PhPMyAdmin] or any other SQL shell-like tool which can execute said script.

## Output script

The SQL output script is meant to initialize an empty database, therefore without any data in there, so it can't be used as a all-in-one solution (unless some work is done).

Any generated script, with any Conversion kernel given with `merise_dot` (we won't care if you're using your own) will have the following elements :

- database name (the graph's name)
- table definitions (based on MLD entities)
- primary and foreign key constraints
- nullable and non-nullable fields
- link tables for ternaries

The specifics then may vary depending on which Conversion kernel you used. As of now, only these ones are planned, more on their use later down the page :

- MySQL
- PostgreSQL
