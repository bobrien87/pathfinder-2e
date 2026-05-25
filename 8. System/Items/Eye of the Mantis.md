---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This 1-inch tall figurine depicts a crouched praying mantis. It's usually carved from green jade, crimson marble, or purple porphyry. Regardless of the figurine's material composition, its gemstone eyes are always a dull ruby red that seems to drink light.

**Activate—Phantasmal Assassin** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast 4th-rank [[Vision of Death]] (DC 28 [[Will]] save). To the target, it always appears as if they are being attacked by an immense praying mantis.

**Activate—Scouting Eye** 1 minute (concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Scouting Eye]].

**Source:** `= this.source` (`= this.source-type`)
