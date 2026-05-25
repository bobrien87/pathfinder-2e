---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Concussive]]", "[[Scatter 10]]"]
price: "{'gp': 24000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *major breath blaster* is a *+3 major striking blunderbuss* most commonly crafted from the trachea of a dragon, though other creatures with breath attacks or the ability to spit energy are occasionally used. The implementation of the dragon's trachea allows the firearm to unleash a torrent of pure energy in the form of gouts of flame or bolts of electricity.

A *breath blaster's* Strikes deal either acid, cold, electricity, fire, or poison damage, depending on the dragon type or other creature from which it was made, though it can otherwise be used like a normal blunderbuss. A breath blaster also can be activated to fire a line of energy in a @Template[line|distance:30] or @Template[cone|distance:15], chosen when it's created and typically corresponding to the shape of the breath attack used by the type of dragon or creature from which the *breath blaster was created.*

In theory, the foundational techniques required to create a breath blaster would allow for other damage types, but such breath blasters would require the trachea from the correct dragon or creature type and additional creation techniques, making such a breath blaster rare rather than uncommon.

**Activate—Breath Blast** `pf2:2` (manipulate)

**Frequency** once per minute

**Effect** You fire the breath blaster, dealing 10d6 untyped damage of the appropriate type in the appropriate area. Creatures in the area must attempt a DC 38 [[Reflex]] save (or DC 38 [[Fortitude]] save if the damage is poison).

**Craft Requirements** The initial raw materials must include the trachea of a ritually hunted dragon or other creature with a breath attack with the appropriate damage type and area (line or cone) for the *breath blaster*.

**Source:** `= this.source` (`= this.source-type`)
