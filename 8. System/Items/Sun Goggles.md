---
type: item
source-type: "Remaster"
level: "3"
price: "{'gp': 20}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder NPC Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These goggles are usually fitted with a polished piece of yellowtoned crystal, allowing the wearer some protection against the brightness of the sun. Near the Crown of the World, a version of these goggles exists where the crystal is replaced by thin slits, mitigating the effects of the sun's reflection on snow.

When wearing these goggles, you gain a +1 item bonus to saving throws against effects that could inflict the [[Dazzled]] condition.

**Source:** `= this.source` (`= this.source-type`)
