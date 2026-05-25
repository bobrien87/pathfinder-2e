---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Sonic]]", "[[Versatile p]]"]
price: "{'gp': 2000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This massive, curved blade roars when it crashes down on opponents, seemingly intent on subduing them with sheer force. It's said materials for the first thundering fury dadaos came from the hide of Yorak, the Horned Thunder, a legendary kaiju that roams the Shanguang desert. The lack of embellishments on this *+2 striking thundering greatsword* belies a weapon of deadly efficacy.

**Activation—Thunder Dance** `pf2:1` (concentrate)

**Frequency** once per day

**Effect** You infuse the thundering fury dadao with the speed of lightning and the force of thunder. The weapon gains the agile and forceful traits for one round. You can Sustain this activation for up to 1 minute.

> [!danger] Effect: Thundering Fury Dadao

**Source:** `= this.source` (`= this.source-type`)
