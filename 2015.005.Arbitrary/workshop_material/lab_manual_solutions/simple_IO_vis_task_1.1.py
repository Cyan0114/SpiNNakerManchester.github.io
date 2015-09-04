# imports of both spynnaker and external device plugin.
import spynnaker.pyNN as Frontend
import spynnaker_external_devices_plugin.pyNN as ExternalDevices
from spynnaker_external_devices_plugin.pyNN.connections\
    .spynnaker_live_spikes_connection import SpynnakerLiveSpikesConnection
# plotter in python
import pylab
# initial call to set up the front end (pynn requirement)
Frontend.setup(timestep=1.0, min_delay=1.0, max_delay=144.0)
# neurons per population and the length of runtime in ms for the simulation,
# as well as the expected weight each spike will contain
n_neurons = 100
run_time = 8000
weight_to_spike = 2.0
# neural parameters of the ifcur model used to respond to injected spikes.
# (cell params for a synfire chain)
cell_params_lif = {'cm': 0.25, 'i_offset': 0.0, 'tau_m': 20.0, 'tau_refrac': 2.0,
                   'tau_syn_E': 5.0, 'tau_syn_I': 5.0, 'v_reset': -70.0, 'v_rest': -65.0,
                   'v_thresh': -50.0}
# create synfire populations (if cur exp)
pop_forward = Frontend.Population(n_neurons, Frontend.IF_curr_exp,
                                  cell_params_lif, label='pop_forward')
# Create injection populations
injector_forward = Frontend.Population(
    n_neurons, ExternalDevices.SpikeInjector,
    {'port':12365}, label='spike_injector_forward')
# Create a connection from the injector into the populations
Frontend.Projection(injector_forward, pop_forward,
                    Frontend.OneToOneConnector(weights=weight_to_spike))
# Synfire chain connections where each neuron is connected to its next neuron
# NOTE: there is no recurrent connection so that each chain stops once it
# reaches the end
loop_forward = list()
loop_backward = list()
for i in range(0, n_neurons - 1):
    loop_forward.append((i, (i + 1) % n_neurons, weight_to_spike, 3))
Frontend.Projection(pop_forward, pop_forward,
                    Frontend.FromListConnector(loop_forward))
# record spikes from the synfire chains so that we can read off valid results
# in a safe way afterwards, and verify the behavior
pop_forward.record()
# Create a sender of packets for the forward population
def send_input_forward(label, sender):
        print "Sending forward spike for neuron 0"
        sender.send_spike(label, 0)
# Set up the live connection for sending spikes
live_spikes_connection = SpynnakerLiveSpikesConnection(
    receive_labels=None, local_port=19999,
    send_labels=["spike_injector_forward"])
# Set up callbacks to occur at the start of simulation
live_spikes_connection.add_start_callback("spike_injector_forward",
                                          send_input_forward)
# Run the simulation on spiNNaker
Frontend.run(run_time)
# Retrieve spikes from the synfire chain population
spikes_forward = pop_forward.getSpikes()
# If there are spikes, plot using matplotlib
if len(spikes_forward) != 0:
    pylab.figure()
    if len(spikes_forward) != 0:
        pylab.plot([i[1] for i in spikes_forward],
                   [i[0] for i in spikes_forward], "b.")
    pylab.ylabel('neuron id')
    pylab.xlabel('Time/ms')
    pylab.title('spikes')
    pylab.show()
else:
    print "No spikes received"
# Clear data structures on spiNNaker to leave the machine in a clean state for
# future executions
Frontend.end()
