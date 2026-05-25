---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Arcane]]", "[[Capacity 3]]", "[[Concussive]]", "[[Fatal d8]]", "[[Fire]]"]
price: "{'gp': 2900}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+2 greater striking pepperbox* cycles through several magical cores, swapping in new ones while the previous ones cool. The gun deals fire or electricity damage, alternating with each attack as it rotates cores. Arcadian gunslingers liken the rotating cores to a group of dancers sharing the spotlight.

**Activate** `pf2:2` (manipulate)

**Frequency** once per day

**Effect** The spark dancer casts either *[[Fireball]]* or *[[Lightning Bolt]]*, depending on whether the current core would deal fire or electricity damage, as a 7th-rank arcane spell (DC 30 [[Reflex]] save).

**Source:** `= this.source` (`= this.source-type`)
