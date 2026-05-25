---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1000}"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A dark haze seems to envelop you when you wear this dusky *+1 resilient shadow leather armor*, muffling your steps and concealing your movement. While wearing the armor, you can create even deeper shadows to hide within.

**Activate—Shroud** `pf2:2` (arcane, concentrate, manipulate)

**Frequency** once per day

**Effect** You cast [[Darkness]] as a 4th-rank spell centered on you.

**Craft Requirements** Supply a casting of *darkness* (4th rank).

**Source:** `= this.source` (`= this.source-type`)
