from oids.oid_node import OidNode

# HOST_RESOURCES-MIB::hrStorageTable
#
# The (conceptual) table of logical storage areas on
# the host.
# 
# An entry shall be placed in the storage table for each
# logical area of storage that is allocated and has
# fixed resource limits. The amount of storage
# represented in an entity is the amount actually usable
# by the requesting entity, and excludes loss due to
# formatting or file system reference information.
# 
# These entries are associated with logical storage
# areas, as might be seen by an application, rather than
# physical storage entities which are typically seen by
# an operating system. Storage such as tapes and
# floppies without file systems on them are typically
# not allocated in chunks by the operating system to
# requesting applications, and therefore shouldn't
# appear in this table. Examples of valid storage for
# this table include disk partitions, file systems, ram
# (for some architectures this is further segmented into
# regular memory, extended memory, and so on), backing
# store for virtual memory (`swap space').
# 
# This table is intended to be a useful diagnostic for
# `out of memory' and `out of buffers' types of
# failures. In addition, it can be a useful performance
# monitoring tool for tracking memory, disk, or buffer
# usage.
hrStorageTable = OidNode('1.3.6.1.2.1.25.2.3', 'hrStorageTable')
hrStorageTable.addChildren([
    OidNode('1', 'hrStorageEntry'),
])

hrStorageTable['hrStorageEntry'].addChildren([
    # The type of storage represented by this entry.
    OidNode('2', 'hrStorageType'),
    
    # A description of the type and instance of the storage
    # described by this entry
    OidNode('3', 'hrStorageDescr'),
    
    # The size, in bytes, of the data objects allocated
    # from this pool. If this entry is monitoring sectors,
    # blocks, buffers, or packets, for example, this number
    # will commonly be greater than one. Otherwise this
    # number will typically be one.
    OidNode('4', 'hrStorageAllocationUnits'),
    
    # The size of the storage represented by this entry, in
    # units of hrStorageAllocationUnits. This object is
    # writable to allow remote configuration of the size of
    # the storage area in those cases where such an
    # operation makes sense and is possible on the
    # underlying system. For example, the amount of main
    # memory allocated to a buffer pool might be modified or
    # the amount of disk space allocated to virtual memory
    # might be modified.
    OidNode('5', 'hrStorageSize'),
    
    # The amount of the storage represented by this entry
    # that is allocated, in units of
    # hrStorageAllocationUnits.
    OidNode('6', 'hrStorageUsed'),
])


hrStorageTypes = OidNode('1.3.6.1.2.1.25.2.1', 'hrStorageTypes')
hrStorageTypes.addChildren([
    OidNode('1', 'hrStorageOther'),
    OidNode('2', 'hrStorageRam'),
    OidNode('3', 'hrStorageVirtualMemory'),
    OidNode('4', 'hrStorageFixedDisk'),
    OidNode('5', 'hrStorageRemovableDisk'),
    OidNode('6', 'hrStorageFloppyDisk'),
    OidNode('7', 'hrStorageCompactDisk'),
    OidNode('8', 'hrStorageRamDisk'),
    OidNode('9', 'hrStorageFlashMemory'),
    OidNode('10', 'hrStorageNetworkDisk'),
])



hrDeviceTable = OidNode('1.3.6.1.2.1.25.3.2', 'hrDeviceTable')
hrDeviceTable.addChildren([
    OidNode('1', 'hrDeviceEntry')
])
hrDeviceTable['hrDeviceEntry'].addChildren([
    OidNode('1', 'hrDeviceIndex'),
    OidNode('2', 'hrDeviceType'),
    OidNode('3', 'hrDeviceDescr'),
    OidNode('4', 'hrDeviceID'),
    OidNode('5', 'hrDeviceStatus'),
    OidNode('6', 'hrDeviceErrors'),
])

# The (conceptual) table of processors contained by the
# host.
# 
# Note that this table is potentially sparse: a
# (conceptual) entry exists only if the correspondent
# value of the hrDeviceType object is
# `hrDeviceProcessor'.
hrProcessorTable = OidNode('1.3.6.1.2.1.25.3.3', 'hrProcessorTable')
hrProcessorTable.addChildren([
    # A (conceptual) entry for one processor contained by
    # the host. The hrDeviceIndex in the index represents
    # the entry in the hrDeviceTable that corresponds to the
    # hrProcessorEntry.
    # 
    # As an example of how objects in this table are named,
    # an instance of the hrProcessorFrwID object might be
    # named hrProcessorFrwID.3
    OidNode('1', 'hrProcessorEntry')
])
hrProcessorTable['hrProcessorEntry'].addChildren([
    # The product ID of the firmware associated with the
    # processor
    OidNode('1', 'hrProcessorFrwID'),
    
    # The average, over the last minute, of the percentage
    # of time that this processor was not idle.
    # Implementations may approximate this one minute
    # smoothing period if necessary
    OidNode('2', 'hrProcessorLoad'),
])

hrDeviceTypes = OidNode('1.3.6.1.2.1.25.3.1', 'hrDeviceTypes')
hrDeviceTypes.addChildren([
    OidNode('1', 'hrDeviceOther'),
    OidNode('2', 'hrDeviceUnknown'),
    OidNode('3', 'hrDeviceProcessor'),
    OidNode('4', 'hrDeviceNetwork'),
    OidNode('5', 'hrDevicePrinter'),
    OidNode('6', 'hrDeviceDiskStorage'),
    OidNode('10', 'hrDeviceVideo'),
    OidNode('11', 'hrDeviceAudio'),
    OidNode('12', 'hrDeviceCoprocessor'),
    OidNode('13', 'hrDeviceKeyboard'),
    OidNode('14', 'hrDeviceModem'),
    OidNode('15', 'hrDeviceParallelPort'),
    OidNode('16', 'hrDevicePointing'),
    OidNode('17', 'hrDeviceSerialPort'),
    OidNode('18', 'hrDeviceTape'),
    OidNode('19', 'hrDeviceClock'),
    OidNode('20', 'hrDeviceVolatileMemory'),
    OidNode('21', 'hrDeviceNonVolatileMemory'),
])

# The (conceptual) table of file systems local to this
# host or remotely mounted from a file server. File
# systems that are in only one user's environment on a
# multi-user system will not be included in this table.
hrFSTable = OidNode('1.3.6.1.2.1.25.3.8', 'hrFSTable')
hrFSTable.addChildren([
    # A (conceptual) entry for one file system local to
    # this host or remotely mounted from a file server.
    # File systems that are in only one user's environment
    # on a multi-user system will not be included in this
    # table.
    # 
    # As an example of how objects in this table are named,
    # an instance of the hrFSMountPoint object might be
    # named hrFSMountPoint.3
    OidNode('1', 'hrFSEntry')
])

hrFSTable['hrFSEntry'].addChildren([
    # A unique value for each file system local to this
    # host. The value for each file system must remain
    # constant at least from one re-initialization of the
    # agent to the next re-initialization.
    OidNode('1', 'hrFSIndex'),
    
    # The path name of the root of this file system.
    OidNode('2', 'hrFSMountPoint'),
    
    # A description of the name and/or address of the
    # server that this file system is mounted from. This
    # may also include parameters such as the mount point on
    # the remote file system. If this is not a remote file
    # system, this string should have a length of zero.
    OidNode('3', 'hrFSRemoteMountPoint'),
    
    # The value of this object identifies the type of this
    # file system
    OidNode('4', 'hrFSType'),
    
    # An indication if this file system is logically
    # configured by the operating system to be readable and
    # writable or only readable. This does not represent
    # any local access-control policy, except one that is
    # applied to the file system as a whole.
    #
    #     1 : readWrite
    #     2 : readOnly
    #
    OidNode('5', 'hrFSAccess'),
    
    # A flag indicating whether this file system is
    # bootable.
    #
    #     1 : true
    #     2 : false
    #
    OidNode('6', 'hrFSBootable'),
    
    # The index of the hrStorageEntry that represents
    # information about this file system. If there is no
    # such information available, then this value shall be
    # zero. The relevant storage entry will be useful in
    # tracking the percent usage of this file system and
    # diagnosing errors that may occur when it runs out of
    # space
    #
    #     range: 0 - 2147483647
    #
    OidNode('7', 'hrFSStorageIndex'),
    
    # The last date at which this complete file system was
    # copied to another storage device for backup. This
    # information is useful for ensuring that backups are
    # being performed regularly.
    # 
    # If this information is not known, then this variable
    # shall have the value corresponding to January 1, year
    # 0000, 00:00:00.0, which is encoded as
    # (hex)'00 00 01 01 00 00 00 00'.
    OidNode('8', 'hrFSLastFullBackupDate'),
    
    # The last date at which a portion of this file system
    # was copied to another storage device for backup. This
    # information is useful for ensuring that backups are
    # being performed regularly.
    # 
    # If this information is not known, then this variable
    # shall have the value corresponding to January 1, year
    # 0000, 00:00:00.0, which is encoded as
    # (hex)'00 00 01 01 00 00 00 00'.
    OidNode('9', 'hrFSLastPartialBackupDate'),
])

hrFSTypes = OidNode('1.3.6.1.2.1.25.3.9', 'hrFSTypes')
hrFSTypes.addChildren([
    OidNode('1', 'hrFSOther'),
    OidNode('2', 'hrFSUnknown'),
    OidNode('3', 'hrFSBerkeleyFFS'),
    OidNode('4', 'hrFSSys5FS'),
    OidNode('5', 'hrFSFat'),
    OidNode('6', 'hrFSHPFS'),
    OidNode('7', 'hrFSHFS'),
    OidNode('8', 'hrFSMFS'),
    OidNode('9', 'hrFSNTFS'),
    OidNode('10', 'hrFSVNode'),
    OidNode('11', 'hrFSJournaled'),
    OidNode('12', 'hrFSiso9660'),
    OidNode('13', 'hrFSRockRidge'),
    OidNode('14', 'hrFSNFS'),
    OidNode('15', 'hrFSNetware'),
    OidNode('16', 'hrFSAFS'),
    OidNode('17', 'hrFSDFS'),
    OidNode('18', 'hrFSAppleshare'),
    OidNode('19', 'hrFSRFS'),
    OidNode('20', 'hrFSDGCFS'),
    OidNode('21', 'hrFSBFS'),
    OidNode('22', 'hrFSFAT32'),
    OidNode('23', 'hrFSLinuxExt2'),
])