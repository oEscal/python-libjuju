# DO NOT CHANGE THIS FILE! This file is auto-generated by facade.py.
# Changes will be overwritten/lost when the file is regenerated.

from juju.client import _client1, _client2, _client3, _client4, _client5
from juju.client._definitions import *  # noqa

CLIENTS = {
    "1": _client1,
    "2": _client2,
    "3": _client3,
    "4": _client4,
    "5": _client5
}


def lookup_facade(name, version):
        """
        Given a facade name and version, attempt to pull that facade out
        of the correct client<version>.py file.

        """
        for _version in range(int(version), 0, -1):
            try:
                facade = getattr(CLIENTS[str(_version)], name)
                return facade
            except (KeyError, AttributeError):
                continue
        else:
            raise ImportError("No supported version for facade: "
                              "{}".format(name))


class TypeFactory:
    @classmethod
    def from_connection(cls, connection):
        """
        Given a connected Connection object, return an initialized and
        connected instance of an API Interface matching the name of
        this class.

        @param connection: initialized Connection object.

        """
        version = connection.facades[cls.__name__[:-6]]

        c = lookup_facade(cls.__name__, version)
        c = c()
        c.connect(connection)

        return c


class ActionFacade(TypeFactory):
    pass


class AgentFacade(TypeFactory):
    pass


class AgentToolsFacade(TypeFactory):
    pass


class AllModelWatcherFacade(TypeFactory):
    pass


class AllWatcherFacade(TypeFactory):
    pass


class AnnotationsFacade(TypeFactory):
    pass


class ApplicationFacade(TypeFactory):
    pass


class ApplicationRelationsWatcherFacade(TypeFactory):
    pass


class ApplicationScalerFacade(TypeFactory):
    pass


class BackupsFacade(TypeFactory):
    pass


class BlockFacade(TypeFactory):
    pass


class BundleFacade(TypeFactory):
    pass


class CharmRevisionUpdaterFacade(TypeFactory):
    pass


class CharmsFacade(TypeFactory):
    pass


class CleanerFacade(TypeFactory):
    pass


class ClientFacade(TypeFactory):
    pass


class CloudFacade(TypeFactory):
    pass


class ControllerFacade(TypeFactory):
    pass


class DeployerFacade(TypeFactory):
    pass


class DiscoverSpacesFacade(TypeFactory):
    pass


class DiskManagerFacade(TypeFactory):
    pass


class EntityWatcherFacade(TypeFactory):
    pass


class FilesystemAttachmentsWatcherFacade(TypeFactory):
    pass


class FirewallerFacade(TypeFactory):
    pass


class HighAvailabilityFacade(TypeFactory):
    pass


class HostKeyReporterFacade(TypeFactory):
    pass


class ImageManagerFacade(TypeFactory):
    pass


class ImageMetadataFacade(TypeFactory):
    pass


class InstancePollerFacade(TypeFactory):
    pass


class KeyManagerFacade(TypeFactory):
    pass


class KeyUpdaterFacade(TypeFactory):
    pass


class LeadershipServiceFacade(TypeFactory):
    pass


class LifeFlagFacade(TypeFactory):
    pass


class LogForwardingFacade(TypeFactory):
    pass


class LoggerFacade(TypeFactory):
    pass


class MachineActionsFacade(TypeFactory):
    pass


class MachineManagerFacade(TypeFactory):
    pass


class MachineUndertakerFacade(TypeFactory):
    pass


class MachinerFacade(TypeFactory):
    pass


class MeterStatusFacade(TypeFactory):
    pass


class MetricsAdderFacade(TypeFactory):
    pass


class MetricsDebugFacade(TypeFactory):
    pass


class MetricsManagerFacade(TypeFactory):
    pass


class MigrationFlagFacade(TypeFactory):
    pass


class MigrationMasterFacade(TypeFactory):
    pass


class MigrationMinionFacade(TypeFactory):
    pass


class MigrationStatusWatcherFacade(TypeFactory):
    pass


class MigrationTargetFacade(TypeFactory):
    pass


class ModelConfigFacade(TypeFactory):
    pass


class ModelManagerFacade(TypeFactory):
    pass


class NotifyWatcherFacade(TypeFactory):
    pass


class PayloadsFacade(TypeFactory):
    pass


class PayloadsHookContextFacade(TypeFactory):
    pass


class PingerFacade(TypeFactory):
    pass


class ProvisionerFacade(TypeFactory):
    pass


class ProxyUpdaterFacade(TypeFactory):
    pass


class RebootFacade(TypeFactory):
    pass


class RelationUnitsWatcherFacade(TypeFactory):
    pass


class RemoteApplicationWatcherFacade(TypeFactory):
    pass


class RemoteRelationsWatcherFacade(TypeFactory):
    pass


class ResourcesFacade(TypeFactory):
    pass


class ResourcesHookContextFacade(TypeFactory):
    pass


class ResumerFacade(TypeFactory):
    pass


class RetryStrategyFacade(TypeFactory):
    pass


class SSHClientFacade(TypeFactory):
    pass


class SingularFacade(TypeFactory):
    pass


class SpacesFacade(TypeFactory):
    pass


class StatusHistoryFacade(TypeFactory):
    pass


class StorageFacade(TypeFactory):
    pass


class StorageProvisionerFacade(TypeFactory):
    pass


class StringsWatcherFacade(TypeFactory):
    pass


class SubnetsFacade(TypeFactory):
    pass


class UndertakerFacade(TypeFactory):
    pass


class UnitAssignerFacade(TypeFactory):
    pass


class UniterFacade(TypeFactory):
    pass


class UpgraderFacade(TypeFactory):
    pass


class UserManagerFacade(TypeFactory):
    pass


class VolumeAttachmentsWatcherFacade(TypeFactory):
    pass
