---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Light]]", "[[Magical]]"]
price: "{'gp': 3}"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Shining ammunition* gives off a faint glow. When shot, it sheds bright light in a 20-foot radius (and dim light to the next 20 feet) for 10 minutes. If it hits a target, it sticks, causing the target to shed light in the same radius. A creature can remove the ammunition with an Interact action, but the ammunition itself continues to glow for the rest of the duration or until destroyed.

> [!danger] Effect: Shining Ammunition

**Source:** `= this.source` (`= this.source-type`)
