---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Aura]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 50}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A blue finish decorates the ceramic body of a wind ocarina. When you play a note on this ocarina, for 1 minute, winds sweep into strong gusts in a @Template[emanation|distance:5] around you. The winds have the following effects.

- Ammunition from physical ranged attacks—such as arrows, bolts, sling bullets, and other objects of comparable size—can't pass through the area. Passing through the area causes attacks with bigger ranged weapons, such as thrown weapons, to take a –2 circumstance penalty to their attack rolls if their paths pass through the emanation. Massive ranged weapons and spell effects that don't create physical objects can pass through the emanation with no penalty.
- The area is difficult terrain to creatures attempting to move through it.
- Gases, including creatures in the form of a vapor, can't pass through the emanation. When the emanation arises, such gases are removed from the area, including your space.
- The area, including your space, has breathable air.

Once the magic is used, the ocarina remains a non-magical virtuoso musical instrument.

**Source:** `= this.source` (`= this.source-type`)
