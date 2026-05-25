---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Cursed]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
bulk: "1"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made from constrictor snakeskin, the strips of this *+1 leather armor* wrap around you like an anaconda might wrap around its victim. The first time you roll a 1 on any attack roll or check after donning the armor, it fuses with you and constricts. It constricts anytime you roll a 1 on any attack roll or check thereafter. When the armor constricts, you're [[Restrained]] for 1 round.

**Activate** `pf2:1` (concentrate, manipulate)

**Effect** The armor wraps around you, allowing you to don it by the time the activation finishes.

**Source:** `= this.source` (`= this.source-type`)
