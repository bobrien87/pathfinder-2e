---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "wornmask"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Originally designed by a fanatical sect of Gozren priests, *goz masks* were designed to help navigate the area around the Eye of Abendego. The masks couldn't contend with the might of the storm, but people all around the Mwangi Expanse still use them. These masks are typically made of wood and sport round, exaggerated features.

**Activate** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** You ignore [[Concealment]] caused by fog, smoke, and other obscuring vapors for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
