---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]"]
price: "{'gp': 450}"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This minor reinforced buckler (Hardness 6, HP 50, BT 25) is a lightweight metal disk with a rounded bump at the center. The shield gives off a light hum near magic.

**Activate—Spell Amp** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You throw your shield up to 30 feet into an unoccupied space you can see. The shield magically floats in the space as a focal point for your magic for 1 minute. You can cast spells using the shield as your point of origin, calculating range and cover from its space instead of yours. You can Dismiss this effect, causing the shield to fly back to your hand. If the shield breaks, the effect ends.

**Source:** `= this.source` (`= this.source-type`)
