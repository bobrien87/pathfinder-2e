---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 1000}"
usage: "held-in-two-hands"
bulk: "3"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

One end of this heavy cylinder of steel has been forged in the likeness of a dragon turtle's head, the mouth gaping wide. Grips at the opposite end allow one to hold and aim this heavy cannon-like barrel with both hands. As long as you're carrying dragon turtle artillery while you're on a boat or ship, the DC for any effect to capsize that vehicle increases by 4.

**Activate—Turtle's Tsunami** `pf2:2` (concentrate, manipulate, water)

**Frequency** once per day

**Effect** A @Template[type:cone|distance:50] of surging water blasts from the mouth of the cannon, dealing 10d6 bludgeoning damage to creatures in its area of effect (DC 27 [[Reflex]] save). A creature that fails its save is knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
