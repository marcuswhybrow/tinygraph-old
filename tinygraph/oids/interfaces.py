from oids.oid_node import OidNode

# IF-MIB::ifNumber
#
# The number of network interfaces (regardless of their
# current state) present on this system.
ifNumber = OidNode('1.3.6.1.2.1.2.1', 'ifNumber')

# ----------------------------------------------------------

ifTable = OidNode('1.3.6.1.2.1.2.2', 'ifTable')
ifTable.addChildren([
    OidNode('1', 'ifEntry')
])

ifTable['ifEntry'].addChildren([
    # IF-MIB::ifIndex
    #
    # A unique value, greater than zero, for each interface. It
    # is recommended that values are assigned contiguously
    # starting from 1. The value for each interface sub-layer
    # must remain constant at least from one re-initialization of
    # the entity's network management system to the next re-
    # initialization.
    OidNode('1', 'ifIndex'),

    # IF-MIB::ifDescr
    #
    # A textual string containing information about the
    # interface. This string should include the name of the
    # manufacturer, the product name and the version of the
    # interface hardware/software.
    #
    # NOTE: usualy something like "eth0"
    OidNode('2', 'ifDescr'),

    # IF-MIB::ifType
    #
    # The type of interface. Additional values for ifType are
    # assigned by the Internet Assigned Numbers Authority (IANA),
    # through updating the syntax of the IANAifType textual
    # convention.
    #
    # see http://tools.cisco.com/Support/SNMP/do/BrowseOID.do?local=en&translate=Translate&typeName=IANAifType
    # for the full list of types (which are integers)
    OidNode('3', 'ifType'),

    # IF-MIB::ifMtu.
    #
    # The size of the largest packet which can be sent/received
    # on the interface, specified in octets. For interfaces that
    # are used for transmitting network datagrams, this is the
    # size of the largest network datagram that can be sent on the
    # interface.
    OidNode('4', 'ifMtu'),

    # IF-MIB::ifSpeed
    #
    # An estimate of the interface's current bandwidth in bits
    # per second. For interfaces which do not vary in bandwidth
    # or for those where no accurate estimation can be made, this
    # object should contain the nominal bandwidth. If the
    # bandwidth of the interface is greater than the maximum value
    # reportable by this object then this object should report its
    # maximum value (4,294,967,295) and ifHighSpeed must be used
    # to report the interace's speed. For a sub-layer which has
    # no concept of bandwidth, this object should be zero.
    OidNode('5', 'ifSpeed'),

    # IF-MIB::ifPhysAddress
    #
    # The interface's address at its protocol sub-layer. For
    # example, for an 802.x interface, this object normally
    # contains a MAC address. The interface's media-specific MIB
    # must define the bit and byte ordering and the format of the
    # value of this object. For interfaces which do not have such
    # an address (e.g., a serial line), this object should contain
    # an octet string of zero length
    OidNode('6', 'ifPhysAddress'),

    # IF-MIB::ifAdminStatus
    #
    # The desired state of the interface. The testing(3) state
    # indicates that no operational packets can be passed. When a
    # managed system initializes, all interfaces start with
    # ifAdminStatus in the down(2) state. As a result of either
    # explicit management action or per configuration information
    # retained by the managed system, ifAdminStatus is then
    # changed to either the up(1) or testing(3) states (or remains
    # in the down(2) state).
    OidNode('7', 'ifAdminStatus'),

    # IF-MIB::ifOperStatus
    #
    # The current operational state of the interface. The
    # testing(3) state indicates that no operational packets can
    # be passed. If ifAdminStatus is down(2) then ifOperStatus
    # should be down(2). If ifAdminStatus is changed to up(1)
    # then ifOperStatus should change to up(1) if the interface is
    # ready to transmit and receive network traffic; it should
    # change to dormant(5) if the interface is waiting for
    # external actions (such as a serial line waiting for an
    # incoming connection); it should remain in the down(2) state
    # if and only if there is a fault that prevents it from going
    # to the up(1) state; it should remain in the notPresent(6)
    # state if the interface has missing (typically, hardware)
    # components.
    #
    #     1 : up
    #     2 : down
    #     3 : testing
    #     4 : unknown
    #     5 : dormant
    #     6 : notPresent
    #     7 : lowerLayerDown
    OidNode('8', 'ifOperStatus'),

    # IF-MIB::ifLastChange
    #
    # The value of sysUpTime at the time the interface entered
    # its current operational state. If the current state was
    # entered prior to the last re-initialization of the local
    # network management subsystem, then this object contains a
    # zero value.
    OidNode('9', 'ifLastChange'),

    # ----------------------------------------------------------

    # IF-MIB::ifInOctets
    #
    # The total number of octets received on the interface,
    # including framing characters.
    OidNode('10', 'ifInOctets'),

    # IF-MIB::ifInUcastPkts
    #
    # The number of packets, delivered by this sub-layer to a
    # higher (sub-)layer, which were not addressed to a multicast
    # or broadcast address at this sub-layer.
    OidNode('11', 'ifInUcastPkts'),

    # IF-MIB::ifInNUcastPkts
    #
    # The number of packets, delivered by this sub-layer to a
    # higher (sub-)layer, which were addressed to a multicast or
    # broadcast address at this sub-layer.
    OidNode('12', 'ifInNUcastPkts'),

    # IF-MIB::ifInDiscards
    #
    # The number of inbound packets which were chosen to be
    # discarded even though no errors had been detected to prevent
    # their being deliverable to a higher-layer protocol. One
    # possible reason for discarding such a packet could be to
    # free up buffer space.
    OidNode('13', 'ifInDiscards'),

    # IF-MIB::ifInErrors
    #
    # For packet-oriented interfaces, the number of inbound
    # packets that contained errors preventing them from being
    # deliverable to a higher-layer protocol. For character-
    # oriented or fixed-length interfaces, the number of inbound
    # transmission units that contained errors preventing them
    # from being deliverable to a higher-layer protocol.
    OidNode('14', 'ifInErrors'),

    # IF-MIB::ifInUnknownProtos
    #
    # For packet-oriented interfaces, the number of packets
    # received via the interface which were discarded because of
    # an unknown or unsupported protocol. For character-oriented
    # or fixed-length interfaces that support protocol
    # multiplexing the number of transmission units received via
    # the interface which were discarded because of an unknown or
    # unsupported protocol. For any interface that does not
    # support protocol multiplexing, this counter will always be
    # 0
    OidNode('15', 'ifInUnknownProtos'),

    # ----------------------------------------------------------

    # IF-MIB::ifOutOctets
    #
    # The total number of octets transmitted out of the
    # interface, including framing characters.
    OidNode('16', 'ifOutOctets'),

    # IF-MIB::ifOutUcastPkts
    #
    # The number of packets, delivered by this sub-layer to a
    # higher (sub-)layer, which were not addressed to a multicast
    # or broadcast address at this sub-layer.
    OidNode('17', 'ifOutUcastPkts'),

    # IF-MIB::ifOutNUcastPkts
    #
    # The total number of packets that higher-level protocols
    # requested be transmitted, and which were addressed to a
    # multicast or broadcast address at this sub-layer, including
    # those that were discarded or not sent.
    OidNode('18', 'ifOutNUcastPkts'),

    # IF-MIB::ifOutDiscards
    #
    # The number of outbound packets which were chosen to be
    # discarded even though no errors had been detected to prevent
    # their being transmitted. One possible reason for discarding
    # such a packet could be to free up buffer space
    OidNode('19', 'ifOutDiscards'),

    # IF-MIB::ifOutErrors
    #
    # For packet-oriented interfaces, the number of outbound
    # packets that could not be transmitted because of errors.
    # For character-oriented or fixed-length interfaces, the
    # number of outbound transmission units that could not be
    # transmitted because of errors.
    OidNode('20', 'ifOutErrors'),

    # IF-MIB::ifOutQLen
    #
    # The length of the output packet queue (in packets).
    OidNode('21', 'ifOutQLen'),
    
    # ----------------------------------------------------------
    
    OidNode('22', 'ifSecific'),
])