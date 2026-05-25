---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 500}"
usage: "etched-onto-light-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Light seems to partially penetrate this armor.

**Activate—Go Invisible** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** With a thought, you become invisible for 1 minute, gaining the effects of a 2nd-rank [[Invisibility]] spell.

**Craft Requirements** Supply one casting of *invisibility*.

**Source:** `= this.source` (`= this.source-type`)
