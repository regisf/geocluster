GeoCluster library
==================

GeoCluster is a Python library to regroup item on a map in the same way than Google MarkerCluster or AnyCluster.
This library is designed to be fast not accurate. This library is framework and database agnostic.


Installation
------------

* using Git: In your project tree, open a shell or a console and type 
`git clone https://github.com/regisf/geocluster.git geocluster`. Enter into `geocluster` and type
`python setup.py install` to install it. Alternativly you may use the module directly by moving `geocluster`
directory. 

* using easy_install: Open a shell and type `easy_install geocluster`
* using pip: Open a shell and type `pip install geocluster` or `pip install -U geocluster` to update 
* unzig zip: Download the zip package [here][https://github.com/regisf/geocluster/archive/master.zip] 
or [here][https://pypi.python.org/packages/source/g/geocluster/geocluster-1.0.1.zip#md5=acd94b84f2ea3468e5ee593e4760fc00]. 
Unpack it, enter into `geocluster` and type `python setup.py install` to 
install it. Alternativly you may use the module directly by moving `geocluster`
directory. 

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

### Compute and get the data
```Python 
data_clusturized_as_a_dictionnary = cluster.to_json()
```

### Don't clusterize

In some case, the clusterization is not useful. For example when there's a 
important zoom on map. 

You just have to set `GeoCluster.use_clustering` to `False`.

e.g.:

```python
# Use clustering
cluster.use_clustering(True)

# Don't use clustering
cluster.use_clustering(False)
```

### Setting data


### Use the result
`GeoCluster.to_json` send a 2 dimensional array 
(a list of list)

```python
[
	[ col_1, col_2, col_3, col_4 ],  # Row 1
	[ col_1, col_2, col_3, col_4 ],  # Row 2
	[ col_1, col_2, col_3, col_4 ],  # Row 3
	[ col_1, col_2, col_3, col_4 ],  # Row 4
	# ...
]
```

Each cell (here col_1 to col_4) is a dictionnary. If use_clustering isn't set
to True, the cell contains `count` key. If the count key is greater than zero,
it also contains `lat` for lattitude, `lng` for longitude and all other 
provided keys if `count` is equal to one (1). 

```python
[
	[
		{'count': 0},
		# lat 0.0 and lng 0.0 are here for example
		{'count': 1, 'lat': 0.0, 'lng': 0.0, 'extra': 'An example'},
		{'count': 2, 'lat': 0.0, 'lng': 0.0}
	],
	#...
]
```

If `use_clustering` is set to True, there's only one key `points` which 
contains all the points of the bound. 

```python
[
	[
		{'points': [
			{'lat': 0.0, 'lng': 0.0, 'extra': "An example"},
			{'lat': 0.0, 'lng': 0.0, 'other', 'an other example'},
			# ...
		]},
		{'points': [
		#...
		]},
	],
	# ...
]
```

You can't have a mix between `count` and `points` in the same list. Either 
it's a list with `count` keys either its a list with `points`. 


### Set extra data

You can add any kind of data in the dictionnary. They will be set in the 
return result. 

e.g. : 

```python
data = [{
		'lat': d.lattitude,
		'lng': d.longitude,
		'id': d.id,
		'desc': d.description
	} for d in get_my_data()]
cluster.populate(data)
```

`cluster.to_json` will contains the keys `id` and `desc`.


Know bug
--------

When a bound is cross by the Longitude 0 (the Greenwich meridian) the computation is completly wrong.

To resolve this bug:

* Help me and submit a Pull Request
* Don't help me and adapt your code with a delta

