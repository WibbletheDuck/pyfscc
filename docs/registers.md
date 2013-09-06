# Registers

The FSCC driver is a swiss army knife of sorts with communication. It can
handle many different situations, if configured correctly. Typically to
configure it to handle your specific situation you need to modify the card's
register values.

_For a complete listing of all of the configuration options please see the 
manual._

In HDLC mode some settings are fixed at certain values. If you are in
HDLC mode and after setting/getting your registers some bits don't look correct,
then they are likely fixed. A complete list of the fixed values can be found in 
the CCR0 section of the manual.

All of the registers, except FCR, are tied to a single port. FCR on the other hand 
is shared between two ports on a card. You can differentiate between which FCR 
settings affects what port by the A/B labels. A for port 0 and B for port 1.

You should purge the data stream after changing the registers.
Settings like CCR0 will require being purged for the changes to take 
effect.

###### Driver Support
| Code           | Version
| -------------- | --------
| `fscc-windows` | `v2.0.0` 
| `fscc-linux`   | `v2.0.0` 
| `pyfscc`       | `v1.0.0`


## Property
```python
registers = property(...)
```


## Set
###### Examples
```python
import fscc
...

p.registers.CCR0 = 0x0011201c
p.registers.BGR = 10
```


## Get
###### Examples
```python
import fscc
...

ccr0 = p.registers.CCR0
bgr = p.registers.BGR
```


### Additional Resources
- Complete example: [`examples\registers.py`](https://github.com/commtech/pyfscc/blob/master/examples/registers.py)
- Implemenation details: [`src\fscc.py`](https://github.com/commtech/pyfscc/blob/master/src/fscc.py)