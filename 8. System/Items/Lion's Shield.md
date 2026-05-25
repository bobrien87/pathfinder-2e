---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Magical]]"]
price: "{'gp': 245}"
bulk: "1"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This steel shield (Hardness 6, HP 36, BT 18) is forged into the shape of a roaring lion's head. The lion's head functions as *+1 striking shield boss* that can't be removed from the shield.

**Activate—Lion's Bite** `pf2:f` (manipulate)

**Frequency** once per day

**Requirements** Your shield is raised

**Effect** You animate the lion's head, making a melee Strike with it. The shield's biting maw is a martial melee weapon that deals 2d6 piercing damage and has the deadly d6 trait; it can't be enhanced by runes.

The shield remains animated for 1 minute, during which time you can Strike with it each time you Raise the Shield, as well as with a Strike action.

> [!danger] Effect: Lion's Bite

**Source:** `= this.source` (`= this.source-type`)
