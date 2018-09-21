# mininet

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
