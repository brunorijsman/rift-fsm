# System test: test_sys_2n_l0_l1
#
# See topology 2n_l0_l1.yaml
#
# We test the following:
# * Bring the topology up
# * The CLI reports that adjacency reaches state 3-way on both nodes
# * The expected FSM transitions to reach state 3-way occur on both nodes
# * Fail interface if1 on node1 (bi-directional failure)
# * The CLI on node1 reports that the adjaceny to node2 is in state 2-way
# * The CLI on node2 reports that the adjaceny to node2 is in state 1-way

# Allow long test names
# pylint: disable=invalid-name

from rift_expect_session import RiftExpectSession
from log_expect_session import LogExpectSession

def check_rift_node1_intf_up(res):
    res.check_adjacency_3way(
        node="node1",
        interface="if1",
        other_node="node2",
        other_interface="if1")
    res.check_rx_offer(
        node="node1",
        interface="if1",
        system_id="2",
        level=0,
        not_a_ztp_offer=False,
        state="THREE_WAY",
        best=False,
        best_3way=False,
        removed=True,
        removed_reason="Level is leaf")
    res.check_tx_offer(
        node="node1",
        interface="if1",
        system_id="1",
        level=1,
        not_a_ztp_offer=False,
        state="THREE_WAY")
    res.check_level(
        node="node1",
        configured_level=1,
        level_value=1)

def check_rift_node1_intf_down(res):
    res.check_adjacency_1way(
        node="node1",
        interface="if1")
    # TODO: Check offers and level

def check_rift_node2_intf_up(res):
    res.check_adjacency_3way(
        node="node2",
        interface="if1",
        other_node="node1",
        other_interface="if1")
    res.check_rx_offer(
        node="node2",
        interface="if1",
        system_id="1",
        level=1,
        not_a_ztp_offer=False,
        state="THREE_WAY",
        best=True,
        best_3way=True,
        removed=False,
        removed_reason="")
    res.check_tx_offer(
        node="node2",
        interface="if1",
        system_id="2",
        level=0,
        not_a_ztp_offer=False,
        state="THREE_WAY")
    res.check_level(
        node="node2",
        configured_level=0,
        level_value=0)

def check_rift_node2_intf_down(res):
    res.check_adjacency_1way(
        node="node2",
        interface="if1")
    # TODO: Check offers and level

def check_log_node1_intf_up(les):
    les.check_lie_fsm_3way("node1", "if1")
    #!!!les.check_lie_fsm_3way("node2", "if1")

# TODO: Check log when interface is down

def test_2_nodes_l0_l1():
    # Bring topology up
    res = RiftExpectSession("2n_l0_l1")
    les = LogExpectSession("rift.log")
    # Check that adjacency reaches 3-way
    check_rift_node1_intf_up(res)
    check_rift_node2_intf_up(res)
    check_log_node1_intf_up(les)
    # Bring interface if1 on node1 down
    res.interface_failure("node1", "if1", "failed")
    check_rift_node1_intf_down(res)
    check_rift_node2_intf_down(res)
    # Done
    res.stop()
    # Check FSM
    # TODO: Check FSM transitions after interface failure
