---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 40}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

When you Activate an explosive mine, you place it on the ground in a square within your reach, priming it to explode when a creature steps on that square. If you have time in advance to prepare, you can place the mine on the ground before activating it, and you or an ally can try to use Stealth to [[Conceal an Object]] before you Activate the mine. If you don't Conceal the mine, its position is obvious at a glance.

Once activated, the mine is primed to explode when enough pressure is placed on the square where it's located. Typically, this occurs when a Small or larger creature moves onto the square, though it could happen if a creature intentionally places pressure on the square from a distance to safely trigger the mine. Once triggered, the mine explodes, dealing @Damage[6d6[fire]|options:area-damage] damage to any creatures in a @Template[type:emanation|distance:5] with a DC 20 [[Reflex]] save.

**Source:** `= this.source` (`= this.source-type`)
