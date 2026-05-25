---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 300}"
usage: "affixed-to-a-ranged-weapon"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a ranged Strike with the affixed weapon while hidden or undetected.

This long strip of linen is tightly wound around the barrel of the affixed firearm or the grip of a bow. When activated, the talisman's magic dampens the sound of the triggering shot, rendering it completely silent, and additionally skews the angle of the shot, so it appears to come from a different location and direction than your actual position. You don't become automatically observed to any creatures due to making the triggering Strike.

**Source:** `= this.source` (`= this.source-type`)
