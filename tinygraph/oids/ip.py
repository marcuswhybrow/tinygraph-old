from oids.oid_node import OidNode

ipAddrTable = OidNode('1.3.6.1.2.1.4.20', 'ipAddrTable')
ipAddrTable.addChildren([
    OidNode('1', 'ipAddrEntry')
])

ipAddrTable['ipAddrEntry'].addChildren([
    # IP-MIB::ipAdEntAddr
    #
    # The IPv4 address to which this entry's addressing
    # information pertains.
    OidNode('1', 'ipAdEntAddr'),

    # IP-MIB::ipAdEntIfIndex
    #
    # The index value which uniquely identifies the interface to
    # which this entry is applicable. The interface identified by
    # a particular value of this index is the same interface as
    # identified by the same value of the IF-MIB's ifIndex.
    OidNode('2', 'ipAdEntIfIndex'),

    # IP-MIB::ipAdEntNetMask
    #
    # The subnet mask associated with the IPv4 address of this
    # entry. The value of the mask is an IPv4 address with all
    # the network bits set to 1 and all the hosts bits set to 0.
    OidNode('3', 'ipAdEntNetMask'),

    # IP-MIB::ipAdEntBcastAddr
    #
    # The value of the least-significant bit in the IPv4 broadcast
    # address used for sending datagrams on the (logical)
    # interface associated with the IPv4 address of this entry.
    # For example, when the Internet standard all-ones broadcast
    # address is used, the value will be 1. This value applies to
    # both the subnet and network broadcast addresses used by the
    # entity on this (logical) interface
    OidNode('4', 'ipAdEntBcastAddr'),

    # IP-MIB::ipAdEntReasmMaxSize
    #
    # The size of the largest IPv4 datagram which this entity can
    # re-assemble from incoming IPv4 fragmented datagrams received
    # on this interface.
    OidNode('5', 'ipAdEntReasmMaxSize'),
])

ipNetToMediaTable = OidNode('1.3.6.1.2.1.4.22', 'ipNetToMediaTable')
ipNetToMediaTable.addChildren([
    OidNode('1', 'ipNetToMediaEntry')
])

ipNetToMediaTable['ipNetToMediaEntry'].addChildren([
    OidNode('1', 'ipNetToMediaIfIndex'),
    OidNode('2', 'ipNetToMediaPhysAddress'),
    OidNode('3', 'ipNetToMediaNetAddress'),
    OidNode('4', 'ipNetToMediaType'),
])