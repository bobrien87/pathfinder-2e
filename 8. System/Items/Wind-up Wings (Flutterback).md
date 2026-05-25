---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Clockwork]]"]
price: "{'gp': 50}"
usage: "attached-to-a-thrown-weapon"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These delicate clockwork wings enable thrown weapons to soar through the air at high speeds, performing turns and other aerial maneuvers mid-flight. Wind-up wings also have different types of special effects depending on the type. Wind-up wings must be attached to a thrown weapon and wound to function. A thrown weapon with an attached set of wind-up wings can't have anything else attached to it, or the wings cease to function. Attaching or detaching a pair of wind-up wings to a thrown weapon requires a repair kit, and the process takes 10 minutes. Winding an attached pair of wind-up wings takes three Interact actions. There are a variety of wind-up wings, with different effects.

When you make a thrown Strike with the weapon to which a pair of flutterback wind-up wings are attached, and the wings are wound, the wings fly the weapon back to your hand after the Strike is complete. If your hands are full when the weapon returns, the wings hover in place 3 feet above the ground. At the end of your turn, the wings are wound down; they don't function again until wound. If you aren't holding the weapon when the flutterback wind-up wings become wound down, the weapon falls to the ground.

**Source:** `= this.source` (`= this.source-type`)
