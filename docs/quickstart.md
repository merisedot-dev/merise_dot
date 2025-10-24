# Getting started

In this section, we'll assume you're working using a `pyproject.toml` file for build purposes (`requirements.txt` still exists but we won't cover it).

## Adding `merise_dot` to your project

To add the library to your project, please add the following to your `pyproject.toml` :

```toml
dependencies = [ "merise_dot" ]
```

If you're using devshells, please refer to one of the following sections for the following devshell tool you're using. As of now, only the following have been tested, so they are the only one being talked about here.

### Nix

Add the following to your `flake.nix` :

```
inputs.merise_dot.url = "github:merisedot-dev/merise_dot";

outputs = {
    devShells.default = pkgs.mkShell {
        name = "myshell";
        packages = [ merise_dot ];
    };
};
```

## Simple graph

Now that you've added `merise_dot` to your project, you'll need to create an MCD graph to start working. To speak the truth, most of the work you'll do will pass through the `Graph` class. This would look something like this :

```py
graph = Graph('mygraph')
```

Once your graph is created, you'll want to add in some entity and links. Keep in mind links will require an entity to even be created, while entities can exist in standalone. Let's turn the `graph` in a simple enough MCD graph :

```py
ent1 = graph.add_entity('ent1')
ent1.add_field('pk_e1', 'int', True)
ent1.add_field('test', 'boolean', False)
ent1.add_field('testtest', 'varchar(10)')

ent2 = graph.add_entity('ent2')
ent2.add_field('pk_e2', 'int', True)
```

## Rendering

Once you build your graph how you wanted, you may want to render the graph to visualize your MCD. This can easily be done via the following instructions :

```py
mcdb = MCDBuilder()
mcdb.mk_graph(graph)
mcdb.build('/tmp/test.gr') # please see extra sections
```
