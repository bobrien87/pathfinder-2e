---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 450}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

You pride yourself on being well prepared with weaponry for any situation. Your dark-gray boots might appear mundane, but you know that they can conjure a blade at any moment. Even the most thorough of searches can't find a knife that doesn't exist yet.

**Activate—Draw Secret Blade** `pf2:1` (manipulate)

**Frequency** once per hour

**Effect** You reach down to your boot, draw a *+1 striking dagger* from it, and make a ranged or melee Strike with it. This dagger is created magically and does not exist before being drawn. The dagger remains a physical object until the next time you use Draw Secret Blade, and it disappears as a new blade is created.

**Source:** `= this.source` (`= this.source-type`)
