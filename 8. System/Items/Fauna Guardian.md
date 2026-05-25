---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 675}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *fauna guardian* is a tattoo of an animal, which you can temporarily animate to protect you. The animal must be chosen when you get the tattoo, and can be any common animal of 4th level or lower. (Your GM might allow other options.)

**Activate** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** You animate your tattoo using the duration and other parameters of a 5th-rank [[Summon Animal]] spell. It appears in a space adjacent to you. If your tattoo animal drops to 0 HP, the activation ends, and the inanimate tattoo returns to your skin.

**Source:** `= this.source` (`= this.source-type`)
