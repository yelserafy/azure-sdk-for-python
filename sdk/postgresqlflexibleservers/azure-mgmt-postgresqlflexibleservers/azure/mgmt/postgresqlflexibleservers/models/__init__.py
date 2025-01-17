# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ActiveDirectoryAdministrator
from ._models_py3 import ActiveDirectoryAdministratorAdd
from ._models_py3 import AdminCredentials
from ._models_py3 import AdministratorListResult
from ._models_py3 import AuthConfig
from ._models_py3 import Backup
from ._models_py3 import BackupRequestBase
from ._models_py3 import BackupSettings
from ._models_py3 import BackupStoreDetails
from ._models_py3 import CapabilitiesListResult
from ._models_py3 import CapabilityBase
from ._models_py3 import CheckNameAvailabilityRequest
from ._models_py3 import CheckNameAvailabilityResponse
from ._models_py3 import Configuration
from ._models_py3 import ConfigurationForUpdate
from ._models_py3 import ConfigurationListResult
from ._models_py3 import DataEncryption
from ._models_py3 import Database
from ._models_py3 import DatabaseListResult
from ._models_py3 import DbLevelValidationStatus
from ._models_py3 import DbMigrationStatus
from ._models_py3 import DbServerMetadata
from ._models_py3 import DelegatedSubnetUsage
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorResponse
from ._models_py3 import FastProvisioningEditionCapability
from ._models_py3 import FirewallRule
from ._models_py3 import FirewallRuleListResult
from ._models_py3 import FlexibleServerCapability
from ._models_py3 import FlexibleServerEditionCapability
from ._models_py3 import HighAvailability
from ._models_py3 import LogFile
from ._models_py3 import LogFileListResult
from ._models_py3 import LtrBackupRequest
from ._models_py3 import LtrBackupResponse
from ._models_py3 import LtrPreBackupRequest
from ._models_py3 import LtrPreBackupResponse
from ._models_py3 import LtrServerBackupOperation
from ._models_py3 import LtrServerBackupOperationList
from ._models_py3 import MaintenanceWindow
from ._models_py3 import MigrationNameAvailabilityResource
from ._models_py3 import MigrationResource
from ._models_py3 import MigrationResourceForPatch
from ._models_py3 import MigrationResourceListResult
from ._models_py3 import MigrationSecretParameters
from ._models_py3 import MigrationStatus
from ._models_py3 import MigrationSubStateDetails
from ._models_py3 import NameAvailability
from ._models_py3 import Network
from ._models_py3 import Operation
from ._models_py3 import OperationDisplay
from ._models_py3 import OperationListResult
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import ProxyResource
from ._models_py3 import Replica
from ._models_py3 import Resource
from ._models_py3 import RestartParameter
from ._models_py3 import Server
from ._models_py3 import ServerBackup
from ._models_py3 import ServerBackupListResult
from ._models_py3 import ServerForUpdate
from ._models_py3 import ServerListResult
from ._models_py3 import ServerSku
from ._models_py3 import ServerSkuCapability
from ._models_py3 import ServerThreatProtectionListResult
from ._models_py3 import ServerThreatProtectionSettingsModel
from ._models_py3 import ServerVersionCapability
from ._models_py3 import Sku
from ._models_py3 import Storage
from ._models_py3 import StorageEditionCapability
from ._models_py3 import StorageMbCapability
from ._models_py3 import StorageTierCapability
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserAssignedIdentity
from ._models_py3 import UserIdentity
from ._models_py3 import ValidationDetails
from ._models_py3 import ValidationMessage
from ._models_py3 import ValidationSummaryItem
from ._models_py3 import VirtualEndpointResource
from ._models_py3 import VirtualEndpointResourceForPatch
from ._models_py3 import VirtualEndpointsListResult
from ._models_py3 import VirtualNetworkSubnetUsageParameter
from ._models_py3 import VirtualNetworkSubnetUsageResult

from ._postgre_sql_management_client_enums import ActiveDirectoryAuthEnum
from ._postgre_sql_management_client_enums import ArmServerKeyType
from ._postgre_sql_management_client_enums import AzureManagedDiskPerformanceTiers
from ._postgre_sql_management_client_enums import CancelEnum
from ._postgre_sql_management_client_enums import CapabilityStatus
from ._postgre_sql_management_client_enums import CheckNameAvailabilityReason
from ._postgre_sql_management_client_enums import ConfigurationDataType
from ._postgre_sql_management_client_enums import CreateMode
from ._postgre_sql_management_client_enums import CreateModeForUpdate
from ._postgre_sql_management_client_enums import CreatedByType
from ._postgre_sql_management_client_enums import ExecutionStatus
from ._postgre_sql_management_client_enums import FailoverMode
from ._postgre_sql_management_client_enums import FastProvisioningSupportedEnum
from ._postgre_sql_management_client_enums import GeoBackupSupportedEnum
from ._postgre_sql_management_client_enums import GeoRedundantBackupEnum
from ._postgre_sql_management_client_enums import HaMode
from ._postgre_sql_management_client_enums import HighAvailabilityMode
from ._postgre_sql_management_client_enums import IdentityType
from ._postgre_sql_management_client_enums import KeyStatusEnum
from ._postgre_sql_management_client_enums import LogicalReplicationOnSourceDbEnum
from ._postgre_sql_management_client_enums import MigrateRolesEnum
from ._postgre_sql_management_client_enums import MigrationDbState
from ._postgre_sql_management_client_enums import MigrationDetailsLevel
from ._postgre_sql_management_client_enums import MigrationListFilter
from ._postgre_sql_management_client_enums import MigrationMode
from ._postgre_sql_management_client_enums import MigrationNameAvailabilityReason
from ._postgre_sql_management_client_enums import MigrationOption
from ._postgre_sql_management_client_enums import MigrationState
from ._postgre_sql_management_client_enums import MigrationSubState
from ._postgre_sql_management_client_enums import OnlineResizeSupportedEnum
from ._postgre_sql_management_client_enums import OperationOrigin
from ._postgre_sql_management_client_enums import Origin
from ._postgre_sql_management_client_enums import OverwriteDbsInTargetEnum
from ._postgre_sql_management_client_enums import PasswordAuthEnum
from ._postgre_sql_management_client_enums import PrincipalType
from ._postgre_sql_management_client_enums import PrivateEndpointConnectionProvisioningState
from ._postgre_sql_management_client_enums import PrivateEndpointServiceConnectionStatus
from ._postgre_sql_management_client_enums import ReadReplicaPromoteMode
from ._postgre_sql_management_client_enums import ReplicationPromoteOption
from ._postgre_sql_management_client_enums import ReplicationRole
from ._postgre_sql_management_client_enums import ReplicationState
from ._postgre_sql_management_client_enums import RestrictedEnum
from ._postgre_sql_management_client_enums import ServerHAState
from ._postgre_sql_management_client_enums import ServerPublicNetworkAccessState
from ._postgre_sql_management_client_enums import ServerState
from ._postgre_sql_management_client_enums import ServerVersion
from ._postgre_sql_management_client_enums import SkuTier
from ._postgre_sql_management_client_enums import SourceType
from ._postgre_sql_management_client_enums import SslMode
from ._postgre_sql_management_client_enums import StartDataMigrationEnum
from ._postgre_sql_management_client_enums import StorageAutoGrow
from ._postgre_sql_management_client_enums import StorageAutoGrowthSupportedEnum
from ._postgre_sql_management_client_enums import StorageType
from ._postgre_sql_management_client_enums import ThreatProtectionName
from ._postgre_sql_management_client_enums import ThreatProtectionState
from ._postgre_sql_management_client_enums import TriggerCutoverEnum
from ._postgre_sql_management_client_enums import ValidationState
from ._postgre_sql_management_client_enums import VirtualEndpointType
from ._postgre_sql_management_client_enums import ZoneRedundantHaAndGeoBackupSupportedEnum
from ._postgre_sql_management_client_enums import ZoneRedundantHaSupportedEnum
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ActiveDirectoryAdministrator",
    "ActiveDirectoryAdministratorAdd",
    "AdminCredentials",
    "AdministratorListResult",
    "AuthConfig",
    "Backup",
    "BackupRequestBase",
    "BackupSettings",
    "BackupStoreDetails",
    "CapabilitiesListResult",
    "CapabilityBase",
    "CheckNameAvailabilityRequest",
    "CheckNameAvailabilityResponse",
    "Configuration",
    "ConfigurationForUpdate",
    "ConfigurationListResult",
    "DataEncryption",
    "Database",
    "DatabaseListResult",
    "DbLevelValidationStatus",
    "DbMigrationStatus",
    "DbServerMetadata",
    "DelegatedSubnetUsage",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorResponse",
    "FastProvisioningEditionCapability",
    "FirewallRule",
    "FirewallRuleListResult",
    "FlexibleServerCapability",
    "FlexibleServerEditionCapability",
    "HighAvailability",
    "LogFile",
    "LogFileListResult",
    "LtrBackupRequest",
    "LtrBackupResponse",
    "LtrPreBackupRequest",
    "LtrPreBackupResponse",
    "LtrServerBackupOperation",
    "LtrServerBackupOperationList",
    "MaintenanceWindow",
    "MigrationNameAvailabilityResource",
    "MigrationResource",
    "MigrationResourceForPatch",
    "MigrationResourceListResult",
    "MigrationSecretParameters",
    "MigrationStatus",
    "MigrationSubStateDetails",
    "NameAvailability",
    "Network",
    "Operation",
    "OperationDisplay",
    "OperationListResult",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "ProxyResource",
    "Replica",
    "Resource",
    "RestartParameter",
    "Server",
    "ServerBackup",
    "ServerBackupListResult",
    "ServerForUpdate",
    "ServerListResult",
    "ServerSku",
    "ServerSkuCapability",
    "ServerThreatProtectionListResult",
    "ServerThreatProtectionSettingsModel",
    "ServerVersionCapability",
    "Sku",
    "Storage",
    "StorageEditionCapability",
    "StorageMbCapability",
    "StorageTierCapability",
    "SystemData",
    "TrackedResource",
    "UserAssignedIdentity",
    "UserIdentity",
    "ValidationDetails",
    "ValidationMessage",
    "ValidationSummaryItem",
    "VirtualEndpointResource",
    "VirtualEndpointResourceForPatch",
    "VirtualEndpointsListResult",
    "VirtualNetworkSubnetUsageParameter",
    "VirtualNetworkSubnetUsageResult",
    "ActiveDirectoryAuthEnum",
    "ArmServerKeyType",
    "AzureManagedDiskPerformanceTiers",
    "CancelEnum",
    "CapabilityStatus",
    "CheckNameAvailabilityReason",
    "ConfigurationDataType",
    "CreateMode",
    "CreateModeForUpdate",
    "CreatedByType",
    "ExecutionStatus",
    "FailoverMode",
    "FastProvisioningSupportedEnum",
    "GeoBackupSupportedEnum",
    "GeoRedundantBackupEnum",
    "HaMode",
    "HighAvailabilityMode",
    "IdentityType",
    "KeyStatusEnum",
    "LogicalReplicationOnSourceDbEnum",
    "MigrateRolesEnum",
    "MigrationDbState",
    "MigrationDetailsLevel",
    "MigrationListFilter",
    "MigrationMode",
    "MigrationNameAvailabilityReason",
    "MigrationOption",
    "MigrationState",
    "MigrationSubState",
    "OnlineResizeSupportedEnum",
    "OperationOrigin",
    "Origin",
    "OverwriteDbsInTargetEnum",
    "PasswordAuthEnum",
    "PrincipalType",
    "PrivateEndpointConnectionProvisioningState",
    "PrivateEndpointServiceConnectionStatus",
    "ReadReplicaPromoteMode",
    "ReplicationPromoteOption",
    "ReplicationRole",
    "ReplicationState",
    "RestrictedEnum",
    "ServerHAState",
    "ServerPublicNetworkAccessState",
    "ServerState",
    "ServerVersion",
    "SkuTier",
    "SourceType",
    "SslMode",
    "StartDataMigrationEnum",
    "StorageAutoGrow",
    "StorageAutoGrowthSupportedEnum",
    "StorageType",
    "ThreatProtectionName",
    "ThreatProtectionState",
    "TriggerCutoverEnum",
    "ValidationState",
    "VirtualEndpointType",
    "ZoneRedundantHaAndGeoBackupSupportedEnum",
    "ZoneRedundantHaSupportedEnum",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
