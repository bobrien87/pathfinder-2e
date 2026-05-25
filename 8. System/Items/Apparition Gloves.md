---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Illusion]]", "[[Magical]]"]
price: "{'gp': 25}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This set of gloves translates whatever the wearer says into the signed version of that language by projecting a ghostly, translucent version of the wearer's hands in front of them. The apparition is a purely visual illusion used for communication, so it can't move on its own, nor can it hold or manipulate objects, or attack.

**Source:** `= this.source` (`= this.source-type`)
