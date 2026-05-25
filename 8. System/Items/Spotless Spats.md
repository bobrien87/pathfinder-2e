---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 30}"
usage: "worn"
bulk: "—"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

No soldier in a parade or other formal appearance would dare forget their pristine white spats covering their boots. Their presence inspires the wearer to keep the rest of their uniform equally tidy. While wearing the *spotless spats*, your outfit is magically cleaned every 10 minutes, as if by the  spell.

**Source:** `= this.source` (`= this.source-type`)
