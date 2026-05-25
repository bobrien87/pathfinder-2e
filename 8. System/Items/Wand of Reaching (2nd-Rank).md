---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 250}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This long, slender wand is constructed of silver, polished to a mirror shine.

**Activate** Cast a Spell; This activation takes `pf2:2` if the spell normally takes `pf2:1` to cast, or `pf2:3` if the spell normally takes `pf2:2`

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell. Its range increases by 30 feet. As normal for increasing ranges, if the spell normally has a range of touch, its range extends to 30 feet.

**Craft Requirements** Supply a casting of a spell of the appropriate rank. The spell must have a casting time of `pf2:1` or `pf2:2`, and must have a range.

**Source:** `= this.source` (`= this.source-type`)
