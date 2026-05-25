---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 175}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Magical reagents slosh inside this rime-frosted pottery jar the size of a human head. Despite appearing to be rimed in hoarfrost, the jar is warm to the touch. Ilverani wizards create *rime jars* to sustain themselves during the coldest winter nights.

**Activate—Siphon Chill** `pf2:3` (manipulate)

**Effect** The jar draws off the cold and warms your body. If you have the [[Fatigued]] condition caused by exposure to environmental cold, it removes the condition. For 8 hours after applying the rime, you treat extreme cold as severe cold.

**Source:** `= this.source` (`= this.source-type`)
