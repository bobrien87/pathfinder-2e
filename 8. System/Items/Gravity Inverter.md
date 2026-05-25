---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 300}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you Activate a gravity inverter, you can either place it in an adjacent space or toss it up to 30 feet away. Once you've done so, this metallic device implodes, creating a @Template[cylinder|distance:10]{10-foot-radius, 40-foot-tall cylinder} of unstable gravity that lasts for 4 rounds.

All creatures and objects in the area when a gravity inverter is activated, who enter the area, or who begin their turn in the area float upward 10 feet, stopping harmlessly if they collide with a solid object or reach the top of the cylinder. While floating, a creature is [[Off Guard]] and can't move unless they Push Off a surface or Fly. Pushing Off is a single action that has the move trait, allowing the creature to move half its Speed in a straight line through the area (if the creature remains in the area, this momentum will be disrupted by the gravity inverter at the beginning of the creature's next turn, as noted above). At the end of the duration, this gravity well fades—all creatures floating fall to the ground, taking falling damage as appropriate. Creatures who can fly are immune to this fall damage.

**Source:** `= this.source` (`= this.source-type`)
