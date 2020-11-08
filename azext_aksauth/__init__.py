from azure.cli.core import AzCommandsLoader
import azext_aksauth._help  # pylint: disable=unused-import
from ._validators import validate_resource_group


class AKSAuthExtCommandLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        aksauth_custom = CliCommandType(operations_tmpl='azext_aksauth.custom#{}')
        super(AKSAuthExtCommandLoader, self).__init__(
            cli_ctx=cli_ctx, custom_command_type=aksauth_custom)

    def load_command_table(self, _):
        with self.command_group('aksauth') as g:
            g.custom_command('connect', 'aksauth_connect')
        return self.command_table

    def load_arguments(self, _):
        with self.argument_context('aksauth connect') as c:
            c.argument('resource_group',
                       options_list=['--resource-group', '-g'],
                       help='Cluster Resource Group',
                       validator=validate_resource_group,
                       type=str.lower)
            c.argument('cluster_name',
                       options_list=['--cluster-name', '-c'],
                       help='Cluster Name',
                       type=str.lower)
            c.argument('tenant',
                       help='Tenant ID',
                       options_list=['--tenant', '-t'],
                       default=None,
                       type=str.lower)
            c.argument('username',
                       help='Username',
                       options_list=['--username', '-u'],
                       default=None,
                       type=str.lower)
            c.argument('password',
                       help='Password',
                       options_list=['--password', '-p'],
                       default=None)     
                                         
COMMAND_LOADER_CLS = AKSAuthExtCommandLoader
