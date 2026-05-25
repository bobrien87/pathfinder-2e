---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Cold]]", "[[Reach]]"]
price: "{'gp': 10000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking greater frost longspear* appears to be a single continuous icicle stretching over 6 feet long. The icicle automatically extinguishes non-magical fires in a @Template[emanation|distance:20]. While wielding it, you gain fire resistance 5.

**Activate—Quench Flames** `pf2:2` (concentrate, manipulate)

**Effect** You swing the icicle into the area of an ongoing magical fire, and the spear attempts to counteract the fire with a counteract modifier of +27. If it fails, it can't attempt to counteract the same fire again.

**Activate—Ice Spike** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** The icicle grows rapidly, piercing creatures in a @Template[line|distance:30]. Each creature in the area takes @Damage[11d6[cold]|options:area-damage] damage with a DC 35 [[Reflex]] save. A creature that fails its save also takes 3d6 persistent,bleed damage (double on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
