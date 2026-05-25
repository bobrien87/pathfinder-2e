---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Concussive]]", "[[Elf]]", "[[Fatal d10]]", "[[Parry]]"]
price: "{'gp': 7}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Neither dawnsilver nor a tree, this long gun takes its name from the legends of the elves of Jinin and is most commonly found within the nation. An elegant weapon, a mithral tree does somewhat resemble a tree; its fanned stock and long, sweeping barrel reinforced with metal rings enable a wielder to parry melee attacks while moving back into safe firing range.

**Source:** `= this.source` (`= this.source-type`)
