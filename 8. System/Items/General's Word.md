---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Magical]]", "[[Shove]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The mere act of wielding this heavy *+2 greater striking thundering mace* grants you a distinct air of authority and gravitas. While wielding the weapon, you can cast [[Bullhorn]] as a 1st-rank cantrip at will.

**Activate—Battlefield Broadcast** `pf2:2` (concentrate, linguistic, manipulate, mental, occult)

**Frequency** once per day

**Effect** The weapon amplifies your force of personality across the battlefield with the effects of [[Telepathy]] for 10 minutes, except the range is 500 feet. The effect ends immediately if you drop your weapon.

**Craft Requirements** Supply one casting of *bullhorn* and *telepathy*.

**Source:** `= this.source` (`= this.source-type`)
