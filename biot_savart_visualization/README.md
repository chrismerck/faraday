This is a demo visualization of a potential current running through a wire and the magnetic field which it generates.

This is a very early version and is meant only for testing cubes. Attempts at generating any other fields will probably break the simulation.

Tested with Python 3.4.3 and matplotlib version 2.0.0b3+1972.g2cdb5aa

The newest matplotlib version is required because of the normalization feature added to the 3D quiver plot function.

### TODO (In no particular order)
- [ ] Abstract code properply
- [ ] Add a way for the user to specifiy settings during initial runtime of the program. Or load the settings from a file.
- [ ] Re-write resolution feature with the dictionary idea.
- [ ] Decouple current from a few things.
- [ ] Custom current input.
