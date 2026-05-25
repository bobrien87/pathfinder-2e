---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Bulwark]]", "[[Entrench ranged]]", "[[Ponderous]]"]
price: "{'gp': 32}"
bulk: "5"
source: " Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Dwarves of Dongun Hold developed fortress plate, which is still popular in Alkenstar and Dongun Hold. A trained wearer can adjust the articulated armor's overlapping layers of plates and panels to provide protection from missiles.

**Source:** `= this.source` (`= this.source-type`)
