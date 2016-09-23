---
title: PushBot (TUM SpiNNaker Robot)
---

# The Robot

<center>
<img src="therobot.jpg" style="width: 400px">
</center>

# The wifi connector for the SpiNNaker machine

<center>
<img src="wificonnector.jpg" style="width: 400px">
</center>

# The wifi access point that is used to relay between the push bot and either a host machine or the wifi connector.

<center>
<img src="wifi_access_point.jpg" style="width: 400px">
</center>

The PushBot is a robotic platform developed by [Technische Universität München](http://www.ei.tum.de/en/research/coc-neuro-engineering/).

# Hardware Overview

## Robot Features

  * 2 tracks, each controlled by 2 wheels.
  * A silicon retina
  * A laser

## Control Systems

The robot can be connected to a SpiNNaker machine through 2 interfaces.
    * It can go through the SpiNNaker link connector via the WiFi connector provided above.
    * It can be connected to SpiNNaker via the access point (shown above) indirectly via a host machine and using the SpiNNaker Software Stack.

# SpiNNaker-Facing API

The API for the robot has changed and is now defined in the following google document:

[https://docs.google.com/document/d/1lJ2t5ISbdJpgHs7oGCI9pG10y2xzKz2hoclRX5WocLM/pub](https://docs.google.com/document/d/1lJ2t5ISbdJpgHs7oGCI9pG10y2xzKz2hoclRX5WocLM/pub)

(Alternatively, a copy was made on 22-09-14 in the event that the above link should die: [http://pastebin.com/HC5GPs0n](http://pastebin.com/HC5GPs0n))

## Charging

The robot has 4 AA batteries which are located below:

<center>
<img src="where_batteries_are_on_pushbot.jpg" style="width: 400px">
</center>

There is a provided battery charger as shown below:

<center>
<img src="battery_charger.jpg" style="width: 400px">
</center>

## Wifi Access Point

The robot's wifi interface consists of a WiFi access point to which the pushbot communicates with regardless of the connection type for SpiNNaker. The network details are as follows:

2.4 GHz
	SSID: NSTrobots_2.4GHz
	wireless mode: b/g/n mixed
	b/g Protection: auto
	channel bandwidth: 20/40 MHz
	channel: auto
	extension channel: above
	authentication method: wpa2-personal
	wpa encryption: aes
	wpa key: rpo45trkrfgpoloektr45poael
	network key rotation level: 3600
	tx power adjustment: 100
	region code: europe (channels 1-13)

	Guest AP: off
	Bridge: AP only, Channel auto
	Wireless MAC filter: empty
	Radius Setting: empty

5.0 GHz
	SSID: NSTrobots_5GHz
	mode: a/n
	rest see above

LAN
	IP: 10.162.177.1
	Subnet: 255.255.255.0

	DHCP Server
		Domain Name: tu-muenchen.de
		IP Pool Start: 10.162.177.175
		IP Pool End: 10.162.177.249
		Lease Time: 86400
		Default GW: 10.162.177.254therobot

		DNS 1: 10.156.33.53
		DNS 2: 129.187.5.1

		Manual Assignment:
			00:23:A7:01:04:89	10.162.177.20	RedPineMiniSPI00
			00:23:A7:01:08:2E	10.162.177.21	RedPineMiniSPI01
			00:23:A7:01:08:17	10.162.177.22	RedPineMiniSPI02
			00:23:A7:1B:C7:D9	10.162.177.30	RedPineSPIEval
			00:23:A7:1B:C9:77	10.162.177.31	RedPineSPI01
			00:23:A7:1B:C9:34	10.162.177.32	RedPineSPI02
			00:23:A7:1D:C7:8E	10.162.177.40	RedPineSmall00
			00:23:A7:1D:88:EB	10.162.177.41	RedPineSmall01
			00:23:A7:1F:0E:FD	10.162.177.42	RedPineSmall02
			00:23:A7:1D:8B:27	10.162.177.43	RedPineSmallSPI03
			00:23:A7:1D:5B:60	10.162.177.44	RedPineSmallSPI04
			00:23:A7:1D:8A:8E	10.162.177.45	RedPineSmallSPI05
			00:23:A7:1D:5A:E7	10.162.177.50	OmniRob7-ROB-TOP
			00:23:A7:1B:C7:94	10.162.177.51	OmniRob7-000
			00:23:A7:1D:8A:95	10.162.177.53	OmniRob7-120
			00:23:A7:1D:5A:F5	10.162.177.55	OmniRob7-240
			00:01:36:1D:D7:13	10.162.177.60	Rovio00
			00:01:36:22:84:74	10.162.177.61	Rovio01
			00:23:A7:1D:58:4A	10.162.177.62	OmniRob62
			00:23:A7:1D:5A:DB	10.162.177.63	OmniRob63
			00:23:A7:1F:0F:94	10.162.177.64	OmniRob64
			00:23:A7:1D:36:9C	10.162.177.65	OmniRob65
			00:23:A7:1D:36:80	10.162.177.66	OmniRob66
			00:23:A7:00:14:11	10.162.177.130	RedPine5GHzSPI0
			00:23:A7:00:9C:B1	10.162.177.131	RedPine5GHzSPI1
			00:23:A7:00:14:1D	10.162.177.132	RedPine5GHzSPI2
			00:23:A7:00:9B:C9	10.162.177.133	RedPine5GHzSPI3
			00:23:A7:00:14:13	10.162.177.134	RedPine5GHzSPI4
			00:23:A7:00:9C:A7	10.162.177.135	RedPine5GHzSPI5
			00:23:A7:00:9B:D2	10.162.177.136	RedPine5GHzSPI6
			00:23:A7:00:9A:30	10.162.177.137	RedPine5GHzSPI7
			00:23:A7:00:9B:4A	10.162.177.138	RedPine5GHzSPI8
			4C:E6:76:F7:DE:35	10.162.177.59	SpOmniBot

	Route
		use dhcp routes: yes
		enable static routes: yes
		static routes:
			0.0.0.0	0.0.0.0	10.162.177.254	303	LAN

	IPTV
		off

Firewall
	Disabled


Login
	nst/nst

The IP of the pushbot is 10.162.177.XXXXX where XXXXX is the number of the red circle at the back of the push bot. As shown below, where the IP would by 10.162.177.57.

<center>
<img src="back_of_push_bot.jpg" style="width: 400px">
</center>
