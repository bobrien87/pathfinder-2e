---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 425}"
usage: "worneyepiece"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

*Clarity goggles* feature faceted lenses that filter your surroundings from several slightly different angles at once, giving you a sharper picture of them. While wearing the goggles, you gain a +1 item bonus to visual Perception checks.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You focus on your environment and the creatures around you to see them as they really are. The GM rolls a secret counteract check using your Perception bonus against any illusion effect created by a 3rd-rank or lower spell or a creature of 8th level or lower. You must be able to see the illusion, and it must be within 60 feet. If the check succeeds, you see through the illusion for 10 minutes.

*PFS Note:* The Item Level determines the counteract rank, not the character level.

**Source:** `= this.source` (`= this.source-type`)
