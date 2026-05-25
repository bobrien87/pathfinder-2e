---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 30}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Northern peoples design these tattoos to protect against cold weather, typically in geometric patterns with a combination of straight lines and whorls. This tattoo negates any damage you take from severe environmental cold and reduces damage you take from extreme cold to equal that of severe cold.

**Activate** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** Until the end of your next turn, you ignore difficult terrain and greater difficult terrain from ice and snow and don't risk falling when crossing ice.

**Source:** `= this.source` (`= this.source-type`)
