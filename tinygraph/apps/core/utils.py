# from pysnmp.smi import builder, view, error
# 
# def list_mibs():
#     
#     mibBuilder = builder.MibBuilder().loadModules(
#         'SNMPv2-MIB', 'SNMP-FRAMEWORK-MIB', 'SNMP-COMMUNITY-MIB'
#     )
#     mibView = view.MibViewController(mibBuilder)
#     
#     oid, label, suffix = mibView.getFirstNodeName()
#     while True:
#         try:
#             modName, nodeDesc, suffix = mibView.getNodeLocation(oid)
#             print '%s::%s == %s' % (modName, nodeDesc, oid)
#             oid, label, suffix = mibView.getNextNodeName(oid)
#         except error.NoSuchObjectError:
#             break

from pysnmp.entity.rfc3413.oneliner import cmdgen

def byteToHex(byteStr):
    """
    Convert a byte string to it's hex string representation e.g. for output.
    """
    return ' '.join(['%02X' % ord(x) for x in byteStr])

def get(host, community, oidNode, bulk=False, number_to_get=1, oids=None, values={}, converters={}):
    
    args = [
        cmdgen.CommunityData('test-agent', community),
        cmdgen.UdpTransportTarget((host, 161)),
    ]
    if bulk:
        args.append(0)
        args.append(number_to_get)
        klass = cmdgen.CommandGenerator().bulkCmd
    else:
        klass = cmdgen.CommandGenerator().getCmd
        
    args.append(
        tuple(map(int, str(oidNode).split('.')))
    )
    
    errorIndication, errorStatus, errorIndex, varBinds = klass(*args)

    if errorIndication:
        raise Exception(errorIndication)
    else:
        if errorStatus:
            raise Exception('%s at %s\n' % (
                errorStatus.prettyPrint(), varBinds[int(errorIndex)-1]
            ))
        else:
            if bulk:
                data = {}
                if oids is not None:
                    for target_oid_name in oids:
                        for row in varBinds:
                            oid = row[0][0].prettyPrint()
                            val = row[0][1].prettyPrint()
                            
                            # If more readable replacement values have been
                            # specified for this value, then replace them.
                            if target_oid_name in values:
                                for nodeName, node in values[target_oid_name].getChildren().items():
                                    if val == node.absolute_oid():
                                        val = nodeName
                                        break
                            
                            if target_oid_name in converters:
                                val = converters[target_oid_name](val)
                            
                            targetOidNode = oidNode[target_oid_name]
                            left = '%s.' % targetOidNode
                            if oid.startswith(left):
                                index = oid[len(left):]
                                try:
                                    data[index][target_oid_name] = val
                                except KeyError:
                                    data[index] = {target_oid_name: val}
                else:
                    for row in varBinds:
                        data[row[0][0].prettyPrint()] = row[0][1].prettyPrint()
                return data
            else:
                return varBinds[0][1].prettyPrint()

import oids

def get_details(host, community):
    # ip = get(host, oids.ip.ADDRESS_TABLE, bulk=True)
    
    return {
        'system_description': get(host, community,         '1.3.6.1.2.1.1.1.0'),
        'host_name': get(host, community,                  '1.3.6.1.2.1.1.5.0'),
        'up_time': get(host, community,                '1.3.6.1.2.1.1.3.0'),
        'number_of_interfaces': get(host, community,   '1.3.6.1.2.1.2.1.0'),
        'number_of_users': get(host, community,        '1.3.6.1.2.1.25.1.5.0'),
        'processes': get(host, community,              '1.3.6.1.2.1.25.1.6.0'),
        'memory': str(int(get(host, community,                 '1.3.6.1.2.1.25.2.2.0')) * 1024),
        'storage': get(host, community, oids.host_resources.hrStorageTable['hrStorageEntry'], bulk=True, oids=[
            'hrStorageType',
            'hrStorageDescr',
            'hrStorageAllocationUnits',
            'hrStorageSize',
            'hrStorageUsed',
        ], values={
            'hrStorageType': oids.host_resources.hrStorageTypes,
        }),
        'interfaces': get(host, community, oids.interfaces.ifTable['ifEntry'], bulk=True, oids=[
            'ifIndex', 'ifDescr', 'ifType', 'ifMtu', 'ifSpeed', 'ifPhysAddress', 'ifAdminStatus', 'ifOperStatus', 'ifLastChange',
            'ifInOctets', 'ifInUcastPkts', 'ifInNUcastPkts', 'ifInDiscards', 'ifInErrors', 'ifInUnknownProtos',
            'ifOutOctets', 'ifOutUcastPkts', 'ifOutNUcastPkts', 'ifOutDiscards', 'ifOutErrors', 'ifOutQLen'
        ], converters={
            'ifPhysAddress': byteToHex,
        }),
        'ip_addresses': get(host, community, oids.ip.ipAddrTable['ipAddrEntry'], bulk=True, oids=[
            'ipAdEntAddr',
            'ipAdEntIfIndex',
            'ipAdEntNetMask',
            'ipAdEntBcastAddr',
            'ipAdEntReasmMaxSize',
        ]),
        'net_to_media': get(host, community, oids.ip.ipNetToMediaTable['ipNetToMediaEntry'], bulk=True, oids=[
            'ipNetToMediaIfIndex',
            'ipNetToMediaPhysAddress',
            'ipNetToMediaNetAddress',
            'ipNetToMediaType',
        ] , converters={
            'ipNetToMediaPhysAddress': byteToHex,
        }),
        'devices': get(host, community, oids.host_resources.hrDeviceTable['hrDeviceEntry'], bulk=True, oids=[
            'hrDeviceIndex',
            'hrDeviceType',
            'hrDeviceDescr',
            'hrDeviceID',
            'hrDeviceStatus',
            'hrDeviceErrors',
        ], values={
            'hrDeviceType': oids.host_resources.hrDeviceTypes,
        }),
        'processors': get(host, community, oids.host_resources.hrProcessorTable['hrProcessorEntry'], bulk=True, oids=[
            'hrProcessorFrwID',
            'hrProcessorLoad',
        ]),
        'partitions': get(host, community, oids.host_resources.hrFSTable['hrFSEntry'], bulk=True, oids=[
            'hrFSIndex',
            'hrFSMountPoint',
            'hrFSRemoteMountPoint',
            'hrFSType',
            'hrFSAccess',
            'hrFSBootable',
            'hrFSStorageIndex',
            'hrFSLastFullBackupDate',
            'hrFSLastPartialBackupDate',
        ], values={
            'hrFSType': oids.host_resources.hrFSTypes,
        }),
    }