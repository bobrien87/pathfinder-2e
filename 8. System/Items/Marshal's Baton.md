---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 60, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This short, thick, stick-like object is crafted of wood and steel. Precious metals decorate the grip, and fine filigree marks the caps on each end. A marshal's baton grants you a +1 item bonus to Diplomacy and Intimidation checks against troops, individual soldiers, and military leaders.

**Activate—Stentorian Order** `pf2:2` (auditory, manipulate)

**Frequency** once per day

**Effect** You issue a command in a booming voice while gesturing with the marshal's baton and cast a [[Command]] spell (DC 18). This spell affects troops and swarms as if they were a single creature.

**Source:** `= this.source` (`= this.source-type`)
