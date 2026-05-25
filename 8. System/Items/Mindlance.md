---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Arcane]]", "[[Concussive]]", "[[Fatal d12]]", "[[Kickback]]", "[[Mental]]", "[[Nonlethal]]"]
price: "{'gp': 500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 striking arquebus* is used by caravan guards to nonlethally—though powerfully—deter large game and bandits. When fired, the spark gun deals mental damage and adds the nonlethal trait to the attack. Each mindlance also includes a reinforced stock that benefits from any fundamental runes on the firearm. When you critically succeed at an attack roll with a mindlance, the target becomes [[Frightened]] 2 unless it succeeds at a DC 24 [[Will]] save.

**Source:** `= this.source` (`= this.source-type`)
