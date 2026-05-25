---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "applied-to-footwear"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Trackless runes are common among hunters and trappers, as well as thieves and anyone fleeing pursuit. While wearing trackless footwear, you have a +4 item bonus to the DC to track you. However, this bonus doesn't stack with the status bonus from [[Vanishing Tracks]].

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** You extend the effect of your rune out to a @Template[emanation|distance:20]. The emanation remains for 8 hours, affecting up to 10 creatures of your choice within the area. You can Dismiss this effect.

**Source:** `= this.source` (`= this.source-type`)
