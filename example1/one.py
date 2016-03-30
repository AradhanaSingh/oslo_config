#Code to read configuration from app.conf

from oslo_config import cfg

# creating a group
opt_group = cfg.OptGroup(name='simple', title='A simple Example')

# creating options
simple_opts = [cfg.BoolOpt('enable', default=False,help=('True enables, False disables'))]

CONF = cfg.CONF

# registering group
CONF.register_group(opt_group)

# registering options with their groups
CONF.register_opts(simple_opts, opt_group)

if __name__ =="__main__":
        # specifying file from which configuration will be read
        # if file is not specified, default value is used
        CONF(default_config_files=['app.conf'])
	print(CONF.simple.enable)
