import re
from knack.util import CLIError


def validate_resource_group(namespace):
    if not re.match('^[a-z][a-z0-9\-]{0,50}$', namespace.resource_group.lower()):
        raise CLIError('Name limited to 50 characters. Can only contain letters and numbers, and start with a letter')
