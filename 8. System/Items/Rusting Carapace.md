---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Laminar]]"]
price: "{'gp': 476}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 leather lamellar armor* incorporates the plates of an ore louse's hide, woven together with the creature's own sinew into a functional set of armor. While wearing the rusting carapace, you gain a +1 circumstance bonus to AC and saving throws against any effect that would rust you or your items, such as the ore louse's Strikes that have the rust ability or the [[Rust Cloud]] spell.

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** Oxidizing liquid seeps from between the segments of the rusting hide onto a nearby metal creature, non-magical metal hazard, or non-magical metal item of up to 1 Bulk. A targeted creature or hazard gets a DC 24 [[Fortitude]] save; a targeted item automatically gets a critical failure if unattended, but a creature holding or wearing it can attempt a DC 24 [[Reflex]] save. The rust deals 8d6 untyped damage to a creature or hazard, plus 2d6 persistent damage on a failed save; it deals 2d6 untyped damage to an item, plus 1d6 persistent damage on a failed save.

**Craft Requirements** The initial raw materials must include the hide of an ore louse.

**Source:** `= this.source` (`= this.source-type`)
