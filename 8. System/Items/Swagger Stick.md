---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Magical]]"]
price: "{'cp': 0, 'gp': 75, 'pp': 0, 'sp': 0}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This stick is a decorative wooden baton with a metal cap on one end and a stylized handle in the shape of a horse or other martial beast on the other. Mundane swagger sticks are carried by officers in armies all across Golarion. This one is made of particularly fine wood, with an aged silver cap and handle, and small garnets for the creature's eyes.

**Activate—Swagger** `pf2:1` (manipulate, visual)

**Frequency** once per day

**Effect** You dramatically swing, twirl, or otherwise brandish the swagger stick to direct your troops. All allied creatures within 30 feet who can see your display gain +1 status bonus to attack rolls, Fortitude saves, and Will saves against mental effects for 1 round.

> [!danger] Effect: Swagger

**Source:** `= this.source` (`= this.source-type`)
