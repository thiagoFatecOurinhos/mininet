#!/usr/bin/python
#
# 2hosts-with-nat.py - Mininet network topology created to
#                      practical tests in final paper graduate
#                      work in Fatec Ourinhos College
#
# @author  thiago at fatecourinhos.edu.br
# @since   2016-06
# @version v1.0
#
#************************** [ Visao Virtualbox ]
# +--[Mininet-VM]--+
# |             [eth0] <-------> [Virtualbox Host-only]
# | Mininet-VM  [eth1] <-------> [*bridge* (s1)]
# |             [eth2] <-------> [*bridge* (s2)]
# +----[eth3]------+                 |
#    /
#   /                                 +--Firewall-VM]--+
#  --> [switch-mininet (vbox)] <---> {eth1}        {eth0} <---> {Internet}
#                                     +----------------+
#
#
#**************************************************************************
from mininet.net  import Mininet
from mininet.node import Controller
from mininet.cli  import CLI
from mininet.link import Intf
from mininet.log  import setLogLevel, info

def redeThiago():
    # Criando topologia sem definicao, apenas para testes
    net = Mininet(topo=None, build=False)
    # Adiciona a Controladora com nome c0
    info( '=> ADICIONANDO CONTROLLER c0...\n' )
    net.addController(name='c0')

    # Cria switch s1, que deve ser bridge da eth1 e conectar o host h1
    info( '=> ADICIONANDO SWITCH s1 NA PORTA 3364...\n')
    s1 = net.addSwitch('s1')
    # Adicionando eth1 da controller na switch s1
    Intf( 'eth1', node=s1 )
    s1.listenPort = 6634

    # Cria switch s2, que deve ser bridge da eth2 e conectar o host h2
    info( '=> ADICIONANDO SWITCH s2 NA PORTA 3365...\n')
    s2 = net.addSwitch('s2')
    # Adicionando eth2 da controller na switch s1
    Intf( 'eth2', node=s2 )
    s2.listenPort = 6635

    # Cria o host h1 sem parametros de rede
    info( '=> ADICIONANDO HOST h1...\n')
    h1 = net.addHost('h1', ip='0.0.0.0')

    # Cria o host h2 sem parametros de rede
    info( '=> ADICIONANDO HOST h2...\n')
    h2 = net.addHost('h2', ip='0.0.0.0')

    # Monta a topologia fisica (links)
    info( '=> LIGANDO HOSTS AO SWITCH...\n')
    # Liga host h1 ao switch s1
    net.addLink(h1, s1)
    # Liga host h2 ao switch s1 e s2
    net.addLink(h2, s2) # Deve vir primeiro
    net.addLink(h2, s1)

    # Configuracoes de rede (IPs, MACs e DNS)
    info( '=> CONFIGURANDO REDE NOS HOSTS...\n')
    net.start()

    h1.cmdPrint('ifconfig h1-eth0 172.16.0.10 netmask 255.255.255.0 hw ether 00:00:00:00:00:02')
    h1.cmdPrint('route add default gw 172.16.0.1')
    h1.cmdPrint('echo nameserver\ 8.8.8.8 > /etc/resolv.conf')

    h2.cmdPrint('ifconfig h2-eth0 172.16.0.20 netmask 255.255.255.0 hw ether 00:00:00:00:00:03')
    h2.cmdPrint('route add default gw 172.16.0.1')
    h2.cmdPrint('echo nameserver\ 8.8.8.8 > /etc/resolv.conf')

    h2.cmdPrint('ifconfig h2-eth1 172.16.0.21 netmask 255.255.255.0 hw ether 00:00:00:00:00:05')


    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    redeThiago()
