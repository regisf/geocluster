GeoCluster library
==================

GeoCluster is a Python library to regroup item on a map. This library is designed to be fast not accurate.
This library is framework and database agnostic.


Installation
------------

* using Git : In your project tree, open a shell or a console and type 
`git clone https://github.com/regisf/geocluster.git geocluster` GeoCluster is now ready do use 
* using easy_install
* using pip
* unzig zip

Using it
--------

GeoCluster is designed to be as simple as possible. There's only few API to know. 

### Import geocluster

There's only one object to handle : GeoCluster. So to use GeoCluster library just add on the top of your Python
file 

```python
from geocluster import GeoCluster
```

### Create a GeoCluster object

```python
cluster = GeoCluster()
```

### Setup the GeoCluster object

You have to setup the cluster bounds and the size of the computation grid.
 
```python
# North, west, south and east are arbitrary
cluster.set_bounds(north, west, south, east))
cluster.set_grid(15, 15)
```

### Populate the cluster

```python
# Data come from the database
data = [{'lat': d.lattitude, 'lng': d.longitude} for d in get_my_data()]
cluster.populate(data)
```

Know bug
--------

When a bound is cross by the Longitude 0 (such as Greenwich meridian) the computation is completly wrong.

To resolve this bug:

* Help me and submit a Pull Request
* Don't help me and adapt your code with a delta

