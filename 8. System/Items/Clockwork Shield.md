---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'gp': 1300}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This brass-coated, steel shield (Hardness 12, HP 90, BT 45) has *+2 striking shield spikes* made of bronze gears.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The shield's gears begin to spin, subtly adjusting the shield's position as you fight. You gain an extra reaction this turn and at the start of each of your turns for the next minute that you can use only to Shield Block.

**Source:** `= this.source` (`= this.source-type`)
