from django.test import LiveServerTestCase

from .utils.distributed_server_factory import DistributedServer


class SameVersionTests(LiveServerTestCase):

    def test_can_run_on_distributed_server(self):
        with DistributedServer(CENTRAL_SERVER_HOST=self.live_server_url) as d1:
            d1.call_command('validate')
            _stdout, stderr = d1.wait()
            # the command shouldn't have printed anything to stderr
            self.assertFalse(stderr)

    def test_can_instantiate_two_distributed_servers(self):
        settings = {'CENTRAL_SERVER_HOST': self.live_server_url}

        with DistributedServer(**settings) as d1, DistributedServer(**settings) as d2:
            d1.call_command('validate')
            d2.call_command('validate')

            d1.wait()
            d2.wait()