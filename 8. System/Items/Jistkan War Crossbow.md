---
type: item
source-type: "Remaster"
level: "18"
traits: ["[[Backstabber]]", "[[Magical]]"]
price: "{'gp': 22000}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These *+3 greater striking grievous arbalests* are a fantastically intricate creation of the ancient Jistka Imperium, seamlessly weaving together mechanical ingenuity and powerful magic to create one of the deadliest projectile weapons ever devised by human hands.

**Activate—Bolt of War** `pf2:1`

**Frequency** once per 10 minutes

**Effect** Make a Strike with the Jistkan war crossbow, ignoring the penalty for making a Strike within your second or third range increment. Additionally, the arbalest gains the splash trait and deals 10 piercing splash damage for this Strike.

**Source:** `= this.source` (`= this.source-type`)
