---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 85}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Affectionately called "the healer's kit of the Plane of Wood," *therapeutic snap peas* are specially cultivated snap pea pods overflowing with restorative magic.

**Activate—Healing Pod** `pf2:2` (concentrate, manipulate)

**Effect** You break the snap pea pod in half, unleashing its restorative healing energy. Up to 5 creatures of your choice within 30 feet regain @Damage[(4d8+10)[healing]]{4d8+10 Hit Points} and gain a +2 item bonus to all saves against poisons or diseases for 1 minute.

> [!danger] Effect: Therapeutic Snap Peas

**Activate—Beanstalk** 10 minutes (manipulate)

**Effect** You plant the *therapeutic snap peas* in a square of open ground, after which they rapidly grow into a 10-foot-tall beanstalk that remains in place for 8 hours. The beanstalk's enormous pea pods provide a full day's food for up to 8 living creatures of size Large or smaller, which must be eaten before the beanstalk expires. Any creature that eats the pea pods also immediately heals 30 healing Hit Points and can attempt a new saving throw against one poison or disease afflicting them.

**Source:** `= this.source` (`= this.source-type`)
