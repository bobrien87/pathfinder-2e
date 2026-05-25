---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]"]
price: "{'gp': 3000}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This moderate reinforced standard-grade duskwood tower shield (Hardness 8, HP 84, BT 42) is slightly wider than standard. Designed for bodyguards, it grants the user a small burst of speed to save themself and others from harm.

**Activate—By Your Side** `pf2:r`

**Frequency** once per day

**Trigger** An effect within 15 feet would deal damage in an area and require a saving throw

**Requirements** Your shield is raised

**Effect** You Stride up to 15 feet and grant yourself and creatures adjacent to you after the movement a +2 circumstance bonus to the saving throw against the triggering effect.

> [!danger] Effect: Vanguard's Shield

**Source:** `= this.source` (`= this.source-type`)
