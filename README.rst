=========
TinyGraph
=========

This is the home of some experimentally initial code for the dissertation of `Marcus Whybrow <http://marcuswhybrow.net/>`_. The goal is to create a highly guided (by which is meant simple to use) SNMP based tool for monitoring networks. Despite being simple to get working, it should also not be limiting to users who know what a MIB is and want to delve in and start monitoring bespoke SNMP data.

The following goals are on the roadmap, and are listed in order of probable implementation:

* Overview dashboard for real-time stats such as CPU, memory, storage space etc. of all machines on the network
* Time series data of all monitored values should be stored in the database, and be viewable as beautiful graphs.
* A higher level of visualisation (along the lines of `Network Weathermap <http://www.network-weathermap.com/gallery>`_) such that data becomes meaningful and comprehendible at a glance.