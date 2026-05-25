---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Figurehead]]", "[[Magical]]", "[[Water]]"]
price: "{'gp': 490}"
usage: "attached-to-ships-bow"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** attached to a ship's bow

A knot of tentacles makes up the body of this figurehead. It's always slightly slimy and sticky to the touch. Superstitious sailors tend to avoid ships with this figurehead on the bow, claiming it's bad luck to flaunt a kraken's image while at sea.

**Activate—Lash Out!** `pf2:2` (aura, concentrate)

**Frequency** once per hour

**Effect** The effigy causes spectral tentacles to erupt from the ship's hull. These tentacles lash out in an emanation with a distance equal to the ship's length and remain active for 10 minutes. Creatures in the aura and in the same body of water as the ship take a -2 circumstance penalty to Athletics checks to [[Swim]] as the writhing tentacles lash out in all directions.

**Activate—Grab Them!** `pf2:1` (attack, concentrate)

**Requirements** The ship's spectral tentacles are activated

**Effect** The tentacles grab at an enemy vessel in the aura. Attempt a piloting check against the target vessel's AC. On a success, the tentacles grab hold and tether the two vessels together. While tethered, the ships can't move farther away from each other, creatures aboard the enemy vessel receive a -2 circumstance penalty to all piloting checks, and creatures attempting to [[Board]] the enemy vessel gain a +2 circumstance bonus to any check required to do so.

If you use this activation while the tentacles are already latched onto another ship, the tentacles instead pull that ship toward yours a distance up to half your ship's swim Speed with a success (or up to your ship's full swim Speed with a critical success). The pilot of the enemy ship can attempt a DC 27 piloting check to break free as a single action that has the attack trait. With a success, the ship frees itself from the tentacles.

**Source:** `= this.source` (`= this.source-type`)
