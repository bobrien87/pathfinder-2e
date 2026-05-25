---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Versatile p]]"]
price: "{'gp': 500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Hewn from a solid block of ensorcelled stone, this *+1 striking greatsword* is monumental in heft as well as destructive force. The weapon is named for the disbelieving leaders of the Seventh Army of Exploration, who denied the power of such a weapon and claimed their losses came from natural disasters. When wielded against creatures that are larger than you, the sword gains the sweep trait.

**Activate—Shatter Legions** `pf2:2` (earth)

**Frequency** once per day

**Effect** You smash the sword down upon the ground with the anger of a conquered land and a subjugated people. Each creature in a @Template[type:cone|distance:30] takes 4d12 piercing damage with a DC 24 [[Reflex]] save as the earth shatters beneath their feet. Until the beginning of your next turn, you gain the benefits of standard cover from the broken soil around you.

**Source:** `= this.source` (`= this.source-type`)
