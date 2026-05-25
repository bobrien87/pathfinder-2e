---
type: item
source-type: "Remaster"
level: "19"
traits: ["[[Bulwark]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 35000}"
bulk: "4"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you are wearing this armor, you're a veritable battering ram. This *+3 greater resilient fortification full plate* is topped with a reinforced helmet shaped like a ram's head that enables you to smash through doors and gates.

**Activate—Ram** `pf2:2` (manipulate)

**Frequency** once per hour

**Effect** You Stride up to 60 feet in a straight line. If you end your movement adjacent to an enemy, object, or structure, you can smash it. If you smash an enemy, you deal bludgeoning damage equal to the total distance traveled (DC 39 [[Fortitude]] save). Objects and structures you smash take damage equal to twice the distance traveled.

**Source:** `= this.source` (`= this.source-type`)
