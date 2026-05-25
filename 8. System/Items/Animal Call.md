---
type: item
source-type: "Remaster"
level: "0"
price: "{'sp': 5}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Animal calls are often whistles or similar devices that imitate the calls of animals. Each call is for a specific type of animal, such as a duck or bear. When you use the call, it gives you a +1 item bonus to [[Command an Animal]], provided the animal is of the type as the call. You also do not take a circumstance penalty when attempting to [[Demoralize]] that animal for not sharing a language.

**Source:** `= this.source` (`= this.source-type`)
