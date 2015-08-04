'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2
Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''

from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.link import TCLink


class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        setLogLevel('info')
        Topo.__init__(self, **opts)
        
        c1 = self.addSwitch('c1')

        aggregations = iter(xrange(1, fanout + 1))
        edges = iter(xrange(1, fanout * fanout + 1))
        hosts = iter(xrange(1, fanout * fanout * fanout + 1))

        for aggregation in range(1, fanout + 1):
            a = self.addSwitch('a{}'.format(next(aggregations)))
            self.addLink(c1, a, **linkopts1)
            for edge in range(1, fanout + 1):
                e = self.addSwitch('e{}'.format(next(edges)))
                self.addLink(a, e, **linkopts2)
                for host in range(1, fanout + 1):
                    h = self.addHost('h{}'.format(next(hosts)))
                    self.addLink(e, h, **linkopts3)



        
                    
topos = {'custom': (lambda: CustomTopo())}


# def simple_test():
#     """Create and test a simple network """
#
#     linkopts = dict(bw=10, delay='5ms', max_queue_size=1000, use_htb=True)
#
#     topology = CustomTopo(linkopts, linkopts, linkopts, 3)
#     net = Mininet(topology, link=TCLink)
#     net.start()
#     print "Dumping host connections"
#     dumpNodeConnections(net.hosts)
#     print "Testing network connectivity"
#     net.pingAll()
#     h1 = net.get('h1')
#     h27 = net.get('h27')
#
#     print h1.cmd('ping', '-c6', h27.IP())
#     net.stop()
#
#
# if __name__ == '__main__':
#     # Tell mininet to print useful information
#     setLogLevel('info')
#     simple_test()