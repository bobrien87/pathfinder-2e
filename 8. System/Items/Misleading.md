---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 8000}"
usage: "etched-onto-light-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune attempts to obfuscate your location through illusory trickery. When you're [[Concealed]], the DC of the flat check to target you with an effect is 6 instead of 5.

**Activate**`pf2:2` (concentrate)

**Frequency** once per day

**Effect** The armor casts mislead, affecting you. It lasts until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
