---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]"]
price: "{'gp': 6500}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *major* *spider gun* is a *+2 greater striking* weapon. It's a distinct type of martial firearm made from the fangs and spinneret of a Large spider. It deals 1d10 poison damage with a range increment of 30 feet and reload 1. On a critical hit, the venom clings to the target and they take persistent poison damage equal to @Damage[(1d4+@item.system.damage.dice)[persistent,poison]]. A spider gun does not add critical specialization effects. The gun can be activated to fire webbing that hampers other creatures.

**Activate—Web Shot** `pf2:1` (manipulate)

**Frequency** once per round

**Effect** You fire a mass of webbing at a square within 30 feet. That square becomes covered in webbing for 1 minute. A square covered with the webbing from a spider gun can be cleared by a single attack or effect that deals at least 25 slashing damage or 15 fire damage. A square has AC 5, and it automatically fails its saving throws. The first time each turn a creature in the webbing begins to use a move action or enters the webbing during a move action, it must attempt an DC 34 [[Athletics]] check{Athletics} check or DC 34 [[Reflex]] save{Reflex} save against DC 34. On a success, it moves normally through the webbing and clears away the webbing from any squares it enters this turn. On a failure, it treats squares of webbing as difficult terrain this turn, and on a critical failure, it's [[Immobilized]] for 1 round or until it Escapes (DC 34) or destroys the webbing.

**Craft Requirements** The initial raw materials for the spider gun must include the fangs and spinneret of a giant spider or other Large spider.

**Source:** `= this.source` (`= this.source-type`)
