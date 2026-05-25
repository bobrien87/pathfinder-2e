---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 80}"
usage: "worngloves"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These clean, white gloves never show signs of blood, even when used to stitch up wounds or treat other ailments. They give you a +1 item bonus to Medicine checks.

**Activate—Healer's Touch** A (manipulate)

**Frequency** once per day

**Effect** You can soothe the wounds of a willing, living, adjacent creature, restoring @Damage[(2d6+7)[vitality,healing]|shortLabel:true] Hit Points to that creature. This is a healing vitality effect. You can't harm undead with this healing.

**Source:** `= this.source` (`= this.source-type`)
