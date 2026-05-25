---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Deadly d6]]", "[[Monk]]", "[[Reach]]", "[[Shove]]"]
price: "{'gp': 2}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A pantograph gauntlet is a heavy, fist-like weight, mounted on an extendable frame and attached to your outer arm with a series of leather straps. The frame's set of mechanical linkages connected at various hinges allow movements to propagate across the frame based on reshaping parallelograms, further controlled by a crossbar grasped in your hand. A pantograph gauntlet is driven by your own motion and mirrors your arm's movements-a punch thrown with your fist moves the pantograph, extending the weight out at a rapid speed to land blows up to 10 feet away. In some regions, such as Alkenstar and Ustalav, pantograph gauntlets are occasionally constructed entirely of metal and fashioned in the likeness of oversized arms, incorporating a complex system of gears or a miniature steam engine in place of the simpler pantograph mechanism.

**Source:** `= this.source` (`= this.source-type`)
