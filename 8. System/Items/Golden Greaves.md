---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "worn"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These shiny greaves made of splinted metal coated with gold protect the shins and help you stand your ground in the heat of battle. While wearing the greaves, you gain a +1 item bonus to your Fortitude DC against forced movement effects and to your Reflex DC against effects that would knock you [[Prone]].

**Activate—Make Them Fall** `pf2:r` (concentrate, misfortune)

**Frequency** once per day

**Trigger** An enemy fails to [[Reposition]], [[Shove]], or [[Trip]] you

**Effect** Your golden greaves glow with a strange light, and you move your legs in just the right way to completely throw off your opponent. Your opponent instead critically fails on the triggering check.

**Source:** `= this.source` (`= this.source-type`)
