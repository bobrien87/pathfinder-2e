---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Magical]]"]
price: "{'gp': 30}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This large feather is garishly colored in reds, oranges, and yellows, but on closer inspection, it's simply a particularly large chicken feather that's been dyed. Carrying the feather provides a boost to your self-confidence, but it might lead you into dangerous situations.

**Activate—Overconfident Facade** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** For 1 hour, the feather grants you a +1 item bonus to Intimidation checks to [[Demoralize]] and Diplomacy checks to [[Make an Impression]], but a –1 item penalty on Acrobatics and Athletics checks, as your inflated confidence leads you to attempt things you simply cannot do.

> [!danger] Effect: Overconfident Facade

**Source:** `= this.source` (`= this.source-type`)
